# Bricka
Build reusable styled HTML components with python.

## Installation

`pip install bricka`

## Usage
### Creating a basic HTML document.

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

### Creating a styled table

```python
from bricka.elements import *

headers = ["Fruit", "Color"]

fruits = [
  ["Banana", "Yellow"],
  ["Orange", "Orange"],
  ["Apricot", "Orange"],
  ["Apple", "Green"],
  ["Lemon", "Yellow"]
]

style: Style = {
  "table": {
    "border": ("1px", "solid", "black"),
    "border-collapse": "collapse",      
  },
  "th": {
    "font-weight": "600",
    "background-color": "aqua",
  },
  "td": {
    "border": ("1px", "solid", "black"),
    "padding-x": "0.75rem",
  },
  "tr": {
    ":hover": {
      "background-color": "fuchsia"
    }
  },
}

with Table(css=style["table"]) as table:
  with Thead():
    with Tr():
      Th("#", css=[style["th"], style["td"]])
      for header in headers:
        Th(header, css=[style["th"], style["td"]])

  with Tbody():
    for i, fruit in enumerate(fruits):
      with Tr(css=style["tr"]):
        Td(i+1, css=style["td"])
        Td(fruit[0], css=style["td"])
        Td(fruit[1], css=style["td"])

  print(table.render())
  print(table.render_css())
```

Generated HTML.

```html
<table class="fe6697e7 ff18cedd ">
  <thead>
    <tr>
      <th class="f1acb709 f10a659d fe6697e7 fa3a81d2 fd93d40d ">#</th>
      <th class="f1acb709 f10a659d fe6697e7 fa3a81d2 fd93d40d ">Fruit</th>
      <th class="f1acb709 f10a659d fe6697e7 fa3a81d2 fd93d40d ">Color</th>
    </tr>
  </thead>
  <tbody>
    <tr class="feec5036 ">
      <td class="fe6697e7 fa3a81d2 fd93d40d ">1</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Banana</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Yellow</td>
    </tr>
    <tr class="feec5036 ">
      <td class="fe6697e7 fa3a81d2 fd93d40d ">2</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Orange</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Orange</td>
    </tr>
    <tr class="feec5036 ">
      <td class="fe6697e7 fa3a81d2 fd93d40d ">3</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Apricot</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Orange</td>
    </tr>
    <tr class="feec5036 ">
      <td class="fe6697e7 fa3a81d2 fd93d40d ">4</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Apple</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Green</td>
    </tr>
    <tr class="feec5036 ">
      <td class="fe6697e7 fa3a81d2 fd93d40d ">5</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Lemon</td>
      <td class="fe6697e7 fa3a81d2 fd93d40d ">Yellow</td>
    </tr>
  </tbody>
</table>
```

Generated CSS.

```css
.fe6697e7 { border: 1px solid black; }
.ff18cedd { border-collapse: collapse; }
.f1acb709 { font-weight: 600; }
.f10a659d { background-color: aqua; }
.fa3a81d2 { padding-left: 0.75rem; }
.fd93d40d { padding-right: 0.75rem; }
.feec5036:hover { background-color: fuchsia; }
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
  - Components styling with pure python
  - Create styles using ready CSS constraints
  - Atomic CSS generation
  - Code autocompletion for CSS properties and constraints
  - Comprehensive unit tests
