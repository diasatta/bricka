from bricka.node import Root
from foo_elements import Foo, Bar

class TestRootRendering():
  def test_rendering_an_empty_root(self):
    # Renders an empty string
    node = Root()
    assert node.render() == ""

  def test_default_rendering_of_a_root_with_children(self):
    # Renders only the children as siblings
    container = Root()
    container.insert(Foo())
    container.insert(Bar())
    
    assert container.render() == f'''\
<foo></foo>
<bar></bar>'''  
    
  def test_forcing_rendering_of_a_root_inline(self):
  # Renders only the children inline as siblings
    root = Root()
    root.insert(Foo())
    root.insert(Bar())
    
    assert root.render_inline() == "<foo></foo><bar></bar>"  