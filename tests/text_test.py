from bricka.node import Text, Root
from foo_elements import Foo, Bar, Quux
import pytest

class TestTextRendering():
  def test_rendering_with_alphabetic_characters(self):
    # Renders the text as is without any HTML tag
    node = Text("Bar")
    assert node.render() == "Bar"
 
  def test_rendering_with_html_special_characters(self):
    # Renders the text with HTML escaping
    node = Text("<script>foo()</script>")
    assert node.render() == "&lt;script&gt;foo()&lt;/script&gt;"

  def test_rendering_with_new_line_characters(self):
    # Renders the text as is, including the new line characters
    node = Text("Foo\nBar")
    assert node.render() == "Foo\nBar"

class TestTextRightShifting():
  def test_right_shifting_a_string_to_a_text(self):
    # Appends the string to the Text
    node = "Bar" >> Text("Foo")
    assert node.text == "FooBar"
    assert node.render_inline() == "FooBar"

  def test_right_shifting_a_string_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      "Foo" >> Quux() # type: ignore  

  def test_right_shifting_a_string_to_a_container(self):
    # Converts the string to Text and appends it
    node = "Bar" >> Foo()   
    assert node.render_inline() == "<foo>Bar</foo>"  

  def test_right_shifting_a_number_to_a_text(self):
    # Appends the number to the Text
    node = 1 >> Text("Foo")
    assert node.render_inline() == "Foo1"

  def test_right_shifting_a_number_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      1 >> Quux() # type: ignore     

  def test_right_shifting_a_number_to_a_container(self):
    # Converts the number to Text and appends it
    node = 1 >> Foo()   
    assert node.render_inline() == "<foo>1</foo>"  

  def test_right_shifting_a_float_to_a_text(self):
    # Appends the float to the Text
    node = 1.23 >> Text("Foo")
    assert node.render_inline() == "Foo1.23"

  def test_right_shifting_a_float_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      1.23 >> Quux() # type: ignore

  def test_right_shifting_a_float_to_a_container(self):
    # Converts the float to Text and appends it
    node = 1.23 >> Foo()   
    assert node.render_inline() == "<foo>1.23</foo>"  

  def test_right_shifting_a_boolean_to_a_text(self):
    # Appends the boolean to the Text
    node = True >> Text("Foo")
    assert node.render_inline() == "FooTrue"

  def test_right_shifting_a_boolean_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      True >> Quux() # type: ignore

  def test_right_shifting_a_boolean_to_a_container(self):
    # Converts the boolean to Text and appends it
    node = True >> Foo()         
    assert node.render_inline() == "<foo>True</foo>"  

  def test_right_shifting_a_text_to_a_text(self):
    # Appends the left Text's string to the right Text's string
    # And sets the left Text's string to empty
    bar = Text("Bar") 
    node = bar >> Text("Foo") 
    assert bar.render_inline() == ""
    assert node.render_inline() == "FooBar"

  def test_right_shifting_a_text_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Text("Foo")  >> Quux() # type: ignore

  def test_right_shifting_a_text_to_a_container(self):
    # Appends the text to the element
    node = Text("Bar") >> Foo() 
    assert node.render_inline() == "<foo>Bar</foo>"   

  def test_right_shifting_a_text_to_a_root(self):
    # Appends the text to the container
    node = Text("Bar") >> Root() 
    assert node.render_inline() == "Bar"    

class TestTextLeftShifting():
  def test_left_shifting_a_string_to_a_text(self):
    # Appends the string to the Text
    node = Text("Foo")
    node << "Bar" # type: ignore
    assert node.text == "FooBar"
    assert node.render_inline() == "FooBar"

  def test_left_shifting_a_number_to_a_text(self):
    # Appends the number to the Text
    node = Text("Foo")
    node << 1 # type: ignore
    assert node.render_inline() == "Foo1"

  def test_left_shifting_a_float_to_a_text(self):
    # Appends the float to the Text
    node = Text("Foo")
    node << 1.23 # type: ignore
    assert node.render_inline() == "Foo1.23"

  def test_left_shifting_a_boolean_to_a_text(self):
    # Appends the boolean to the Text
    node = Text("Foo")
    node << True # type: ignore
    assert node.render_inline() == "FooTrue"

  def test_left_shifting_a_text_to_a_text(self):
    # Appends the right Text's string to the left Text's string
    # And sets the right Text's string to empty
    node = Text("Foo")
    bar = Text("Bar")
    node << bar # type: ignore
    assert bar.render_inline() == ""
    assert node.render_inline() == "FooBar"

  def test_left_shifting_a_tag_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Text("Foo") << Quux() # type: ignore

  def test_left_shifting_an_element_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Text("Foo") << Foo() # type: ignore

  def test_left_shifting_a_root_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Text("Foo") << Root() # type: ignore

class TestTextAdding():
  def test_adding_a_text_and_a_string(self):
    # Creates text siblings
    left, right = Text("Foo"), "Bar"
    node = left + right
    assert node.render_inline() == "FooBar"

  def test_adding_a_text_and_an_integer(self):
    # Creates text siblings
    left, right = Text("Foo"), 1
    node = left + right
    assert node.render_inline() == "Foo1"

  def test_adding_a_text_and_a_float(self):
    # Creates text siblings
    left, right = Text("Foo"), 1.23
    node = left + right
    assert node.render_inline() == "Foo1.23"

  def test_adding_a_text_and_a_text(self):
    # Creates text siblings
    left, right = Text("Foo"), Text("Bar")
    node = left + right
    assert node.render_inline() == "FooBar"

  def test_adding_a_text_and_a_tag(self):
    # Creates siblings
    left, right = Text("Foo"), Quux()
    node = left + right
    assert node.render_inline() == "Foo<quux>"

  def test_adding_a_text_and_an_element(self):
    # Creates siblings
    left, right = Text("Foo"), Bar()
    node = left + right
    assert node.render_inline() == "Foo<bar></bar>"

  def test_adding_a_text_and_a_root(self):
    # Prepends the text to the root
    left, right = Text("Foo"), Root(Bar())
    node = left + right
    assert node.render_inline() == "Foo<bar></bar>"

class TestTextChainedAdding():
  def test_adding_text_and_multiple_strings(self):
    # Creates a text for each string 
    node = Text("Foo") + "Bar" + "Baz"
    assert len(node._nodes) == 3
    assert node.render_inline() == "FooBarBaz" 

  def test_adding_multiple_strings_and_text(self):
    # Groups the strings to a single text
    node = "Foo" + "Bar" + Text("Baz")
    assert len(node._nodes) == 2
    assert node.render_inline() == "FooBarBaz" 

  def test_adding_text_and_multiple_numbers(self):
    # Creates a text for each number
    node = Text("Foo") + 1 + 2
    assert len(node._nodes) == 3
    assert node.render_inline() == "Foo12" 

  def test_adding_multiple_numbers_and_text(self):
    # Adds the numbers then creates a text
    node = 1 + 2 + Text("Foo")
    assert len(node._nodes) == 2
    assert node.render_inline() == "3Foo" 
    