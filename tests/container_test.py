from foo_elements import Foo

class TestContainerRendering():
  def test_rendering_a_container_using_render(self):
    # Renders a HTML container with an opening and a closing tag
    # The container is rendred inline by default if it has no children
    node = Foo()
    assert node.render() == "<foo></foo>"

  def test_rendering_a_container_using_str(self):
    # Is equivalent to calling render()
    node = Foo()
    assert str(node) == "<foo></foo>"