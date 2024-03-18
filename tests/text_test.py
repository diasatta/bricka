from bricka.node import Text

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