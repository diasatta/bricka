from bricka.node import Root, Text
from foo_elements import Foo, Bar, Quux, Fred
import pytest

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

class TestVoidRightShifting():
  def test_right_shifting_return_value(self):
    # Is always the rightmost term
    node = Foo()
    assert node == Quux() >> node

  def test_right_shifting_a_void_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() >> Text() # type: ignore

  def test_right_shifting_a_void_to_another_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() >> Quux() # type: ignore

  def test_right_shifting_a_void_to_a_container(self):
    # Appends the void to the container
    node = Quux() >> Foo()   
    assert node.render_inline() == "<foo><quux></foo>"

  def test_right_shifting_a_void_to_a_root(self):
    # Appends the void to the container
    node = Quux() >> Root()   
    assert node.render_inline() == "<quux>"

class TestVoidLeftShifting():
  def test_left_shifting_a_string_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() << "Foo" # type: ignore

  def test_left_shifting_a_number_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() << 1 # type: ignore    

  def test_left_shifting_a_text_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() << Text() # type: ignore  

  def test_left_shifting_a_void_to_another_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() << Quux() # type: ignore   
       
  def test_left_shifting_an_container_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() << Foo() # type: ignore   
       
  def test_left_shifting_a_root_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() << Root() # type: ignore   

class TestNodeAdding():
  def test_adding_a_void_and_a_string(self):
    # Creates siblings
    left, right = Quux(), "Bar"
    node = left + right
    assert node.render_inline() == "<quux>Bar"

  def test_adding_a_void_and_an_integer(self):
    # Creates siblings
    left, right = Quux(), 1
    node = left + right
    assert node.render_inline() == "<quux>1"

  def test_adding_a_void_and_a_float(self):
    # Creates siblings
    left, right = Quux(), 1.23
    node = left + right
    assert node.render_inline() == "<quux>1.23"

  def test_adding_a_void_and_a_text(self):
    # Creates siblings
    left, right = Quux(), Text("Bar")
    node = left + right
    assert node.render_inline() == "<quux>Bar"

  def test_adding_a_void_and_a_void(self):
    # Creates siblings
    left, right = Quux(), Fred()
    node = left + right
    assert node.render_inline() == "<quux><fred>"

  def test_adding_a_void_and_a_container(self):
    # Creates siblings
    left, right = Quux(), Bar()
    node = left + right
    assert node.render_inline() == "<quux><bar></bar>"

  def test_adding_a_void_and_a_root(self):
    # Prepends the void to the root
    left, right = Quux(), Root(Bar())
    node = left + right
    assert node.render_inline() == "<quux><bar></bar>"

class TestNodeChainedAdding():
  def test_adding_multiple_tags(self):
    # Creates siblings
    node = Quux() + Fred() + Quux()
    assert node.render_inline() == "<quux><fred><quux>" 

