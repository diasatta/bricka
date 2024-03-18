from bricka.node import Root, Text
from foo_elements import Foo, Bar, Baz, Quux
import pytest

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

class TestContainerRightShifting():
  def test_right_shifting_return_value(self):
    # Is always the rightmost term
    node = Foo()
    assert node == Bar() >> node

  def test_right_shifting_a_container_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo() >> Text("") # type: ignore    

  def test_right_shifting_a_container_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo() >> Quux() # type: ignore

  def test_right_shifting_a_container_to_a_container(self):
    # Appends the left container to the right container
    node = Bar() >> Foo()   
    assert node.render_inline() == "<foo><bar></bar></foo>"

  def test_right_shifting_a_container_to_a_root(self):
    # Appends the left container to the container
    node = Bar() >> Root()  
    assert node.render_inline() == "<bar></bar>"

  def test_right_shifting_a_none_to_a_container(self):
    # Converts the None to empty Text and appends it
    node = None >> Foo()   
    assert node.render_inline() == "<foo></foo>"
  
  def test_chained_right_shifting_with_containers(self):
    # Creates a hierarchy of nodes
    node = Baz() >> Bar() >> Foo()
    assert node.render_inline() == "<foo><bar><baz></baz></bar></foo>"   

  def test_chained_right_shifting_with_text(self):
    # Creates a hierarchy of nodes
    node = "Baz" >> Bar() >> Foo()
    assert node.render_inline() == "<foo><bar>Baz</bar></foo>"  

  def test_chained_right_shifting_with_void(self):
    # Creates a hierarchy of nodes
    node = Quux() >> Bar() >> Foo()
    assert node.render_inline() == "<foo><bar><quux></bar></foo>"    

  def test_right_shifting_using_parenthesis(self):
    # Is not associative
    node = (Quux() >> Bar()) >> Foo()
    assert node.render_inline() == "<foo><bar><quux></bar></foo>" 

    node = Quux() >> (Bar() >> Foo())
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"    

class TestContainerLeftShifting():
  def test_left_shifting_return_value_with_non_root(self):
    # Is the rightmost
    node = Bar()
    assert node == Foo() << node

  def test_left_shifting_return_value_with_root(self):
    # Is the leftmost term
    node = Foo()
    assert node == node << Root(Quux())

  def test_left_shifting_a_string_to_a_container(self):
    # Converts the string to Text and appends it
    node = Foo()
    node << "Bar" # type: ignore
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_left_shifting_a_number_to_an_container(self):
    # Converts the number to Text and appends it
    node = Foo()   
    node << 1 # type: ignore
    assert node.render_inline() == "<foo>1</foo>"

  def test_left_shifting_a_float_to_a_container(self):
    # Converts the float to Text and appends it
    node = Foo()   
    node << 1.23 # type: ignore
    assert node.render_inline() == "<foo>1.23</foo>"

  # def test_left_shifting_a_boolean_to_a_container(self):
  #   # Converts the boolean to Text and appends it
  #   node = Foo()
  #   node << True
  #   assert node.render_inline() == "<foo>True</foo>"

  def test_left_shifting_a_none_to_a_container(self):
    # Converts the None to empty Text and appends it
    node = Foo()   
    node << None # type: ignore
    assert node.render_inline() == "<foo></foo>"

  def test_left_shifting_a_text_to_a_container(self):
    # Appends the Text to the element
    node = Foo()   
    node << Text("Bar") # type: ignore
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_left_shifting_a_tag_to_a_container(self):
    # Appends the right element to the left element
    node = Foo()
    node << Quux() # type: ignore
    assert node.render_inline() == "<foo><quux></foo>"

  def test_left_shifting_an_element_to_a_container(self):
    # Appends the right element to the left element
    node = Foo()
    node << Bar() # type: ignore
    assert node.render_inline() == "<foo><bar></bar></foo>"

  def test_left_shifting_a_root_to_a_container(self):
    # Appends the root's children to the container
    # And empties the container
    node = Foo()
    container = Root()
    bar = container << Bar()
    node2 = node << container
    assert node == node2
    assert bar in node._nodes
    assert container._nodes == []
    assert node.render_inline() == "<foo><bar></bar></foo>"

  def test_chained_left_shifting_with_containers(self):
    # Creates a hierarchy of nodes
    node = Foo()
    node << Bar() << Baz() # type: ignore
    assert node.render_inline() == "<foo><bar><baz></baz></bar></foo>"   

  def test_chained_left_shifting_with_text(self):
    # Creates a hierarchy of nodes
    node = Foo()
    node << Bar() << "Baz" # type: ignore
    assert node.render_inline() == "<foo><bar>Baz</bar></foo>"  

  def test_chained_left_shifting_with_tag(self):
    # Creates a hierarchy of nodes
    node = Foo()
    node << Bar() << Quux() # type: ignore
    assert node.render_inline() == "<foo><bar><quux></bar></foo>"  

  def test_chained_left_shifting_with_root(self):
    # Appends the rightmost term as a sibling of the container children
    node = Foo()
    root = Root()
    root << Bar() # type: ignore
    node << root << Quux() # type: ignore
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"    

  def test_left_shifting_using_parenthesis(self):
    # Is not associative and may raise an exception
    node = Foo()
    (node << Bar()) << Quux() # type: ignore
    assert node.render_inline() == "<foo><bar><quux></bar></foo>" 

    node = Foo()
    with pytest.raises(Exception):
      node << (Bar() << Quux()) # type: ignore

class TestContainerAdding():
  def test_adding_a_container_and_a_string(self):
    # Creates siblings
    left, right = Foo(), "Bar"
    node = left + right
    assert node.render_inline() == "<foo></foo>Bar"

  def test_adding_a_container_and_an_integer(self):
    # Creates siblings
    left, right = Foo(), 1
    node = left + right
    assert node.render_inline() == "<foo></foo>1"

  def test_adding_a_container_and_a_float(self):
    # Creates siblings
    left, right = Foo(), 1.23
    node = left + right
    assert node.render_inline() == "<foo></foo>1.23"

  def test_adding_a_container_and_a_text(self):
    # Creates siblings
    left, right = Foo(), Text("Bar")
    node = left + right
    assert node.render_inline() == "<foo></foo>Bar"

  def test_adding_a_container_and_a_void(self):
    # Creates siblings
    left, right = Foo(), Quux()
    node = left + right
    assert node.render_inline() == "<foo></foo><quux>"

  def test_adding_a_container_and_a_container(self):
    # Creates siblings
    left, right = Foo(), Bar()
    node = left + right
    assert node.render_inline() == "<foo></foo><bar></bar>"

  def test_adding_a_container_and_a_root(self):
    # Prepends the container to the root
    left, right = Foo(), Root(Bar())
    node = left + right
    assert node.render_inline() == "<foo></foo><bar></bar>"

class TestContainerChainedAdding():
  def test_adding_multiple_container(self):
    # Creates siblings
    node = Foo() + Bar() + Baz()
    assert node.render_inline() == "<foo></foo><bar></bar><baz></baz>"   

