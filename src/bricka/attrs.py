from typing import Literal

AReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
ARelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "tag",
]
ATargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
AreaReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
AreaRelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "tag",
]
AreaShapeL = Literal[
  "circle",
  "default",
  "poly",
  "rect",
]
AreaTargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
AudioCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
AudioPreloadL = Literal[
  "auto",
  "metadata",
  "none",
]
BaseTargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
ButtonFormenctypeL = Literal[
  "application/x-www-form-urlencoded",
  "multipart/form-data",
  "text/plain",
]
ButtonFormmethodL = Literal[
  "get",
  "post",
]
ButtonFormtargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
ButtonTypeL = Literal[
  "button",
  "reset",
  "submit",
]
DirL = Literal[
  "auto",
  "ltr",
  "rtl",
]
DraggableL = Literal[
  "false",
  "true",
]
FormAutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work",
]
FormEnctypeL = Literal[
  "application/x-www-form-urlencoded",
  "multipart/form-data",
  "text/plain",
]
FormMethodL = Literal[
  "get",
  "post",
]
FormRelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "tag",
]
FormTargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
HtmlXmlnsL = Literal[
  "http://www.w3.org/1999/xhtml",
]
IframeAllowfullscreenL = Literal[
  "false",
  "true",
]
IframeLoadingL = Literal[
  "eager",
  "lazy",
]
IframeReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
IframeSandboxL = Literal[
  "allow-forms",
  "allow-pointer-lock",
  "allow-popups",
  "allow-same-origin",
  "allow-scripts",
  "allow-top-navigation",
]
ImgCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
ImgDecodingL = Literal[
  "async",
  "auto",
  "sync",
]
ImgFetchpriorityL = Literal[
  "auto",
  "high",
  "low",
]
ImgLoadingL = Literal[
  "eager",
  "lazy",
]
ImgReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
InputAcceptL = Literal[
  "audio/*",
  "video/*",
  "image/*",
]
InputAutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work",
]
InputFormenctypeL = Literal[
  "application/x-www-form-urlencoded",
  "multipart/form-data",
  "text/plain",
]
InputFormmethodL = Literal[
  "get",
  "post",
]
InputFormtargetL = Literal[
  "_blank",
  "_self",
  "_parent",
  "_top",
]
InputTypeL = Literal[
  "button",
  "checkbox",
  "color",
  "date",
  "datetime",
  "datetime-local",
  "email",
  "file",
  "hidden",
  "image",
  "month",
  "number",
  "password",
  "radio",
  "range",
  "reset",
  "search",
  "submit",
  "tel",
  "text",
  "time",
  "url",
  "week",
]
InputmodeL = Literal[
  "email",
  "full-width-latin",
  "kana",
  "kana-name",
  "katakana",
  "latin",
  "latin-name",
  "latin-prose",
  "numeric",
  "tel",
  "url",
  "verbatim",
]
LinkCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
LinkReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
LinkRelL = Literal[
  "alternate",
  "author",
  "bookmark",
  "external",
  "help",
  "license",
  "next",
  "nofollow",
  "noreferrer",
  "noopener",
  "prev",
  "search",
  "tag",
]
MetaHttp_equivL = Literal[
  "content-security-policy",
  "content-type",
  "default-style",
  "refresh",
]
MetaNameL = Literal[
  "application-name",
  "author",
  "description",
  "generator",
  "keywords",
  "viewport",
]
OlTypeL = Literal[
  "1",
  "A",
  "I",
  "a",
  "i",
]
RoleL = Literal[
  "alert",
  "alertdialog",
  "application",
  "article",
  "banner",
  "button",
  "cell",
  "checkbox",
  "columnheader",
  "combobox",
  "complementary",
  "contentinfo",
  "definition",
  "dialog",
  "directory",
  "doc-abstract",
  "doc-acknowledgments",
  "doc-afterword",
  "doc-appendix",
  "doc-backlink",
  "doc-biblioentry",
  "doc-bibliography",
  "doc-biblioref",
  "doc-chapter",
  "doc-colophon",
  "doc-conclusion",
  "doc-cover",
  "doc-credit",
  "doc-credits",
  "doc-dedication",
  "doc-endnote",
  "doc-endnotes",
  "doc-epigraph",
  "doc-epilogue",
  "doc-errata",
  "doc-example",
  "doc-footnote",
  "doc-foreword",
  "doc-glossary",
  "doc-glossref",
  "doc-index",
  "doc-introduction",
  "doc-noteref",
  "doc-notice",
  "doc-pagebreak",
  "doc-pagelist",
  "doc-part",
  "doc-preface",
  "doc-prologue",
  "doc-pullquote",
  "doc-qna",
  "doc-subtitle",
  "doc-tip",
  "doc-toc",
  "document",
  "feed",
  "figure",
  "form",
  "grid",
  "gridcell",
  "group",
  "heading",
  "img",
  "link",
  "list",
  "listbox",
  "listitem",
  "log",
  "main",
  "marquee",
  "math",
  "menu",
  "menubar",
  "menuitem",
  "menuitemcheckbox",
  "menuitemradio",
  "navigation",
  "none",
  "note",
  "option",
  "presentation",
  "progressbar",
  "radio",
  "radiogroup",
  "region",
  "region",
  "row",
  "rowgroup",
  "rowheader",
  "scrollbar",
  "search",
  "searchbox",
  "separator",
  "slider",
  "spinbutton",
  "status",
  "switch",
  "tab",
  "table",
  "tablist",
  "tabpanel",
  "term",
  "text",
  "textbox",
  "timer",
  "toolbar",
  "tooltip",
  "tree",
  "treegrid",
  "treeitem",
]
ScriptCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
ScriptReferrerpolicyL = Literal[
  "no-referrer",
  "no-referrer-when-downgrade",
  "origin",
  "origin-when-cross-origin",
  "same-origin",
  "strict-origin-when-cross-origin",
  "unsafe-url",
]
SelectAutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work",
]
SpellcheckL = Literal[
  "false",
  "true",
]
TextareaAutocompleteL = Literal[
  "additional-name",
  "address-level1",
  "address-level2",
  "address-level3",
  "address-level4",
  "address-line1",
  "address-line2",
  "address-line3",
  "bday",
  "bday-day",
  "bday-month",
  "bday-year",
  "billing",
  "cc-additional-name",
  "cc-csc",
  "cc-exp",
  "cc-exp-month",
  "cc-exp-year",
  "cc-family-name",
  "cc-given-name",
  "cc-name",
  "cc-number",
  "cc-type",
  "country",
  "country-name",
  "current-password",
  "email",
  "family-name",
  "fax",
  "given-name",
  "home",
  "honorific-prefix",
  "honorific-suffix",
  "impp",
  "language",
  "mobile",
  "name",
  "new-password",
  "nickname",
  "off",
  "on",
  "organization",
  "organization-title",
  "pager",
  "photo",
  "postal-code",
  "sex",
  "shipping",
  "street-address",
  "tel",
  "tel-area-code",
  "tel-country-code",
  "tel-extension",
  "tel-local",
  "tel-local-prefix",
  "tel-local-suffix",
  "tel-national",
  "transaction-amount",
  "transaction-currency",
  "url",
  "username",
  "work",
]
TextareaSpellcheckL = Literal[
  "default",
  "false",
  "true",
]
TextareaWrapL = Literal[
  "hard",
  "soft",
]
ThScopeL = Literal[
  "col",
  "colgroup",
  "row",
  "rowgroup",
]
TrackKindL = Literal[
  "captions",
  "chapters",
  "descriptions",
  "metadata",
  "subtitles",
]
TranslateL = Literal[
  "no",
  "yes",
]
VideoCrossoriginL = Literal[
  "anonymous",
  "use-credentials",
]
VideoPreloadL = Literal[
  "auto",
  "metadata",
  "none",
]

