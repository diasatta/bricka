from abc import ABC
import html
from contextvars import ContextVar
from uuid import uuid4
from copy import deepcopy

_with_stack_var: ContextVar[str | None] = ContextVar('_with_stack', default=None)

class Node(ABC):
  tag_name: str = "node"
  inline: bool = False

  _with_stack: dict[str | None, list[list["Node"]]] = {}

  def __init__(self, *nodes, **attrs) -> None:
    self.parent: "Node | None" = None
    self._nodes: list[Node] = []

    for node in nodes:
      self.insert(node)

    if _with_stack_var.get() is None:
      _with_stack_var.set(uuid4().hex)  
      self._with_stack[_with_stack_var.get()] = []

    if Node._with_stack.get(_with_stack_var.get(), None):
      self.collect()    

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
    
    html = f"{indent}<{self.tag_name}>"

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

class Root(Container):
  tag_name: str = "root"

  def start_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return "" 
  
  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return ""
  
  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    return self.inner_html(level, spaces, escape)
  