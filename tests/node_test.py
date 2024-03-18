from bricka.node import Text, Root
from foo_elements import Foo, Bar, Baz, Quux
import pytest

class TestNodeInsertInParent():
  def test_inserting_return_value(self):
    # Is always the parent
    node = Foo()
    void = Quux()
    assert node == void.insert_in(node)   

  def test_inserting_with_a_zero_index(self):
    # Prepends the node
    node = Foo()
    node.insert(Bar())
    Quux().insert_in(node, 0)

    assert node.render_inline() == "<foo><quux><bar></bar></foo>"

  def test_inserting_with_a_none_index(self):
    # Appends the node
    node = Foo()
    node.insert(Bar())
    Quux().insert_in(node, None)

    assert node.render_inline() == "<foo><bar></bar><quux></foo>"

  def test_inserting_with_a_positive_index(self):
    # Inserts the node in the middle
    node = Foo()
    node.insert(Bar())
    node.insert(Baz())
    Quux().insert_in(node, 1)

    assert node.render_inline() == "<foo><bar></bar><quux><baz></baz></foo>"

  def test_inserting_with_an_invalid_positive_index(self):
    # Appends the node
    node = Foo()
    node.insert(Bar())
    Quux().insert_in(node, 10)

    assert node.render_inline() == "<foo><bar></bar><quux></foo>"

  def test_inserting_with_a_reverse_index(self):
     # Inserts the node in the middle counting from the end
    node = Foo()
    node.insert(Bar())
    node.insert(Baz())
    Quux().insert_in(node, -1)

    assert node.render_inline() == "<foo><bar></bar><quux><baz></baz></foo>"

  def test_inserting_with_an_invalid_reverse_index(self):
     # Prepends the node
    node = Foo()
    node.insert(Bar())
    node.insert(Baz())
    Quux().insert_in(node, -10)

    assert node.render_inline() == "<foo><quux><bar></bar><baz></baz></foo>"

  def test_inserting_again_in_another_element(self):
    # Raises an exception
    node_a = Foo()
    node_b = Bar()
    void = Quux()
    void.insert_in(node_a)

    with pytest.raises(Exception):
      void.insert_in(node_b)

  def test_inserting_again_in_the_same_element(self):
    # Raises an exception
    node_a = Foo()
    void = Quux()
    void.insert_in(node_a)

    with pytest.raises(Exception):
      void.insert_in(node_a)

  def test_reinserting_from_a_root_in_a_container(self):
    # Raises an exception
    node = Foo()
    root = Root()
    void = Quux()
    void.insert_in(root)
    with pytest.raises(Exception):
      void.insert_in(node)

  def test_inserting_in_a_void(self):
    # Raises a TypeError exception
    node = Quux()
    void = Quux()
    with pytest.raises(TypeError):
      void.insert_in(node)

  def test_inserting_in_a_text(self): # TODO: Allow?!
    # Raises a TypeError exception
    node = Text("")
    void = Quux()
    with pytest.raises(TypeError):
      void.insert_in(node)

class TestNodeInsertAChild():
  def test_insert_return_value(self):
    # Is always the inserted child
    node = Foo()
    void = Quux()
    assert void == node.insert(void)

  def test_inserting_from_a_void(self):
    # Raises a TypeError
    node = Quux()
    with pytest.raises(TypeError):
      node.insert(Foo())

  def test_inserting_from_a_text(self):
    # Raises a TypeError
    node = Text()
    with pytest.raises(TypeError):
      node.insert(Foo())

  def test_inserting_from_an_element(self):
    # Is equivalent to calling insert_in to the element
    node = Foo()
    node.insert(Quux())

    assert node.render_inline() == "<foo><quux></foo>"

  def test_inserting_a_string(self):
    # Internally converts the string to a Text
    node = Foo()
    text = node.insert("Bar")
    assert type(text) == Text
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_inserting_an_integer(self):
    # Internally converts the integer to a Text
    node = Foo()
    text = node.insert(1)
    assert type(text) == Text
    assert node.render_inline() == "<foo>1</foo>"

  def test_inserting_a_float(self):
    # Internally converts the float to a Text
    node = Foo()
    text = node.insert(1.23)
    assert type(text) == Text
    assert node.render_inline() == "<foo>1.23</foo>"

  def test_inserting_a_boolean(self):
    # Internally converts the boolean to a Text
    node = Foo()
    text = node.insert(True)
    assert type(text) == Text
    assert node.render_inline() == "<foo>True</foo>"

  def test_inserting_a_none(self):
    # Internally converts the None to empty string
    node = Foo()
    text = node.insert(None)
    assert type(text) == Text
    assert node.render_inline() == "<foo></foo>"

  def test_inserting_with_index(self):
    # Inserts the children at the given index
    node = Foo()
    node.insert(Bar())
    node.insert(Baz())
    node.insert(Quux(), 1)
    assert node.render_inline() == "<foo><bar></bar><quux><baz></baz></foo>"

