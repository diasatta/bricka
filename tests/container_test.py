from bricka.node import Root, Text
from foo_elements import Foo, Bar, Baz, Quux

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

class TestContainerConstructor():
  def test_passing_a_string_to_the_constructor(self):
    # Appends the string to the container
    node = Foo("Bar")
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_passing_an_integer_to_the_constructor(self):
    # Appends the integer to the container
    node = Foo(1)
    assert node.render_inline() == "<foo>1</foo>"

  def test_passing_a_float_to_the_constructor(self):
    # Appends the integer to the container
    node = Foo(1.23)
    assert node.render_inline() == "<foo>1.23</foo>"

  def test_passing_a_text_to_the_constructor(self):
    # Appends the text to the container
    node = Foo(Text("Bar"))
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_passing_a_void_to_the_constructor(self):
    # Appends the void to the container
    node = Foo(Quux())
    assert node.render_inline() == "<foo><quux></foo>"

  def test_passing_a_container_to_the_constructor(self):
    # Appends the container to the calling container
    node = Foo(Bar())
    assert node.render_inline() == "<foo><bar></bar></foo>"

  def test_passing_a_root_to_the_constructor(self):
    # Moves the container's children to the container
    root = Root()
    Bar().insert_in(root)
    Quux().insert_in(root)
    node = Foo(root)
    assert root._nodes == []
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"

  def test_passing_multiple_nodes_to_the_constructor(self):
    # Appends the nodes to the container in the specified order
    node = Foo(Bar(), Baz(), "Baz", Quux())
    assert node.render_inline() == "<foo><bar></bar><baz></baz>Baz<quux></foo>"      