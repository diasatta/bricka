# Bricka
Build reusable styled HTML components with python.

## Installation

`pip install bricka`

## Usage
Creating a basic HTML document.

```python
from bricka.elements import *

with Html(lang="en") as doc:
  with Head():
    Meta(charset="UTF-8")
    Meta(name="viewport", content="width=device-width, initial-scale=1.0") 
    Link(rel="stylesheet", href=f"style.css")
    Title("Document", class_="title")    

  with Body():
    P("My first document with Bricka")  

print(doc.render())  
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title class="title">Document</title>
  </head>
  <body>
    <p>My first document with Bricka</p>
  </body>
</html>
```

## Features
Below are the main features of Bricka:

  - Create complex element hierarchies using context managers
  - Append elements with the right and left shift operators
  - Create element siblings with the plus operator
  - Context-aware escaping
  - Support for standard HTML elements
  - Support for standard HTML attributes
  - Code autocompletion for HTML attributes
  - Comprehensive unit tests
