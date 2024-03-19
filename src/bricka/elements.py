from typing import cast, Unpack
from bricka.node import Node, Container, Void
from bricka.attrs import *

#region A
class A(Container):
  """
  Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.
  """
  tag_name: str = "a"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[AAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> AAttrs:
    return cast(AAttrs, self._attrs)

class Abbr(Container):
  """
  Represents an abbreviation or acronym.
  """
  tag_name: str = "abbr"
  inline: bool = True

class Address(Container):
  """
  Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.
  """
  tag_name: str = "address"

class Area(Void):
  """
  Defines an area inside an image map that has predefined clickable areas. An image map allows geometric areas on an image to be associated with hyperlink.
  """
  tag_name: str = "area"

  def __init__(self, **attrs: Unpack[AreaAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> AreaAttrs:
    return cast(AreaAttrs, self._attrs)

class Article(Container):
  """
  Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.
  """
  tag_name: str = "article"

class Aside(Container):
  """
  Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.
  """
  tag_name: str = "aside"

class Audio(Container):
  """
  Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a MediaStream.
  """
  tag_name: str = "audio"

  def __init__(self, *children: Node, **attrs: Unpack[AudioAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> AudioAttrs:
    return cast(AudioAttrs, self._attrs)

#endregion
#region B
class B(Container):
  """
  Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `b` for styling text or granting importance. If you wish to create boldface text, you should use the CSS 'font-weight' property. If you wish to indicate an element is of special importance, you should use the strong element.
  """
  tag_name: str = "b"
  inline: bool = True

class Base(Void):
  """
  Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.
  """
  tag_name: str = "base"
  inline: bool = True

  def __init__(self, **attrs: Unpack[BaseAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> BaseAttrs:
    return cast(BaseAttrs, self._attrs)

class Bdi(Container):
  """
  Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.
  """
  tag_name: str = "bdi"
  inline: bool = True

class Bdo(Container):
  """
  Overrides the current directionality of text, so that the text within is rendered in a different direction.
  """
  tag_name: str = "bdo"
  inline: bool = True

class Blockquote(Container):
  """
  Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the `cite` element.
  """
  tag_name: str = "blockquote"

  def __init__(self, *children: Node, **attrs: Unpack[BlockquoteAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> BlockquoteAttrs:
    return cast(BlockquoteAttrs, self._attrs)

class Body(Container):
  """
  represents the content of an HTML document. There can be only one such element in a document.
  """
  tag_name: str = "body"

  def __init__(self, *children: Node, **attrs: Unpack[BodyAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> BodyAttrs:
    return cast(BodyAttrs, self._attrs)

class Br(Void):
  """
  Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.
  """
  tag_name: str = "br"

class Button(Container):
  """
  An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a form or opening a dialog.
  """
  tag_name: str = "button"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[ButtonAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> ButtonAttrs:
    return cast(ButtonAttrs, self._attrs)

#endregion
#region C
class Canvas(Container):
  """
  Container element to use with either the canvas scripting API or the WebGL API to draw graphics and animations.
  """
  tag_name: str = "canvas"

  def __init__(self, *children: Node, **attrs: Unpack[CanvasAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> CanvasAttrs:
    return cast(CanvasAttrs, self._attrs)

class Caption(Container):
  """
  Specifies the caption (or title) of a table.
  """
  tag_name: str = "caption"
  inline: bool = True

class Cite(Container):
  """
  Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.
  """
  tag_name: str = "cite"
  inline: bool = True

class Code(Container):
  """
  Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.
  """
  tag_name: str = "code"

class Col(Void):
  """
  Defines one or more columns in a column group represented by its implicit or explicit parent `colgroup` element. The `col` element is only valid as a child of a `colgroup` element that has no `span` attribute defined.
  """
  tag_name: str = "col"
  inline: bool = True

  def __init__(self, **attrs: Unpack[ColAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> ColAttrs:
    return cast(ColAttrs, self._attrs)

class Colgroup(Container):
  """
  Defines a group of columns within a table.
  """
  tag_name: str = "colgroup"

  def __init__(self, *children: Node, **attrs: Unpack[ColgroupAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> ColgroupAttrs:
    return cast(ColgroupAttrs, self._attrs)

#endregion
#region D
class Data(Container):
  """
  Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`time` element must be used.
  """
  tag_name: str = "data"

  def __init__(self, *children: Node, **attrs: Unpack[DataAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> DataAttrs:
    return cast(DataAttrs, self._attrs)

class Datalist(Container):
  """
  Contains a set of `option` elements that represent the permissible or recommended options available to choose from within other controls.
  """
  tag_name: str = "datalist"

class Dd(Container):
  """
  Provides the description, definition, or value for the preceding term (`dt`) in a description list (`dl`).
  """
  tag_name: str = "dd"

class Del(Container):
  """
  Represents a range of text that has been deleted from a document. This can be used when rendering 'track changes' or source code diff information, for example. The `ins` element can be used for the opposite purpose: to indicate text that has been added to the document.
  """
  tag_name: str = "del"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[DelAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> DelAttrs:
    return cast(DelAttrs, self._attrs)

class Details(Container):
  """
  Creates a disclosure widget in which information is visible only when the widget is toggled into an 'open' state. A summary or label must be provided using the `summary` element.
  """
  tag_name: str = "details"

  def __init__(self, *children: Node, **attrs: Unpack[DetailsAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> DetailsAttrs:
    return cast(DetailsAttrs, self._attrs)

class Dfn(Container):
  """
  Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor `p` element, the `dt`/`dd` pairing, or the nearest section ancestor of the `dfn` element, is considered to be the definition of the term.
  """
  tag_name: str = "dfn"
  inline: bool = True

class Dialog(Container):
  """
  Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.
  """
  tag_name: str = "dialog"

  def __init__(self, *children: Node, **attrs: Unpack[DialogAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> DialogAttrs:
    return cast(DialogAttrs, self._attrs)

class Div(Container):
  """
  The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like flexbox is applied to its parent element).
  """
  tag_name: str = "div"

class Dl(Container):
  """
  Represents a description list. The element encloses a list of groups of terms (specified using the `dt` element) and descriptions (provided by `dd` elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).
  """
  tag_name: str = "dl"

class Dt(Container):
  """
  Specifies a term in a description or definition list, and as such must be used inside a `dl` element. It is usually followed by a `dd` element; however, multiple `dt` elements in a row indicate several terms that are all defined by the immediate next `dd` element.
  """
  tag_name: str = "dt"

#endregion
#region E
class Em(Container):
  """
  Marks text that has stress emphasis. The `em` element can be nested, with each nesting level indicating a greater degree of emphasis.
  """
  tag_name: str = "em"
  inline: bool = True

class Embed(Void):
  """
  Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.
  """
  tag_name: str = "embed"

  def __init__(self, **attrs: Unpack[EmbedAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> EmbedAttrs:
    return cast(EmbedAttrs, self._attrs)

#endregion
#region F
class Fieldset(Container):
  """
  Used to group several controls as well as labels (`label`) within a web form.
  """
  tag_name: str = "fieldset"

  def __init__(self, *children: Node, **attrs: Unpack[FieldsetAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> FieldsetAttrs:
    return cast(FieldsetAttrs, self._attrs)

class Figcaption(Container):
  """
  Represents a caption or legend describing the rest of the contents of its parent `figure` element.
  """
  tag_name: str = "figcaption"

class Figure(Container):
  """
  Represents self-contained content, potentially with an optional caption, which is specified using the `figcaption` element. The figure, its caption, and its contents are referenced as a single unit.
  """
  tag_name: str = "figure"

class Footer(Container):
  """
  Represents a footer for its nearest ancestor sectioning content or sectioning root element. A `footer` typically contains information about the author of the section, copyright data, or links to related documents.
  """
  tag_name: str = "footer"

class Form(Container):
  """
  Represents a document section containing interactive controls for submitting information.
  """
  tag_name: str = "form"

  def __init__(self, *children: Node, **attrs: Unpack[FormAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> FormAttrs:
    return cast(FormAttrs, self._attrs)

#endregion
#region H
class H1(Container):
  """
  Level 1 of section headings
  """
  tag_name: str = "h1"
  inline: bool = True

class H2(Container):
  """
  Level 2 of section headings
  """
  tag_name: str = "h2"
  inline: bool = True

class H3(Container):
  """
  Level 3 of section headings
  """
  tag_name: str = "h3"
  inline: bool = True

class H4(Container):
  """
  Level 4 of section headings
  """
  tag_name: str = "h4"
  inline: bool = True

class H5(Container):
  """
  Level 5 of section headings
  """
  tag_name: str = "h5"
  inline: bool = True

class H6(Container):
  """
  Level 6 of section headings
  """
  tag_name: str = "h6"
  inline: bool = True

class Head(Container):
  """
  Contains machine-readable information (metadata) about the document, like its title, scripts, and style sheets.
  """
  tag_name: str = "head"

class Header(Container):
  """
  Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.
  """
  tag_name: str = "header"

class Hgroup(Container):
  """
  Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.
  """
  tag_name: str = "hgroup"

class Hr(Void):
  """
  Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.
  """
  tag_name: str = "hr"

class Html(Container):
  """
  Represents the root (top-level element) of an HTML document, so it is also referred to as the root element. All other elements must be descendants of this element.
  """
  tag_name: str = "html"

  def __init__(self, *children: Node, **attrs: Unpack[HtmlAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> HtmlAttrs:
    return cast(HtmlAttrs, self._attrs)
  
  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    return "<!DOCTYPE html>\n" + super().render(level, spaces, escape) 

#endregion
#region I
class I(Container):
  """
  Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `i` naming of this element.
  """
  tag_name: str = "i"
  inline: bool = True

class Iframe(Container):
  """
  Represents a nested browsing context, embedding another HTML page into the current one.
  """
  tag_name: str = "iframe"

  def __init__(self, *children: Node, **attrs: Unpack[IframeAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> IframeAttrs:
    return cast(IframeAttrs, self._attrs)

class Img(Void):
  """
  Embeds an image into the document.
  """
  tag_name: str = "img"

  def __init__(self, **attrs: Unpack[ImgAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> ImgAttrs:
    return cast(ImgAttrs, self._attrs)

class Input(Void):
  """
  Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `input` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.
  """
  tag_name: str = "input"

  def __init__(self, **attrs: Unpack[InputAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> InputAttrs:
    return cast(InputAttrs, self._attrs)

class Ins(Container):
  """
  Represents a range of text that has been added to a document. You can use the `del` element to similarly represent a range of text that has been deleted from the document.
  """
  tag_name: str = "ins"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[InsAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> InsAttrs:
    return cast(InsAttrs, self._attrs)

#endregion
#region K
class Kbd(Container):
  """
  Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `kbd` element using its default monospace font, although this is not mandated by the HTML standard.
  """
  tag_name: str = "kbd"
  inline: bool = True

#endregion
#region L
class Label(Container):
  """
  Represents a caption for an item in a user interface.
  """
  tag_name: str = "label"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[LabelAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> LabelAttrs:
    return cast(LabelAttrs, self._attrs)

class Legend(Container):
  """
  Represents a caption for the content of its parent `fieldset`.
  """
  tag_name: str = "legend"
  inline: bool = True

class Li(Container):
  """
  Represents an item in a list. It must be contained in a parent element: an ordered list (`ol`), an unordered list (`ul`), or a menu (`menu`). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.
  """
  tag_name: str = "li"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[LiAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> LiAttrs:
    return cast(LiAttrs, self._attrs)

class Link(Void):
  """
  Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both 'favicon' style icons and icons for the home screen and apps on mobile devices) among other things.
  """
  tag_name: str = "link"

  def __init__(self, **attrs: Unpack[LinkAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> LinkAttrs:
    return cast(LinkAttrs, self._attrs)

#endregion
#region M
class Main(Container):
  """
  Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.
  """
  tag_name: str = "main"

class Map(Container):
  """
  Used with `area` elements to define an image map (a clickable link area).
  """
  tag_name: str = "map"

  def __init__(self, *children: Node, **attrs: Unpack[MapAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> MapAttrs:
    return cast(MapAttrs, self._attrs)

class Mark(Container):
  """
  Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.
  """
  tag_name: str = "mark"
  inline: bool = True

class Menu(Container):
  """
  A semantic alternative to `ul`, but treated by browsers (and exposed through the accessibility tree) as no different than `ul`. It represents an unordered list of items (which are represented by `li` elements).
  """
  tag_name: str = "menu"

class Meta(Void):
  """
  Represents metadata that cannot be represented by other HTML meta-related elements, like `base`, `link`, `script`, `style` and `title`.
  """
  tag_name: str = "meta"

  def __init__(self, **attrs: Unpack[MetaAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> MetaAttrs:
    return cast(MetaAttrs, self._attrs)

class Meter(Container):
  """
  Represents either a scalar value within a known range or a fractional value.
  """
  tag_name: str = "meter"

  def __init__(self, *children: Node, **attrs: Unpack[MeterAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> MeterAttrs:
    return cast(MeterAttrs, self._attrs)

#endregion
#region N
class Nav(Container):
  """
  Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.
  """
  tag_name: str = "nav"

class Noscript(Container):
  """
  Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.
  """
  tag_name: str = "noscript"
  inline: bool = True

#endregion
#region O
class Object(Container):
  """
  Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.
  """
  tag_name: str = "object"

  def __init__(self, *children: Node, **attrs: Unpack[ObjectAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> ObjectAttrs:
    return cast(ObjectAttrs, self._attrs)

class Ol(Container):
  """
  Represents an ordered list of items — typically rendered as a numbered list.
  """
  tag_name: str = "ol"

  def __init__(self, *children: Node, **attrs: Unpack[OlAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> OlAttrs:
    return cast(OlAttrs, self._attrs)

class Optgroup(Container):
  """
  Creates a grouping of options within a `select` element.
  """
  tag_name: str = "optgroup"

  def __init__(self, *children: Node, **attrs: Unpack[OptgroupAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> OptgroupAttrs:
    return cast(OptgroupAttrs, self._attrs)

class Option(Container):
  """
  Used to define an item contained in a select, an `optgroup`, or a `datalist` element. As such, `option` can represent menu items in popups and other lists of items in an HTML document.
  """
  tag_name: str = "option"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[OptionAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> OptionAttrs:
    return cast(OptionAttrs, self._attrs)

class Output(Container):
  """
  Container element into which a site or app can inject the results of a calculation or the outcome of a user action.
  """
  tag_name: str = "output"

  def __init__(self, *children: Node, **attrs: Unpack[OutputAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> OutputAttrs:
    return cast(OutputAttrs, self._attrs)

#endregion
#region P
class P(Container):
  """
  Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.
  """
  tag_name: str = "p"
  inline: bool = True

class Picture(Container):
  """
  Contains zero or more `source` elements and one `img` element to offer alternative versions of an image for different display/device scenarios.
  """
  tag_name: str = "picture"

class Pre(Container):
  """
  Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or monospaced, font. Whitespace inside this element is displayed as written.
  """
  tag_name: str = "pre"

class Progress(Container):
  """
  Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
  """
  tag_name: str = "progress"

  def __init__(self, *children: Node, **attrs: Unpack[ProgressAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> ProgressAttrs:
    return cast(ProgressAttrs, self._attrs)

#endregion
#region Q
class Q(Container):
  """
  Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the `blockquote` element.
  """
  tag_name: str = "q"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[QAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> QAttrs:
    return cast(QAttrs, self._attrs)

#endregion
#region R
class Rp(Container):
  """
  Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the `ruby` element. One `rp` element should enclose each of the opening and closing parentheses that wrap the `rt` element that contains the annotation's text.
  """
  tag_name: str = "rp"
  inline: bool = True

class Rt(Container):
  """
  Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `rt` element must always be contained within a `ruby` element.
  """
  tag_name: str = "rt"
  inline: bool = True

class Ruby(Container):
  """
  Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.
  """
  tag_name: str = "ruby"
  inline: bool = True

#endregion
#region S
class S(Container):
  """
  Renders text with a strikethrough, or a line through it. Use the `s` element to represent things that are no longer relevant or no longer accurate. However, `s` is not appropriate when indicating document edits; for that, use the del and ins elements, as appropriate.
  """
  tag_name: str = "s"
  inline: bool = True

class Samp(Container):
  """
  Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as Courier or Lucida Console).
  """
  tag_name: str = "samp"
  inline: bool = True

class Script(Container):
  """
  Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `script` element can also be used with other languages, such as WebGL's GLSL shader programming language and JSON.
  """
  tag_name: str = "script"

  def __init__(self, *children: Node, **attrs: Unpack[ScriptAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> ScriptAttrs:
    return cast(ScriptAttrs, self._attrs)

class Section(Container):
  """
  Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.
  """
  tag_name: str = "section"

class Select(Container):
  """
  Represents a control that provides a menu of options.
  """
  tag_name: str = "select"

  def __init__(self, *children: Node, **attrs: Unpack[SelectAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> SelectAttrs:
    return cast(SelectAttrs, self._attrs)

class Slot(Container):
  """
  Part of the Web Components technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.
  """
  tag_name: str = "slot"

  def __init__(self, *children: Node, **attrs: Unpack[SlotAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> SlotAttrs:
    return cast(SlotAttrs, self._attrs)

class Small(Container):
  """
  Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from 'small' to 'x-small'.
  """
  tag_name: str = "small"
  inline: bool = True

class Source(Void):
  """
  Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for image file formats and media file formats.
  """
  tag_name: str = "source"

  def __init__(self, **attrs: Unpack[SourceAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> SourceAttrs:
    return cast(SourceAttrs, self._attrs)

class Span(Container):
  """
  A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `span` is very much like a div element, but div is a block-level element whereas a `span` is an inline-level element.
  """
  tag_name: str = "span"
  inline: bool = True

class Strong(Container):
  """
  Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.
  """
  tag_name: str = "strong"
  inline: bool = True

class Style(Container):
  """
  Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.
  """
  tag_name: str = "style"

  def __init__(self, *children: Node, **attrs: Unpack[StyleAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> StyleAttrs:
    return cast(StyleAttrs, self._attrs)

class Sub(Container):
  """
  Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.
  """
  tag_name: str = "sub"
  inline: bool = True

class Summary(Container):
  """
  Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `summary` element toggles the state of the parent `details` element open and closed.
  """
  tag_name: str = "summary"

class Sup(Container):
  """
  Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.
  """
  tag_name: str = "sup"
  inline: bool = True

class Svg(Container):
  """
  Container defining a new coordinate system and viewport. It is used as the outermost element of SVG documents, but it can also be used to embed an SVG fragment inside an SVG or HTML document.
  """
  tag_name: str = "svg"

#endregion
#region T
class Table(Container):
  """
  Represents tabular data—that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.
  """
  tag_name: str = "table"

class Tbody(Container):
  """
  Encapsulates a set of table rows (`tr` elements), indicating that they comprise the body of a table's (main) data.
  """
  tag_name: str = "tbody"

class Td(Container):
  """
  A child of the `tr` element, it defines a cell of a table that contains data.
  """
  tag_name: str = "td"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[TdAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> TdAttrs:
    return cast(TdAttrs, self._attrs)

class Template(Container):
  """
  A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.
  """
  tag_name: str = "template"

class Textarea(Container):
  """
  Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.
  """
  tag_name: str = "textarea"

  def __init__(self, *children: Node, **attrs: Unpack[TextareaAttrs]) -> None:
    super().__init__(*children, **attrs) # type: ignore

  @property
  def attrs(self) -> TextareaAttrs:
    return cast(TextareaAttrs, self._attrs)

class Tfoot(Container):
  """
  Encapsulates a set of table rows (`tr` elements), indicating that they comprise the foot of a table with information about the table's columns. This is usually a summary of the columns, e.g., a sum of the given numbers in a column.
  """
  tag_name: str = "tfoot"

class Th(Container):
  """
  A child of the `tr` element, it defines a cell as the header of a group of table cells. The nature of this group can be explicitly defined by the `scope` and `headers` attributes.
  """
  tag_name: str = "th"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[ThAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> ThAttrs:
    return cast(ThAttrs, self._attrs)

class Thead(Container):
  """
  Encapsulates a set of table rows (`tr` elements), indicating that they comprise the head of a table with information about the table's columns. This is usually in the form of column headers (`th` elements).
  """
  tag_name: str = "thead"

class Time(Container):
  """
  Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.
  """
  tag_name: str = "time"
  inline: bool = True

  def __init__(self, *children: Node, **attrs: Unpack[TimeAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> TimeAttrs:
    return cast(TimeAttrs, self._attrs)

class Title(Container):
  """
  Defines the document's title that is shown in a browser's title bar or a page's tab. It only contains text; tags within the element are ignored.
  """
  tag_name: str = "title"
  inline: bool = True

class Tr(Container):
  """
  Defines a row of cells in a table. The row's cells can then be established using a mix of `td` (data cell) and `th` (header cell) elements.
  """
  tag_name: str = "tr"

class Track(Void):
  """
  Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in WebVTT format ('.vtt' files)—Web Video Text Tracks.
  """
  tag_name: str = "track"

  def __init__(self, **attrs: Unpack[TrackAttrs]) -> None:
    super().__init__(**attrs)

  @property
  def attrs(self) -> TrackAttrs:
    return cast(TrackAttrs, self._attrs)

#endregion
#region U
class U(Container):
  """
  Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.
  """
  tag_name: str = "u"
  inline: bool = True

class Ul(Container):
  """
  Represents an unordered list of items, typically rendered as a bulleted list.
  """
  tag_name: str = "ul"

#endregion
#region V
class Var(Container):
  """
  Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.
  """
  tag_name: str = "var"
  inline: bool = True

class Video(Container):
  """
  Embeds a media player which supports video playback into the document. You can also use `video` for audio content, but the audio element may provide a more appropriate user experience.
  """
  tag_name: str = "video"

  def __init__(self, *children: Node, **attrs: Unpack[VideoAttrs]) -> None:
    super().__init__(*children, **attrs)

  @property
  def attrs(self) -> VideoAttrs:
    return cast(VideoAttrs, self._attrs)

#endregion
#region W
class Wbr(Void):
  """
  Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.
  """
  tag_name: str = "wbr"
  inline: bool = True

#endregion
