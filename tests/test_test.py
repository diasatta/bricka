import pytest
from bricka.node import Node

class Test():
  def test(self):
    assert Node().tag_name == "node"
    assert 1 == 1