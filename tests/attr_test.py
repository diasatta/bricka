from foo_elements import Foo
import pytest

class TestAttributeNaming():
  def test_creating_attribute_with_letters_only(self):
    # Does not alter the resulting attribute name
    assert Foo.attr_html_name("bar") == "bar"

  def test_creating_attribute_with_letters_and_underscores(self):
    # Replaces the underscores with dashes
    assert Foo.attr_html_name("bar_baz") == "bar-baz"

  def test_creating_attribute_with_alphanumeric(self):
    # Does not alter the resulting attribute name
    assert Foo.attr_html_name("bar1") == "bar1"  

  def test_creating_attribute_with_suffix_underscore(self):
    # Removes the final underscore
    assert Foo.attr_html_name("bar_") == "bar" 

  # def test_initializing_an_attribute_in_constructor_with_invalid_name(self):
  #   # Raises an Exception,
  #   with pytest.raises(Exception):
  #     node = Foo(invalid="baz") 

class TestTextAttribute():
  def test_setting_to_a_string(self):
    # Assigns the string the attribute's value
    assert Foo(bar="baz").render_inline() == '<foo bar="baz"></foo>'

  def test_setting_multiple_attributes(self):
    # Assigns the string the attribute's value
    assert Foo(bar="baz", baz="quux", bar_bool=True, bar_text=None).render_inline() == '<foo bar="baz" baz="quux" bar-bool></foo>'

  def test_setting_to_an_int(self):
    # Converts the number to a string
    assert Foo(bar=1).render_inline() == '<foo bar="1"></foo>'

#   def test_setting_to_a_float(self):
#     # Converts the number to a string
#     assert Foo(bar=1.23).render_inline() == '<foo bar="1.23"></foo>'

  def test_setting_to_an_empty_string(self):
    # Assigns the empty string to the attributes's value
    assert Foo(bar="").render_inline() == '<foo bar=""></foo>'  

  def test_setting_to_none(self):
    # Removes the attribute
    assert Foo(bar=None).render_inline() == "<foo></foo>"  

class TestBooleanAttribute():
  def test_setting_to_true(self):
    # Renders only the attribute name, without a value
    assert Foo(bar_bool=True).render_inline() == "<foo bar-bool></foo>"

  def test_setting_to_false(self):
    # Removes the attribute
    assert Foo(bar_bool=False).render_inline() == "<foo></foo>"

  def test_setting_to_none(self):
    # Removes the attribute
    assert Foo(bar_bool=None).render_inline() == "<foo></foo>"

class TestPseudoBooleanAttribute():
  def test_setting_to_true(self):
    # Renders only the attribute name, without a value
    assert Foo(bar_bool=True).render_inline() == "<foo bar-bool></foo>"

  def test_setting_to_false(self):
    # Removes the attribute
    assert Foo(bar_bool=False).render_inline() == "<foo></foo>"

  def test_setting_to_none(self):
    # Removes the attribute
    assert Foo(bar_bool=None).render_inline() == "<foo></foo>"

  def test_setting_to_string_true(self):
    # Assigns the string the attribute's value
    assert Foo(bar="true").render_inline() == '<foo bar="true"></foo>'  

  def test_setting_to_string_false(self):
    # Assigns the string the attribute's value
    assert Foo(bar="false").render_inline() == '<foo bar="false"></foo>'  

class TestHtmlAttribute():
  def test_setting_attribute_to_html_markup(self):
    # Escapes the markup
    node = Foo(bar_html='<bar class="foo"></bar>')
    assert node.render_inline() == '<foo bar-html="&lt;bar class=&quot;foo&quot;&gt;&lt;/bar&gt;"></foo>'

  def test_setting_attribute_to_none(self):
    # Removes the attribute
    node = Foo(bar_html=None)
    assert node.render_inline() == "<foo></foo>"

class TestAttributeJs():
  # def test_setting_attribute_to_js_code(self):
  # TODO
  #   # Escapes the markup
  #   node = Foo(bar_js='foo(bar);')
  #   assert node.render_inline() == '<foo bar-js="foo(bar);"></foo>'

  def test_setting_attribute_to_none(self):
    # Removes the attribute
    node = Foo(bar_js=None)
    assert node.render_inline() == "<foo></foo>"

class TestAttributeStyle():
  def test_setting_attribute_to_none(self):
    # Removes the attribute
    node = Foo(bar_style=None)
    assert node.render_inline() == "<foo></foo>"

class TestAttributeUrl():
  # def test_setting_attribute_to_a_url(self):
  #   # URL-encodes the attribute
  #   node = Foo(bar_url='www.foo.bar/baz/?quux="1"&waldo=<fred>')
  #   assert node.render_inline() == '<foo bar-url="www.foo.bar/baz/%3Fquux%3D%221%22%26waldo%3D%3Cfred%3E"></foo>'

  def test_setting_attribute_to_none(self):
    # Removes the attribute
    node = Foo(bar_url=None)
    assert node.render_inline() == "<foo></foo>"

class TestDataAttribute():
  def test_creating_a_data_attribute_with_dict_like_syntax(self): 
    # Renders the attribute name with a 'data-' prefix
    assert Foo(data={"bar": "baz"}).render_inline() == '<foo data-bar="baz"></foo>'   

  def test_creating_a_data_attribute_with_multiple_values(self): 
    # Renders the attribute names with a 'data-' prefix
    assert Foo(data={"bar": "baz", "quux": "fred"}).render_inline() == '<foo data-bar="baz" data-quux="fred"></foo>' 

  def test_creating_a_data_attribute_without_a_dict(self): 
    # Renders the attribute name without a suffix
    assert Foo(data="bar").render_inline() == '<foo data="bar"></foo>'   

class TestAriaAttribute():
  def test_creating_an_aria_attribute_with_dict_like_syntax(self): 
    # Renders the attribute name with an 'aria-' prefix
    assert Foo(aria={"bar": "baz"}).render_inline() == '<foo aria-bar="baz"></foo>'   

  def test_creating_an_aria_attribute_with_multiple_values(self): 
    # Renders the attribute names with a 'aria-' prefix
    assert Foo(aria={"bar": "baz", "quux": "fred"}).render_inline() == '<foo aria-bar="baz" aria-quux="fred"></foo>' 

  def test_creating_an_aria_attribute_without_a_dict(self): 
    # Renders the attribute name without a suffix
    assert Foo(aria="bar").render_inline() == '<foo aria="bar"></foo>'   

class TestUserAttribute():
  def test_creating_a_user_attribute_with_dict_like_syntax(self): 
    # Renders the attribute name with a 'user-' prefix
    assert Foo(user={"bar": "baz"}).render_inline() == '<foo user-bar="baz"></foo>'   

  def test_creating_a_user_attribute_with_multiple_values(self): 
    # Renders the attribute names with a 'user-' prefix
    assert Foo(user={"bar": "baz", "quux": "fred"}).render_inline() == '<foo user-bar="baz" user-quux="fred"></foo>' 

  def test_creating_a_user_attribute_without_a_dict(self): 
    # Renders the attribute name without a suffix
    assert Foo(user="bar").render_inline() == '<foo user="bar"></foo>'   
