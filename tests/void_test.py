from foo_elements import Quux

class TestVoidElementRendering():
  def test_rendering_a_void_element_using_render(self):
    # Renders a HTML opening tag with no closing tag
    node = Quux()
    assert node.render() == "<quux>"

  def test_rendering_a_void_element_using_str(self):
    # Is equivalent to calling render()
    node = Quux()
    assert str(node) == "<quux>"

  def test_rendering_a_void_element_with_indent_level(self):
    # Renders the element with an indent depending on the level
    node = Quux()
    level = 0
    assert node.render(level=level) == "<quux>"

    level = 1
    assert node.render(level=level, spaces=2) == level * 2 * " " + "<quux>"

    level = 2
    assert node.render(level=level, spaces=2) == level * 2 * " " + "<quux>"
