from bricka.node import Root
from foo_elements import Foo, Bar

class TestRootRendering():
  def test_rendering_an_empty_root(self):
    # Renders an empty string
    node = Root()
    assert node.render() == ""