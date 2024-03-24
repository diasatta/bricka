from abc import ABC
import html
from contextvars import ContextVar
from uuid import uuid4
from copy import deepcopy
from enum import Enum
from typing import cast
import urllib.parse
from bricka.stylesheet import StyleSheet
from bricka.style import Rule
from bricka.attrs import GlobalAttrs

class AttrType(Enum):
  BOOL = 0
  PSEUDO_BOOL = 1
  TEXT = 2
  HTML = 3
  URL = 4
  JS = 5
  STYLE = 6
  OTHER = 7

CONFLICTING_ATTRS: tuple[str, ...] = ("as", "async", "class", "for", "is")

PREFIXED_ATTRS: tuple[str, ...] = ("aria", "data", "user")

_with_stack_var: ContextVar[str | None] = ContextVar('_with_stack', default=None)

class Node(ABC):
  tag_name: str = "node"
  inline: bool = False

  _with_stack: dict[str | None, list[list["Node"]]] = {}

  def __init__(self, *nodes: "Node | str", **attrs) -> None:
    self.parent: "Node | None" = None
    self._nodes: list[Node] = []
    self._attrs: dict[str, str] = {}
    self._css: StyleSheet = StyleSheet()

    for attr in attrs:
      if attr == "css":
        continue

      self._attrs[attr] = attrs[attr]

    for node in nodes:
      self.insert(node)

    if _with_stack_var.get() is None:
      _with_stack_var.set(uuid4().hex)  
      self._with_stack[_with_stack_var.get()] = []

    if Node._with_stack.get(_with_stack_var.get(), None):
      self.collect()    

  @property
  def attrs(self) -> dict[str, str]:
    return self._attrs    
  
  @property
  def css(self) -> StyleSheet:
    return self._css

  def __str__(self) -> str:
    return self.render()
  
  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    markup = ""
    
    inline = self.inline or spaces is None or not self._nodes
    new_line = "" if inline else "\n"

    markup += self.start_tag(level, spaces)
    markup += new_line
    markup += self.inner_html(level+1, spaces, escape)
    markup += self.end_tag(level, spaces)

    return markup
  
  def render_inline(self, level: int = 0) -> str: 
    return self.render(level=level, spaces=None)
  
  def start_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    indent = "" if spaces is None else " " * level * spaces
    
    attrs = self.render_attrs()
    html = f"{indent}<{self.tag_name}{' ' + attrs if attrs != '' else ''}>"

    return html 
  
  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    inline = self.inline or spaces is None or not self._nodes

    indent = "" if inline else " " * level * (0 if spaces is None else spaces)
    new_line = "" if inline else "\n"
    end_indent = "" if inline is None else indent

    return f"{new_line}{end_indent}</{self.tag_name}>"
  
  def inner_html(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    markup = ""
    inline = self.inline or spaces is None or not self._nodes
    new_line = "" if inline else "\n"

    markup += new_line.join(node.render(level, None if inline else spaces) for node in self._nodes)  

    return html.escape(markup) if escape else markup
  
  def insert(self, child: "str | int | float | Node | None", index: int | None = None) -> "Node": 
    if type(child) == Root:
      i = -1
      while child._nodes:
        node: Node | None = child.take_first()
        i += 1  
        if index is None:
          self.insert(node)
        else:  
          self.insert(node, index+i)

      return child  
    
    if child is None:
      child_ = Text("") 
    elif type(child) in (str, int, float, bool):
      child_ = Text(str(child)) 
    else:
      child_: Node = child # type: ignore

    if child_.parent is not None:
      raise Exception(f"Node {type(self)} already having a parent. Free the node before inserting it again.")  

    child_.parent = self 
    if index is None:
      self._nodes.append(child_)
    else:  
      self._nodes.insert(index, child_)
    return child_  
  
  def insert_in(self, parent: "Node", index: int | None = None) -> "Node":
    parent.insert(self, index)

    return parent
  
  def prepend_to(self, container: "Node") -> "Node":
    return self.insert_in(container, 0)  
  
  def prepend(self, node: "Node | str | int | float") -> "Node":
    return self.insert(node, 0)   

  def append_to(self, container: "Node") -> "Node":
    self.insert_in(container)
    return container 
  
  def append(self, node: "Node | str | int | float") -> "Node":
    return self.insert(node)
  
  def at(self, index: int) -> "Node | None":
    if len(self._nodes) > index:
      return self._nodes[index]
    
    return None
  
  def first(self) -> "Node | None":
    return self.at(0) 
  
  def last(self) -> "Node | None":
    return self.at(-1) 
  
  def take_at(self, index: int) -> "Node | None":
    if len(self._nodes) > index:
      node = self._nodes.pop(index)
      node.parent = None
      return node
    
    return None
  
  def take_first(self) -> "Node | None":
    return self.take_at(0)
  
  def take_last(self) -> "Node | None":
    return self.take_at(-1)
  
  def collect(self) -> "Node":
    if self.parent is not None:
      raise Exception(f"Node already having a parent. Detach the node before collecting it.")

    Node._with_stack[_with_stack_var.get()][-1].append(self)
    return self
  
  def free(self) -> "Node | None":
    old_parent = self.parent
    if self.parent is not None:
      self.parent._nodes.remove(self)
      self.parent = None  

    return old_parent 
   
  def __enter__(self) -> "Node":   
    Node._with_stack[_with_stack_var.get()].append([])
    return self

  def __exit__(self, type_, value, traceback):
    if type_:
      self._with_stack[_with_stack_var.get()].pop()
    else:  
      for node in self._with_stack[_with_stack_var.get()].pop():
        if node.parent is None:
          self.insert(node)

  def __iter__(self):
    return iter(self._nodes)     

  def __rshift__(self, parent: "Node") -> "Node":
    parent.insert(self)
    return parent

  def __rrshift__(self, text: str | int | float | None) -> "Node":
    self.insert(text)
    return self  

  def __lshift__(self, child: "str | int | float | Node | None") -> "Node":
    child_ = self.insert(child)
    return self if type(child) == Root else child_ 
  
  def __radd__(self, text: str | int | float) -> "Root":
    root = Root()
    root.insert(text)
    root.insert(self)
    return root

  def __add__(self, node: "Node | str | int | float") -> "Root":
    root = Root()
    root.insert(self)
    root.insert(node)

    return root   

  def __mul__(self, count: int) -> "Root":
    root = Root()
    for _ in range(count):
      root.insert(deepcopy(self))

    return root
  
  def __rmul__(self, count: int) -> "Container":    
    return self.__mul__(count) 
  
  @classmethod
  def attr_html_name(cls, python_name: str) -> str:
    return python_name.removesuffix("_").replace("_", "-")
  
  def attr_type(self, element_name: str, attr_name: str) -> AttrType:
    types = ATTR_TYPES.get(element_name, None)
    name = self.attr_html_name(attr_name)

    if types is None:      
      return ATTR_TYPES["*"].get(name, AttrType.TEXT)

    return cast(AttrType, ATTR_TYPES[element_name].get(name, ATTR_TYPES["*"].get(name, AttrType.TEXT)))
  
  def render_attr(self, name: str, value: str | bool | None) -> str:
    name = self.attr_html_name(name) # TODO

    if type(value) == bool:
      if value:
        return name
      else:
        return ""

    if value is None:
      return ""

    if self.attr_type(self.tag_name, name) == AttrType.URL:
      return f'{name}="{urllib.parse.quote(value)}"' # type: ignore
    else:  
      return f'{name}="{html.escape(str(value), quote=True)}"'

  def render_attrs(self) -> str:
    attrs: list[str] = []
    output = ""
    for key, value in self._attrs.items():
      if type(value) == dict:
        if key in PREFIXED_ATTRS:
          l = []
          for k, v in value.items(): #type: ignore
            l.append(self.render_attr(f'{key}-{k}', v))
            output = " ".join(l)
        else:
          raise TypeError(f"Dict. values not allowed for attribute '{key}'.")
      else:
        output = self.render_attr(key, value)

      attrs.append(output)

    return " ".join(attrs).strip()
  
  def media_layers(self) -> dict:  
    return {}

class Text(Node):
  def __init__(self, text: str = "", escape=True) -> None:
    super().__init__()
    self.text = text
    self.escape = escape

  @property
  def text(self) -> str:
    return self._text

  @text.setter
  def text(self, text: str) -> None:
    self._text = "" if text is None else str(text)

  def render(self, level: int = 0, spaces: int | None = 2) -> str:
    indent = "" if spaces is None else " " * level * spaces
    text = f"{indent}{html.escape(self.text) if self.escape else self.text}"

    return text  
  
  def insert(self, child: "str | int | float | Node", index: int | None = None) -> "Node": 
    raise TypeError(f"Node insertion not allowed in a Text node.") 

  def __rshift__(self, parent: "Node") -> "Node":
    if type(parent) == Text:
      parent.text += self.text
      self.text = ""
    else:  
      parent.insert(self)

    return parent
  
  def __rrshift__(self, text: str | int | float) -> "Text":
    self.text += str(text)
    return self  
  
  def __lshift__(self, child: str | int | float | Node) -> "Node":
    if type(child) == Text: 
      self.text += child.text
      child.text = ""
    elif type(child) in (str, int, float, bool):
      self.text += str(child)
    else:  
      self.insert(child)

    return self
  
class Element(Node): 
  tag_name: str = "element"

  def __init__(self, *nodes, **kwargs) -> None:
    super().__init__(*nodes, **kwargs)

    self._css: StyleSheet = StyleSheet()
    css = kwargs.get("css", None)
    if css is not None:
      self.css = css

  @property
  def attrs(self) -> GlobalAttrs:
    return cast(GlobalAttrs, self._attrs)      

  @property
  def css(self) -> StyleSheet:
    return self._css

  @css.setter
  def css(self, rules: Rule | list[Rule] | None):
    if rules is None: # TODO: review
      return 
    
    if type(rules) != list:
      rules = [cast(Rule, rules)]

    for rule in rules:
      if type(rule) != dict:
        return # TODO: remove workaround
        # raise TypeError(f"Argument 'rule' must be of type 'Rule': {rule}")  

      self._css.append_rule(rule)    

  def render_attrs(self) -> str:
    classes = self.attrs.get("class_", "") # Preserve the class attribute
    if (class_names := self.class_names()):
      class_names.append(classes)
      self.attrs["class_"] = " ".join(class_names)

    attrs = super().render_attrs()

    if classes:
      self.attrs["class_"] = classes

    return attrs    
  
  def class_names(self) -> list[str]: 
    names: list[str] = []
    media_layers = self.css.media_layers()

    for media, layers in media_layers.items():
      for i, layer in enumerate(layers):
        for selector in layer:
          suffix = "" if i == 0 else str(i)
          class_name = selector.split(":", 1)[0]
          selector = class_name + suffix
          names.append(selector)

    return names   
  
  def media_layers(self) -> dict:  
    return self.css.media_layers()
  
  # As a polyfill for layers, selector names are suffixed with the layer number to ensure that the last style always wins.
  def render_css(self) -> str:
    output = ""
    # for media, layers in self.css.media_layers().items():
    for media, layers in self.media_layers().items():
      opening = f'\n@media {media} {{\n' if media else ""
      indent = "  " if media else ""
      closing = f'}}\n' if media else ""

      output += opening
      for i, layer in enumerate(layers):
        for selector, declaration in layer.items():
          suffix = "" if i == 0 else str(i)
          parts = selector.split(":", 1)
          class_name = parts[0]
          pseudo = ""
          if len(parts) >= 2:
            pseudo = ":" + parts[1]

          selector = class_name + suffix + pseudo
          output += f"{indent}.{selector} {{ {declaration} }}\n"
      output += closing    

    return output  

class Void(Element):
  tag_name: str = "void"

  def __init__(self, **attrs) -> None:
    super().__init__(**attrs)

  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return ""  
  
  def insert(self, child: "Node", index: int | None = None) -> "Node": 
    raise TypeError(f"Node insertion not allowed in a void element.") 
  
class Container(Element):
  tag_name: str = "container"

  def media_layers(self) -> dict:  
    layers = self.css.media_layers()
    for node in self._nodes:
      layers = StyleSheet.merge_media_layers(layers, node.media_layers())

    return layers 

class Root(Container):
  tag_name: str = "root"

  def start_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return "" 
  
  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return ""
  
  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    return self.inner_html(level, spaces, escape)
  
ATTR_TYPES = {
  "*": {
    "accesskey": AttrType.TEXT,
    "autocapitalize": AttrType.TEXT,
    "autofocus": AttrType.BOOL,
    "class": AttrType.TEXT,
    "contenteditable": AttrType.TEXT,
    "dir": AttrType.TEXT,
    "draggable": AttrType.TEXT,
    "enterkeyhint": AttrType.TEXT,
    "hidden": AttrType.PSEUDO_BOOL,
    "id": AttrType.TEXT,
    "inert": AttrType.BOOL,
    "inputmode": AttrType.TEXT,
    "is": AttrType.TEXT,
    "itemid": AttrType.TEXT,
    "itemprop": AttrType.TEXT,
    "itemref": AttrType.TEXT,
    "itemscope": AttrType.BOOL,
    "itemtype": AttrType.URL,
    "lang": AttrType.TEXT,
    "nonce": AttrType.TEXT,
    "part": AttrType.TEXT,
    "popover": AttrType.TEXT,
    "role": AttrType.TEXT,
    "slot": AttrType.TEXT,
    "spellcheck": AttrType.TEXT,
    "style": AttrType.STYLE,
    "tabindex": AttrType.TEXT,
    "title": AttrType.TEXT,
    "translate": AttrType.TEXT,
    "virtualkeyboardpolicy": AttrType.TEXT,
  },
  "a": {
    "download": AttrType.TEXT,
    "href": AttrType.URL,
    "hreflang": AttrType.TEXT,
    "ping": AttrType.URL,
    "referrerpolicy": AttrType.TEXT,
    "rel": AttrType.TEXT,
    "target": AttrType.TEXT,
    "type": AttrType.TEXT,
  },
  "area": {
    "alt": AttrType.TEXT,
    "coords": AttrType.TEXT,
    "download": AttrType.TEXT,
    "href": AttrType.URL,
    "ping": AttrType.URL,
    "referrerpolicy": AttrType.TEXT,
    "rel": AttrType.TEXT,
    "shape": AttrType.TEXT,
    "target": AttrType.TEXT,
  },
  "audio": {
    "autoplay": AttrType.BOOL,
    "controls": AttrType.BOOL,
    "crossorigin": AttrType.TEXT,
    "loop": AttrType.BOOL,
    "muted": AttrType.BOOL,
    "preload": AttrType.TEXT,
    "src": AttrType.URL,
  },
  "base": {
    "href": AttrType.URL,
    "target": AttrType.TEXT,
  },
  "blockquote": {
    "cite": AttrType.URL,
  },
  "body": {
    "onafterprint": AttrType.JS,
    "onbeforeprint": AttrType.JS,
    "onbeforeunload": AttrType.JS,
    "onblur": AttrType.JS,
    "onerror": AttrType.JS,
    "onfocus": AttrType.JS,
    "onhashchange": AttrType.JS,
    "onlanguagechange": AttrType.JS,
    "onload": AttrType.JS,
    "onmessage": AttrType.JS,
    "onoffline": AttrType.JS,
    "ononline": AttrType.JS,
    "onpopstate": AttrType.JS,
    "onredo": AttrType.JS,
    "onresize": AttrType.JS,
    "onstorage": AttrType.JS,
    "onundo": AttrType.JS,
    "onunload": AttrType.JS,
  },
  "button": {
    "autofocus": AttrType.BOOL,
    "disabled": AttrType.BOOL,
    "form": AttrType.TEXT,
    "formaction": AttrType.URL,
    "formenctype": AttrType.TEXT,
    "formmethod": AttrType.TEXT,
    "formnovalidate": AttrType.BOOL,
    "formtarget": AttrType.TEXT,
    "name": AttrType.TEXT,
    "type": AttrType.TEXT,
    "value": AttrType.TEXT,
  },
  "canvas": {
    "height": AttrType.TEXT,
    "width": AttrType.TEXT,
  },
  "col": {
    "span": AttrType.TEXT,
  },
  "colgroup": {
    "span": AttrType.TEXT,
  },
  "data": {
    "value": AttrType.TEXT,
  },
  "del": {
    "cite": AttrType.URL,
    "datetime": AttrType.TEXT,
  },
  "details": {
    "open": AttrType.BOOL,
  },
  "dialog": {
    "open": AttrType.BOOL,
  },
  "embed": {
    "height": AttrType.TEXT,
    "src": AttrType.URL,
    "type": AttrType.TEXT,
    "width": AttrType.TEXT,
  },
  "fieldset": {
    "disabled": AttrType.BOOL,
    "form": AttrType.TEXT,
    "name": AttrType.TEXT,
  },
  "form": {
    "accept-charset": AttrType.TEXT,
    "action": AttrType.URL,
    "autocomplete": AttrType.TEXT,
    "enctype": AttrType.TEXT,
    "method": AttrType.TEXT,
    "name": AttrType.TEXT,
    "novalidate": AttrType.BOOL,
    "rel": AttrType.TEXT,
    "target": AttrType.TEXT,
  },
  "html": {
    "xmlns": AttrType.URL,
  },
  "iframe": {
    "allow": AttrType.TEXT,
    "allowfullscreen": AttrType.TEXT,
    "height": AttrType.TEXT,
    "loading": AttrType.TEXT,
    "name": AttrType.TEXT,
    "referrerpolicy": AttrType.TEXT,
    "sandbox": AttrType.TEXT,
    "src": AttrType.URL,
    "srcdoc": AttrType.HTML,
    "width": AttrType.TEXT,
  },
  "img": {
    "alt": AttrType.TEXT,
    "crossorigin": AttrType.TEXT,
    "decoding": AttrType.TEXT,
    "fetchpriority": AttrType.TEXT,
    "height": AttrType.TEXT,
    "ismap": AttrType.BOOL,
    "loading": AttrType.TEXT,
    "referrerpolicy": AttrType.TEXT,
    "sizes": AttrType.TEXT,
    "src": AttrType.URL,
    "srcset": AttrType.URL,
    "usemap": AttrType.URL,
    "width": AttrType.TEXT,
  },
  "input": {
    "accept": AttrType.TEXT,
    "alt": AttrType.TEXT,
    "autocomplete": AttrType.TEXT,
    "autofocus": AttrType.BOOL,
    "capture": AttrType.TEXT,
    "checked": AttrType.BOOL,
    "dirname": AttrType.TEXT,
    "disabled": AttrType.BOOL,
    "form": AttrType.TEXT,
    "formaction": AttrType.URL,
    "formenctype": AttrType.TEXT,
    "formmethod": AttrType.TEXT,
    "formnovalidate": AttrType.BOOL,
    "formtarget": AttrType.TEXT,
    "height": AttrType.TEXT,
    "list": AttrType.TEXT,
    "max": AttrType.TEXT,
    "maxlength": AttrType.TEXT,
    "min": AttrType.TEXT,
    "minlength": AttrType.TEXT,
    "multiple": AttrType.BOOL,
    "name": AttrType.TEXT,
    "pattern": AttrType.TEXT,
    "placeholder": AttrType.TEXT,
    "readonly": AttrType.BOOL,
    "required": AttrType.BOOL,
    "size": AttrType.TEXT,
    "src": AttrType.URL,
    "step": AttrType.TEXT,
    "type": AttrType.TEXT,
    "value": AttrType.TEXT,
    "width": AttrType.TEXT,
  },
  "ins": {
    "cite": AttrType.URL,
    "datetime": AttrType.TEXT,
  },
  "label": {
    "for": AttrType.TEXT,
  },
  "li": {
    "value": AttrType.TEXT,
  },
  "link": {
    "as": AttrType.TEXT,
    "crossorigin": AttrType.TEXT,
    "fetchpriority": AttrType.TEXT,
    "href": AttrType.URL,
    "hreflang": AttrType.TEXT,
    "imagesizes": AttrType.TEXT,
    "imagesrcset": AttrType.URL,
    "integrity": AttrType.TEXT,
    "media": AttrType.TEXT,
    "referrerpolicy": AttrType.TEXT,
    "rel": AttrType.TEXT,
    "sizes": AttrType.TEXT,
    "type": AttrType.TEXT,
  },
  "map": {
    "name": AttrType.TEXT,
  },
  "meta": {
    "charset": AttrType.TEXT,
    "content": AttrType.TEXT,
    "http-equiv": AttrType.TEXT,
    "name": AttrType.TEXT,
  },
  "meter": {
    "form": AttrType.TEXT,
    "high": AttrType.TEXT,
    "low": AttrType.TEXT,
    "max": AttrType.TEXT,
    "min": AttrType.TEXT,
    "optimum": AttrType.TEXT,
    "value": AttrType.TEXT,
  },
  "object": {
    "data": AttrType.URL,
    "form": AttrType.TEXT,
    "height": AttrType.TEXT,
    "name": AttrType.TEXT,
    "type": AttrType.TEXT,
    "width": AttrType.TEXT,
  },
  "ol": {
    "reversed": AttrType.BOOL,
    "start": AttrType.TEXT,
    "type": AttrType.TEXT,
  },
  "optgroup": {
    "disabled": AttrType.BOOL,
    "label": AttrType.TEXT,
  },
  "option": {
    "disabled": AttrType.BOOL,
    "label": AttrType.TEXT,
    "selected": AttrType.BOOL,
    "value": AttrType.TEXT,
  },
  "output": {
    "for": AttrType.TEXT,
    "form": AttrType.TEXT,
    "name": AttrType.TEXT,
  },
  "progress": {
    "max": AttrType.TEXT,
    "value": AttrType.TEXT,
  },
  "q": {
    "cite": AttrType.URL,
  },
  "script": {
    "async": AttrType.BOOL,
    "crossorigin": AttrType.TEXT,
    "defer": AttrType.BOOL,
    "fetchpriority": AttrType.TEXT,
    "integrity": AttrType.TEXT,
    "nomodule": AttrType.BOOL,
    "nonce": AttrType.TEXT,
    "referrerpolicy": AttrType.TEXT,
    "src": AttrType.URL,
    "type": AttrType.TEXT,
  },
  "select": {
    "autocomplete": AttrType.TEXT,
    "autofocus": AttrType.BOOL,
    "disabled": AttrType.BOOL,
    "form": AttrType.TEXT,
    "multiple": AttrType.BOOL,
    "name": AttrType.TEXT,
    "required": AttrType.BOOL,
    "size": AttrType.TEXT,
  },
  "slot": {
    "name": AttrType.TEXT,
  },
  "source": {
    "height": AttrType.TEXT,
    "media": AttrType.TEXT,
    "sizes": AttrType.TEXT,
    "src": AttrType.URL,
    "srcset": AttrType.URL,
    "type": AttrType.TEXT,
    "width": AttrType.TEXT,
  },
  "style": {
    "blocking": AttrType.TEXT,
    "media": AttrType.TEXT,
    "nonce": AttrType.TEXT,
    "title": AttrType.TEXT,
  },
  "td": {
    "colspan": AttrType.TEXT,
    "headers": AttrType.TEXT,
    "rowspan": AttrType.TEXT,
  },
  "textarea": {
    "autocomplete": AttrType.TEXT,
    "autofocus": AttrType.BOOL,
    "cols": AttrType.TEXT,
    "dirname": AttrType.TEXT,
    "disabled": AttrType.BOOL,
    "form": AttrType.TEXT,
    "maxlength": AttrType.TEXT,
    "minlength": AttrType.TEXT,
    "name": AttrType.TEXT,
    "placeholder": AttrType.TEXT,
    "readonly": AttrType.BOOL,
    "required": AttrType.BOOL,
    "rows": AttrType.TEXT,
    "spellcheck": AttrType.TEXT,
    "wrap": AttrType.TEXT,
  },
  "th": {
    "abbr": AttrType.TEXT,
    "colspan": AttrType.TEXT,
    "headers": AttrType.TEXT,
    "rowspan": AttrType.TEXT,
    "scope": AttrType.TEXT,
  },
  "time": {
    "datetime": AttrType.TEXT,
  },
  "track": {
    "default": AttrType.BOOL,
    "kind": AttrType.TEXT,
    "label": AttrType.TEXT,
    "src": AttrType.URL,
    "srclang": AttrType.TEXT,
  },
  "video": {
    "autoplay": AttrType.BOOL,
    "controls": AttrType.BOOL,
    "crossorigin": AttrType.TEXT,
    "disableremoteplayback": AttrType.BOOL,
    "loop": AttrType.BOOL,
    "muted": AttrType.BOOL,
    "playsinline": AttrType.BOOL,
    "poster": AttrType.URL,
    "preload": AttrType.TEXT,
    "src": AttrType.URL,
    "width": AttrType.TEXT,
  },
}