from typing import TypedDict

class GlobalAttrs(TypedDict, total=False):
  accesskey: str
  autocapitalize: str
  autofocus: bool
  class_: str
  contenteditable: str
  dir: DirL
  draggable: DraggableL
  enterkeyhint: str
  hidden: str
  id: str
  inert: bool
  inputmode: InputmodeL
  is_: str
  itemid: str
  itemprop: str
  itemref: str
  itemscope: bool
  itemtype: str
  lang: str
  nonce: str
  part: str
  popover: str
  role: RoleL
  slot: str
  spellcheck: SpellcheckL
  style: str
  tabindex: str
  title: str
  translate: TranslateL
  virtualkeyboardpolicy: str

class AAttrs(GlobalAttrs, total=False):
  download: str
  href: str
  hreflang: str
  ping: str
  referrerpolicy: AReferrerpolicyL
  rel: ARelL
  target: ATargetL
  type: str

class AreaAttrs(GlobalAttrs, total=False):
  alt: str
  coords: str
  download: str
  href: str
  ping: str
  referrerpolicy: AreaReferrerpolicyL
  rel: AreaRelL
  shape: AreaShapeL
  target: AreaTargetL

class AudioAttrs(GlobalAttrs, total=False):
  autoplay: bool
  controls: bool
  crossorigin: AudioCrossoriginL
  loop: bool
  muted: bool
  preload: AudioPreloadL
  src: str