class TestNodePrependToParent():
  def test_prepend_to_return_value(self):
    # Is always the parent
    node = Foo()
    assert node == Quux().prepend_to(node)

  def test_prepending_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo().prepend_to(Quux())

  def test_prepending_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo().prepend_to(Text())

  def test_prepending_to_an_element(self):
    # Prepends the children to the element
    node = Bar().insert_in(Foo())
    Quux().prepend_to(node)
    assert node.render_inline() == "<foo><quux><bar></bar></foo>"

  def test_prepending_a_text_to_an_element(self):
    # Is possible using a Text object, not directly a string
    node = Bar().insert_in(Foo())
    Text("Baz").prepend_to(node)
    assert node.render_inline() == "<foo>Baz<bar></bar></foo>"

class TestNodePrependAChild():
  def test_prepend_return_value(self):
    # Is always the appended child
    node = Foo()
    void = Quux()
    assert void == node.prepend(void)

  def test_prepending_from_a_void(self):
    # Raises a TypeError
    node = Quux()
    with pytest.raises(TypeError):
      node.prepend(Foo())

  def test_prepending_from_a_text(self):
    # Raises a TypeError
    node = Text()
    with pytest.raises(TypeError):
      node.prepend(Foo())    

  def test_prepending_a_text_from_an_element(self):
    # Is possible using either a Text object or a string
    node = Foo()
    node.prepend("Bar")
    node.prepend(Text("Baz"))
    assert node.render_inline() == "<foo>BazBar</foo>"    

class TestNodeAppendToParent():
  def test_append_to_return_value(self):
    # Is always the parent
    node = Foo()
    assert node == Quux().append_to(node)

  def test_appending_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo().append_to(Quux())

  def test_appending_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo().append_to(Text())

  def test_appending_to_an_element(self):
    # Is equivalent to calling insert_in with index None
    node = Quux().append_to(Foo())
    assert node.render_inline() == "<foo><quux></foo>"

  def test_appending_a_text_to_an_element(self):
    # Is possible using a Text object, not directly a string
    node = Text("Bar").append_to(Foo())
    assert node.render_inline() == "<foo>Bar</foo>"

class TestNodeAppendAChild():
  def test_append_return_value(self):
    # Is always the appended child
    node = Foo()
    void = Quux()
    assert void == node.append(void)

  def test_appending_from_a_void(self):
    # Raises a TypeError
    node = Quux()
    with pytest.raises(TypeError):
      node.append(Foo())

  def test_appending_from_a_text(self):
    # Raises a TypeError
    node = Text()
    with pytest.raises(TypeError):
      node.append(Foo())

  def test_appending_a_text_from_an_element(self):
    # Is possible using either a Text object or a string
    node = Foo()
    node.append("Bar")
    node.append(Text("Baz"))
    assert node.render_inline() == "<foo>BarBaz</foo>"        

  def test_append_from_an_element(self):
    # Appends the children to the element
    node = Foo()
    node.append(Bar())
    node.append(Quux())
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"

  def test_appending_a_string(self):
    # Internally converts the string to a Text
    node = Foo()
    text = node.append("Bar")
    assert type(text) == Text
    assert node.render_inline() == "<foo>Bar</foo>"

class TestNodeWithContext():
  # def test_creating_a_node_outside_of_with_context(self):
  #   # Does not append to the stack
  #   node = Foo()
  #   assert node._with_stack == []

  def test_appending_nodes_using_a_one_level_with_context(self):
    # Appends all the nodes created within the context
    node = Foo()
    with node:
      bar = Bar()
      quux = Quux()
      assert list(node._with_stack.values())[0] == [[bar, quux]]

    assert list(node._with_stack.values())[0] == []
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"
 
  def test_appending_nodes_using_a_two_level_with_context(self):
    # Recursively appends all the nodes created within the context
    with Foo() as node:
      with Bar() as bar:
        baz = Baz()
        quux = Quux()
      
        assert list(node._with_stack.values())[0] == [[bar], [baz, quux]]
    
    assert node.render_inline() == "<foo><bar><baz></baz><quux></bar></foo>"

  def test_appending_using_with_context_and_manual_appending(self):
    # Appends only the nodes that don't have a parent
    with Foo() as node:
      Bar().append(Quux())

    assert node.render_inline() == "<foo><bar><quux></bar></foo>"

  def test_appending_a_node_created_outside_of_with_context(self):
    # Is possible using collect() method
    bar = Bar()
    with Foo() as node:
      bar.collect()

    assert node.render_inline() == "<foo><bar></bar></foo>"  

  def test_appending_a_node_already_inserted_in_another_element(self):
    # Is possible using collect() after detaching it from its parent
    with Bar() as bar:
      baz = Baz()

    assert bar.render_inline() == "<bar><baz></baz></bar>"   

    with Foo() as node:
      baz.free()
      baz.collect()

    assert bar.render_inline() == "<bar></bar>"    
    assert node.render_inline() == "<foo><baz></baz></foo>"    

  # def test_appending_nodes_in_concurrent_threads(self):
  # # TODO
  #   pass
