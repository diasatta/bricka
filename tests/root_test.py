from bricka.node import Root, Text
from foo_elements import Foo, Bar, Baz, Quux
import pytest

class TestRootRendering():
  def test_rendering_an_empty_root(self):
    # Renders an empty string
    node = Root()
    assert node.render() == ""

  def test_rendering_start_tag(self):
    # Renders an empty string
    node = Root()
    assert node.start_tag() == ""

  def test_rendering_end_tag(self):
    # Renders an empty string
    node = Root()
    assert node.end_tag() == ""

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

class TestRootRightShifting():
  def test_right_shifting_return_value(self):
    # Is always the rightmost term
    node = Root()
    assert node == Bar() >> node

  def test_right_shifting_a_root_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo() >> Text("") #type: ignore    

  def test_right_shifting_a_root_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo() >> Quux() #type: ignore

  def test_right_shifting_a_root_to_a_container(self):
    # Appends the left container to the right container

    node = Root(Bar()) >> Foo()   
    assert node.render_inline() == "<foo><bar></bar></foo>"

  def test_right_shifting_a_root_to_a_root(self):
    # Appends the left root to the right one
    node = Root(Bar()) >> Root()  
    assert node.render_inline() == "<bar></bar>"

  def test_right_shifting_a_none_to_a_root(self):
    # Converts the None to empty Text and appends it
    node = None >> Root()   
    assert node.render_inline() == ""
  
  def test_chained_right_shifting_with_root(self):
    # Creates siblings
    node = Root(Baz()) >> Root(Bar()) >> Root(Foo())
    assert node.render_inline() == "<foo></foo><bar></bar><baz></baz>"   

  def test_chained_right_shifting_with_text(self):
    # Creates siblings
    node = "Baz" >> Root(Bar()) >> Root(Foo())
    assert node.render_inline() == "<foo></foo><bar></bar>Baz"  

  def test_chained_right_shifting_with_void(self):
    # Creates a hierarchy of nodes
    node = Quux() >> Root(Bar()) >> Root(Foo())
    assert node.render_inline() == "<foo></foo><bar></bar><quux>"    

  def test_right_shifting_roots_only_using_parenthesis(self):
    # Is associative!
    node = (Root(Quux()) >> Root(Bar())) >> Root(Foo())
    assert node.render_inline() == "<foo></foo><bar></bar><quux>" 

    node = Root(Quux()) >> (Root(Bar()) >> Root(Foo()))
    assert node.render_inline() == "<foo></foo><bar></bar><quux>"    

class TestRootLeftShifting():
  def test_left_shifting_return_value(self):
    # Is the rightmost term
    node = Bar()
    assert node == Root() << node

  def test_left_shifting_return_value_with_root(self):
    # Is the rightmost term
    node = Root()
    assert node == node << Root()

  def test_left_shifting_a_string_to_a_root(self):
    # Converts the string to Text and appends it
    node = Root()
    node << "Bar" # type: ignore
    assert node.render_inline() == "Bar"

  def test_left_shifting_a_number_to_a_root(self):
    # Converts the number to Text and appends it
    node = Root()   
    node << 1 # type: ignore
    assert node.render_inline() == "1"

  def test_left_shifting_a_float_to_a_root(self):
    # Converts the float to Text and appends it
    node = Root()   
    node << 1.23 # type: ignore
    assert node.render_inline() == "1.23"

  # def test_left_shifting_a_boolean_to_a_root(self):
  #   # Converts the boolean to Text and appends it
  #   node = Root()
  #   node << True
  #   assert node.render_inline() == "True"

  # def test_left_shifting_a_none_to_a_root(self):
  #   # Converts the None to empty Text and appends it
  #   node = Root()   
  #   node << None
  #   assert node.render_inline() == ""

  def test_left_shifting_a_text_to_a_root(self):
    # Appends the Text to the element
    node = Root()   
    node << Text("Bar") # type: ignore
    assert node.render_inline() == "Bar"

  def test_left_shifting_a_void_to_a_root(self):
    # Appends the right void to the root
    node = Root()
    node << Quux() # type: ignore
    assert node.render_inline() == "<quux>"

  def test_left_shifting_a_container_to_a_root(self):
    # Appends the container to the root
    node = Root()
    node << Foo() # type: ignore
    assert node.render_inline() == "<foo></foo>"

  def test_left_shifting_a_root_to_another_root(self):
    # Appends the right root's children to the left root
    # And empties the right root
    left = Root()
    right = Root()
    bar = right << Bar()
    node = left << right
    assert node == left
    assert bar in node._nodes
    assert right._nodes == []
    assert node.render_inline() == "<bar></bar>"