class BaseAttrs(GlobalAttrs, total=False):
  href: str
  target: BaseTargetL

class BlockquoteAttrs(GlobalAttrs, total=False):
  cite: str

class BodyAttrs(GlobalAttrs, total=False):
  onafterprint: str
  onbeforeprint: str
  onbeforeunload: str
  onblur: str
  onerror: str
  onfocus: str
  onhashchange: str
  onlanguagechange: str
  onload: str
  onmessage: str
  onoffline: str
  ononline: str
  onpopstate: str
  onredo: str
  onresize: str
  onstorage: str
  onundo: str
  onunload: str

class ButtonAttrs(GlobalAttrs, total=False):
  autofocus: bool
  disabled: bool
  form: str
  formaction: str
  formenctype: ButtonFormenctypeL
  formmethod: ButtonFormmethodL
  formnovalidate: bool
  formtarget: ButtonFormtargetL
  name: str
  type: ButtonTypeL
  value: str

class CanvasAttrs(GlobalAttrs, total=False):
  height: str
  width: str

class ColAttrs(GlobalAttrs, total=False):
  span: str

class ColgroupAttrs(GlobalAttrs, total=False):
  span: str

class DataAttrs(GlobalAttrs, total=False):
  value: str

class DelAttrs(GlobalAttrs, total=False):
  cite: str
  datetime: str

class DetailsAttrs(GlobalAttrs, total=False):
  open: bool

class DialogAttrs(GlobalAttrs, total=False):
  open: bool

class EmbedAttrs(GlobalAttrs, total=False):
  height: str
  src: str
  type: str
  width: str

class FieldsetAttrs(GlobalAttrs, total=False):
  disabled: bool
  form: str
  name: str

class FormAttrs(GlobalAttrs, total=False):
  accept_charset: str
  action: str
  autocomplete: FormAutocompleteL
  enctype: FormEnctypeL
  method: FormMethodL
  name: str
  novalidate: bool
  rel: FormRelL
  target: FormTargetL

class HtmlAttrs(GlobalAttrs, total=False):
  xmlns: HtmlXmlnsL

class IframeAttrs(GlobalAttrs, total=False):
  allow: str
  allowfullscreen: IframeAllowfullscreenL
  height: str
  loading: IframeLoadingL
  name: str
  referrerpolicy: IframeReferrerpolicyL
  sandbox: IframeSandboxL
  src: str
  srcdoc: str
  width: str

class ImgAttrs(GlobalAttrs, total=False):
  alt: str
  crossorigin: ImgCrossoriginL
  decoding: ImgDecodingL
  fetchpriority: ImgFetchpriorityL
  height: str
  ismap: bool
  loading: ImgLoadingL
  referrerpolicy: ImgReferrerpolicyL
  sizes: str
  src: str
  srcset: str
  usemap: str
  width: str

