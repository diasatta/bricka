# Bricka
Build reusable and styled server-side HTML components with python.

Bricka is a library to generate HTML markup and CSS stylesheets without leaving python. The main purpose of the library is the building of reusable server-side HTML components, stylable directly from python. 

Use cases:
  - Create styled HTML reusable components
  - Template engine replacement
  - Generate HTML reports from data
  - Build static site generators

## Installation
To install Bricka from a command line:

```shell
pip install bricka
```

## Usage
### Creating a basic HTML document

In Bricka, HTML elements are defined as Python classes. There is a straightforward translation from HTML to Bricka, just by capitalizing the element's first letter.

HTML attribute names are written as is, except for conflicting attributes, which need a trailing underscore: `class` becomes `class_`.

Let's create our first Bricka component using the `with` context manager, which allows easily buiding HTML elements hierarchies.

```python
from bricka.elements import *

with Html(lang="en") as doc:
  with Head():
    Meta(charset="UTF-8")
    Meta(name="viewport", content="width=device-width, initial-scale=1.0") 
    Link(rel="stylesheet", href="style.css")
    Title("Document", class_="title")    

  with Body():
    P("My first document with Bricka")  

print(doc.render())  
```

In the above example, we created a component of type `Html` named `doc`, with a hierarchy of children. Attributes are passed as keyword arguments to each element's constructor.

To get the HTML out of the component, we call the `render()` method, generating a well formatted HTML markup as a string, as shown below.

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
One of the main features of Bricka is the ability to style components without leaving Python. Styles are defined as Python dicts, and then passed to HTML elements as arguments.

Before rendering, a lot of processing is applied to styles in order to solve common problems related to conflicting CSS properties, and also to optimize CSS output size. After processing the user defined styles, Bricka generates CSS atomic classes.

To give an illustration, let's build a simple styled HTML table.

```python
from bricka.elements import Table, Tbody, Thead, Th, Td, Tr
from bricka.style import Style

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
    "color": "blue",
    ":hover": {
      "color": "navy",
      "background-color": "fuchsia",
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
```

In the above example, after defining the `fruits` data as a list, we declare a dict named `style` with a type hint `Style`. This type hint is necessary to get autocompletion for CSS property names and property values. 

Inside the `style` dict, we have named CSS rules, with arbitrary names, as nested dicts. Inside a rule, there are CSS properties with their values.

All CSS properties' values are entered as strings. For CSS shorthand properties, ie, having multiple values, a tuple is used to group the values, as for the `border` propery.

In the `tr` rule, a pseudo-class is defined as a nested rule with the pseudo-class `:hover` as name.

Once the style is defined, it is applied to the elements using the `css` keyword argument. You can choose which rules are applied to each element using a dict-like syntax to select a rule from the `style`.

Now, our component is ready to be rendered. Calling `render()` on the `table` component, renders the HTML markup with the class attribute filled using the generated CSS atomic classes.

```html
<table class="be6697e7 bf18cedd ">
  <thead>
    <tr>
      <th class="b1acb709 b10a659d be6697e7 ba3a81d2 bd93d40d ">#</th>
      <th class="b1acb709 b10a659d be6697e7 ba3a81d2 bd93d40d ">Fruit</th>
      <th class="b1acb709 b10a659d be6697e7 ba3a81d2 bd93d40d ">Color</th>
    </tr>
  </thead>
  <tbody>
    <tr class="b30ef48f bb449833 b8c123ec1 ">
      <td class="be6697e7 ba3a81d2 bd93d40d ">1</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Banana</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Yellow</td>
    </tr>
    <tr class="b30ef48f bb449833 b8c123ec1 ">
      <td class="be6697e7 ba3a81d2 bd93d40d ">2</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Orange</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Orange</td>
    </tr>
    <tr class="b30ef48f bb449833 b8c123ec1 ">
      <td class="be6697e7 ba3a81d2 bd93d40d ">3</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Apricot</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Orange</td>
    </tr>
    <tr class="b30ef48f bb449833 b8c123ec1 ">
      <td class="be6697e7 ba3a81d2 bd93d40d ">4</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Apple</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Green</td>
    </tr>
    <tr class="b30ef48f bb449833 b8c123ec1 ">
      <td class="be6697e7 ba3a81d2 bd93d40d ">5</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Lemon</td>
      <td class="be6697e7 ba3a81d2 bd93d40d ">Yellow</td>
    </tr>
  </tbody>
</table>
```

To get the final CSS output as atomic classes, use the `render_css()` method. 

```python
print(table.render_css())
```

The CSS output is shown below. It is up to you how to use the CSS output: 

  - Write the output to a `style.css` file and insert a `Link` element in your HTML document to reference the `style.css` stylesheet
  - Or insert the output in a `Style` element in your HTML document.

```css
.be6697e7 { border: 1px solid black; }
.bf18cedd { border-collapse: collapse; }
.b1acb709 { font-weight: 600; }
.b10a659d { background-color: aqua; }
.ba3a81d2 { padding-left: 0.75rem; }
.bd93d40d { padding-right: 0.75rem; }
.b30ef48f { color: blue; }
.bb449833:hover { background-color: fuchsia; }
.b8c123ec1:hover { color: navy; }
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
