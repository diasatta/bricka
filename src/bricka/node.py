from abc import ABC
import html

class Node(ABC):
  tag_name: str = "node"
  inline: bool = False

  def __init__(self, *nodes, **attrs) -> None:
    self.parent: "Node | None" = None
    self._nodes: list[Node] = []

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
  
class Element(Node): 
  tag_name: str = "element"

class Void(Element):
  tag_name: str = "void"

  def __init__(self, **attrs) -> None:
    super().__init__(**attrs)

  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return ""  
  
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
  