class InputAttrs(GlobalAttrs, total=False):
  accept: InputAcceptL
  alt: str
  autocomplete: InputAutocompleteL
  autofocus: bool
  capture: str
  checked: bool
  dirname: str
  disabled: bool
  form: str
  formaction: str
  formenctype: InputFormenctypeL
  formmethod: InputFormmethodL
  formnovalidate: bool
  formtarget: InputFormtargetL
  height: str
  list: str
  max: str
  maxlength: str
  min: str
  minlength: str
  multiple: bool
  name: str
  pattern: str
  placeholder: str
  readonly: bool
  required: bool
  size: str
  src: str
  step: str
  type: InputTypeL
  value: str
  width: str

class InsAttrs(GlobalAttrs, total=False):
  cite: str
  datetime: str

class LabelAttrs(GlobalAttrs, total=False):
  for_: str

class LiAttrs(GlobalAttrs, total=False):
  value: str

class LinkAttrs(GlobalAttrs, total=False):
  as_: str
  crossorigin: LinkCrossoriginL
  fetchpriority: str
  href: str
  hreflang: str
  imagesizes: str
  imagesrcset: str
  integrity: str
  media: str
  referrerpolicy: LinkReferrerpolicyL
  rel: LinkRelL
  sizes: str
  type: str

class MapAttrs(GlobalAttrs, total=False):
  name: str

class MetaAttrs(GlobalAttrs, total=False):
  charset: str
  content: str
  http_equiv: MetaHttp_equivL
  name: MetaNameL

class MeterAttrs(GlobalAttrs, total=False):
  form: str
  high: str
  low: str
  max: str
  min: str
  optimum: str
  value: str

class ObjectAttrs(GlobalAttrs, total=False):
  data: str
  form: str
  height: str
  name: str
  type: str
  width: str

class OlAttrs(GlobalAttrs, total=False):
  reversed: bool
  start: str
  type: OlTypeL

class OptgroupAttrs(GlobalAttrs, total=False):
  disabled: bool
  label: str

class OptionAttrs(GlobalAttrs, total=False):
  disabled: bool
  label: str
  selected: bool
  value: str

class OutputAttrs(GlobalAttrs, total=False):
  for_: str
  form: str
  name: str

class ProgressAttrs(GlobalAttrs, total=False):
  max: str
  value: str

class QAttrs(GlobalAttrs, total=False):
  cite: str

class ScriptAttrs(GlobalAttrs, total=False):
  async_: bool
  crossorigin: ScriptCrossoriginL
  defer: bool
  fetchpriority: str
  integrity: str
  nomodule: bool
  nonce: str
  referrerpolicy: ScriptReferrerpolicyL
  src: str
  type: str

class SelectAttrs(GlobalAttrs, total=False):
  autocomplete: SelectAutocompleteL
  autofocus: bool
  disabled: bool
  form: str
  multiple: bool
  name: str
  required: bool
  size: str

class SlotAttrs(GlobalAttrs, total=False):
  name: str

class SourceAttrs(GlobalAttrs, total=False):
  height: str
  media: str
  sizes: str
  src: str
  srcset: str
  type: str
  width: str

class StyleAttrs(GlobalAttrs, total=False):
  blocking: str
  media: str
  nonce: str
  title: str

class TdAttrs(GlobalAttrs, total=False):
  colspan: str
  headers: str
  rowspan: str

class TextareaAttrs(GlobalAttrs, total=False):
  autocomplete: TextareaAutocompleteL
  autofocus: bool
  cols: str
  dirname: str
  disabled: bool
  form: str
  maxlength: str
  minlength: str
  name: str
  placeholder: str
  readonly: bool
  required: bool
  rows: str
  spellcheck: TextareaSpellcheckL
  wrap: TextareaWrapL

class ThAttrs(GlobalAttrs, total=False):
  abbr: str
  colspan: str
  headers: str
  rowspan: str
  scope: ThScopeL

class TimeAttrs(GlobalAttrs, total=False):
  datetime: str

class TrackAttrs(GlobalAttrs, total=False):
  default: bool
  kind: TrackKindL
  label: str
  src: str
  srclang: str

class VideoAttrs(GlobalAttrs, total=False):
  autoplay: bool
  controls: bool
  crossorigin: VideoCrossoriginL
  disableremoteplayback: bool
  loop: bool
  muted: bool
  playsinline: bool
  poster: str
  preload: VideoPreloadL
  src: str
  width: str
