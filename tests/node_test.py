from bricka.node import Text, Root
from foo_elements import Foo, Bar, Baz, Quux, Fred
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
  
  def test_inserting_a_root_with_index(self):
    # Inserts the root's children at the given index
    root = Root(Quux(), Fred())
    node = Foo(Bar(), Baz())
    node.insert(root, 1)
    assert node.render_inline() == "<foo><bar></bar><quux><fred><baz></baz></foo>"

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

  def test_appending_a_node_again_without_freeing_it(self):
    # Raises an exception
    with Bar() as bar:
      baz = Baz()

    assert bar.render_inline() == "<bar><baz></baz></bar>"   

    with Foo() as node:
      # baz.free()
      with pytest.raises(Exception):
        baz.collect()

    # assert bar.render_inline() == "<bar></bar>"    
    # assert node.render_inline() == "<foo><baz></baz></foo>"    

  # def test_appending_nodes_in_concurrent_threads(self):
  # # TODO
  #   pass

class TestNodeIterator():
  def test_interating_an_element_with_for(self):
    # Iterates on the element's children
    node = Foo(Bar(), Baz())
    i = 0
    for n in node:
      assert n == node._nodes[i]
      i += 1 

class TestNodeRightShifting():
  def test_right_shifting_return_value(self):
    # Is always the rightmost term
    node = Foo()
    assert node == Bar() >> node

  def test_right_shifting_an_element_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo() >> Text("") # type: ignore    

  def test_right_shifting_an_element_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Foo() >> Quux() # type: ignore

  def test_right_shifting_an_element_to_a_container(self):
    # Appends the left element to the container
    node = Bar() >> Foo()   
    assert node.render_inline() == "<foo><bar></bar></foo>"

  def test_right_shifting_an_element_to_a_root(self):
    # Appends the left element to the root
    node = Root(Foo())
    Bar() >> node # type: ignore
    assert node.render_inline() == "<foo></foo><bar></bar>"

  def test_right_shifting_a_string_to_a_container(self):
    # Converts the string to Text and appends it
    node = "Bar" >> Foo()   
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_right_shifting_a_number_to_a_container(self):
    # Converts the number to Text and appends it
    node = 1 >> Foo()   
    assert node.render_inline() == "<foo>1</foo>"

  def test_right_shifting_a_float_to_a_container(self):
    # Converts the float to Text and appends it
    node = 1.23 >> Foo()   
    assert node.render_inline() == "<foo>1.23</foo>"

  def test_right_shifting_a_boolean_to_a_container(self):
    # Converts the boolean to Text and appends it
    node = True >> Foo()         
    assert node.render_inline() == "<foo>True</foo>"

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

class TestNodeLeftShifting():
  def test_left_shifting_return_value(self):
    # Is always the rightmost term
    node = Foo()
    assert node == Bar() << node

  def test_left_shifting_an_element_to_a_text(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Text("") << Foo() # type: ignore    

  def test_left_shifting_an_element_to_a_void(self):
    # Raises a TypeError
    with pytest.raises(TypeError):
      Quux() << Foo() # type: ignore

  def test_left_shifting_an_element_to_a_container(self):
    # Appends the left element to the container
    node = Foo()
    node << Bar() # type: ignore
    assert node.render_inline() == "<foo><bar></bar></foo>"

  def test_left_shifting_an_element_to_a_root(self):
    # Appends the left element to the root
    node = Root(Foo())
    node << Bar() # type: ignore
    assert node.render_inline() == "<foo></foo><bar></bar>"

  def test_left_shifting_a_string_to_a_container(self):
    # Converts the string to Text and appends it
    node = Foo()
    node << "Bar" # type: ignore
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_left_shifting_a_number_to_a_container(self):
    # Converts the number to Text and appends it
    node = Foo()   
    node << 1 # type: ignore
    assert node.render_inline() == "<foo>1</foo>"

  def test_left_shifting_a_float_to_a_container(self):
    # Converts the float to Text and appends it
    node = Foo()   
    node << 1.23 # type: ignore
    assert node.render_inline() == "<foo>1.23</foo>"

  def test_left_shifting_a_boolean_to_a_container(self):
    # Converts the boolean to Text and appends it
    node = Foo()         
    node << True # type: ignore
    assert node.render_inline() == "<foo>True</foo>"

  def test_left_shifting_a_none_to_a_container(self):
    # Converts the None to empty Text and appends it
    node = Foo()   
    node << None # type: ignore
    assert node.render_inline() == "<foo></foo>"
  
  def test_chained_left_shifting_with_containers(self):
    # Creates a hierarchy of nodes
    node = Foo()
    node << Bar() << Baz() # type: ignore
    assert node.render_inline() == "<foo><bar><baz></baz></bar></foo>"   

  def test_chained_left_shifting_with_text(self):
    # Creates a hierarchy of nodes
    node = Foo()
    node << Bar() << "Baz"
    assert node.render_inline() == "<foo><bar>Baz</bar></foo>"  

  def test_chained_left_shifting_with_void(self):
    # Creates a hierarchy of nodes
    node = Foo()
    node << Bar() << Quux()
    assert node.render_inline() == "<foo><bar><quux></bar></foo>"    

  # def test_left_shifting_using_parenthesis(self):
  #   # Is not associative
  #   node = (Quux() << Bar()) << Foo()
  #   assert node.render_inline() == "<foo><bar><quux></bar></foo>" 

  #   node = Quux() << (Bar() << Foo())
  #   assert node.render_inline() == "<foo><bar></bar><quux></foo>"    

class TestNodeChildrenGetting():
  def test_getting_child_at_index(self):
    # Returns the child at the given index, otherwise None
    node = Foo(Bar(), Baz(), Quux())
    assert node.at(1).render_inline() == "<baz></baz>" # type: ignore
    assert node.at(3) == None # type: ignore

  def test_getting_first_child(self):
    # Returns the first child
    node = Foo(Bar(), Baz(), Quux())
    assert node.first().render_inline() == "<bar></bar>" # type: ignore

  def test_getting_last_child(self):
    # Returns the last child
    node = Foo(Bar(), Baz(), Quux())
    assert node.last().render_inline() == "<quux>" # type: ignore

class TestNodeChildrenTaking():
  def test_taking_child_at_index(self):
    # Returns the child at the given index and removes it from the parent node's children
    node = Foo(Bar(), Baz(), Quux())
    assert node.take_at(1).render_inline() == "<baz></baz>" # type: ignore
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"
    assert node.take_at(3) == None

  def test_taking_first_child(self):
    # Returns the first child and removes it from the parent node's children
    node = Foo(Bar(), Baz(), Quux())
    assert node.take_first().render_inline() == "<bar></bar>" # type: ignore
    assert node.render_inline() == "<foo><baz></baz><quux></foo>"

  def test_taking_last_child(self):
    # Returns the last child and removes it from the parent node's children
    node = Foo(Bar(), Baz(), Quux())
    assert node.take_last().render_inline() == "<quux>" # type: ignore
    assert node.render_inline() == "<foo><bar></bar><baz></baz></foo>"

class TestNodeAdding():
  def test_adding_return_value(self):
    # Is always a root
    left, right = "Foo", Text("Bar")
    node = left + right
    assert type(node) == Root

class TestNodeChainedAdding():
  def test_adding_multiple_nodes(self):
    # Creates siblings
    node = Foo() + Text("Bar") + Quux() + "Baz"
    assert node.render_inline() == "<foo></foo>Bar<quux>Baz"     

