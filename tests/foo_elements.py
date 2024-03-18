from bricka.node import Container, Void

class Foo(Container):
  tag_name: str = "foo"

class Bar(Container):
  tag_name: str = "bar"

class Baz(Container):
  tag_name: str = "baz"

class Quux(Void):
  tag_name: str = "quux"

class Fred(Void):
  tag_name: str = "fred"
