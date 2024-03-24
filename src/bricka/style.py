from typing import Any, Literal, TypedDict

EXTRA_PROPS = {
  "margin-x": [
    ['margin-left', 'margin-right']
  ],
  "margin-y": [
    ['margin-top', 'margin-bottom']
  ],
  "padding-x": [
    ['padding-left', 'padding-right']
  ],
  "padding-y": [
    ['padding-top', 'padding-bottom']
  ],
}

#region Pseudo Classes
PseudoClassL = Literal[
  ":active",
  ":any-link",
  ":checked",
  ":default",
  ":dir",
  ":disabled",
  ":empty",
  ":enabled",
  ":focus",
  ":focus-visible",
  ":focus-within",
  ":fullscreen",
  ":future",
  ":hover",
  ":in-range",
  ":indeterminate",
  ":invalid",
  ":lang",
  ":left",
  ":link",
  ":not",
  ":optional",
  ":out-of-range",
  ":read-only",
  ":read-write",
  ":required",
  ":right",
  ":root",
  ":scope",
  ":target",
  ":valid",
  ":visited",
]
#endregion

#region Sets
BlurSetL = Literal["blur(0)", "blur(4px)", "blur(8px)", "blur(12px)", "blur(16px)", "blur(24px)", "blur(40px)", "blur(64px)"]

BreakSetL = Literal["all", "always", "auto", "avoid", "avoid-column", "avoid-page", "avoid-region", "column", "left", "page", "recto", "region", "right", "verso"]

BrightnessSetL = Literal["brightness(0)", "brightness(.5)", "brightness(.75)", "brightness(.9)", "brightness(.95)", "brightness(1)", "brightness(1.05)", "brightness(1.1)", "brightness(1.25)", "brightness(1.5)", "brightness(2)"]

CaretShapeSetL = Literal["auto", "bar", "block", "underscore"]

ColorSetL = Literal["inherit", "currentcolor", "transparent", "aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]

ContrastSetL = Literal["contrast(0)", "contrast(.5)", "contrast(.75)", "contrast(1)", "contrast(1.25)", "contrast(1.5)", "contrast(2)"]

DropShadowSetL = Literal["0 1px 1px rgb(0 0 0 / 0.05)", "('0 1px 2px rgb(0 0 0 / 0.1)', '0 1px 1px rgb(0 0 0 / 0.06)')", "('0 4px 3px rgb(0 0 0 / 0.07)', '0 2px 2px rgb(0 0 0 / 0.06)')", "('0 10px 8px rgb(0 0 0 / 0.04)', '0 4px 3px rgb(0 0 0 / 0.1)')", "('0 20px 13px rgb(0 0 0 / 0.03)', '0 8px 5px rgb(0 0 0 / 0.08)')", "0 25px 25px rgb(0 0 0 / 0.15)", "0 0 #0000"]

FilterOpacitySetL = Literal["opacity(0)", "opacity(0.05)", "opacity(0.1)", "opacity(0.15)", "opacity(0.2)", "opacity(0.25)", "opacity(0.3)", "opacity(0.35)", "opacity(0.4)", "opacity(0.45)", "opacity(0.5)", "opacity(0.55)", "opacity(0.6)", "opacity(0.65)", "opacity(0.7)", "opacity(0.75)", "opacity(0.8)", "opacity(0.85)", "opacity(0.9)", "opacity(0.95)", "opacity(1)"]

Fraction12SetL = Literal["calc(1 / 12 * 100%)", "calc(2 / 12 * 100%)", "calc(3 / 12 * 100%)", "calc(4 / 12 * 100%)", "calc(5 / 12 * 100%)", "calc(6 / 12 * 100%)", "calc(7 / 12 * 100%)", "calc(8 / 12 * 100%)", "calc(9 / 12 * 100%)", "calc(10 / 12 * 100%)", "calc(11 / 12 * 100%)"]

Fraction2SetL = Literal["calc(1 / 2 * 100%)"]

Fraction3SetL = Literal["calc(1 / 3 * 100%)", "calc(2 / 3 * 100%)"]

Fraction4SetL = Literal["calc(1 / 4 * 100%)", "calc(2 / 4 * 100%)", "calc(3 / 4 * 100%)"]

Fraction5SetL = Literal["calc(1 / 5 * 100%)", "calc(2 / 5 * 100%)", "calc(3 / 5 * 100%)", "calc(4 / 5 * 100%)"]

Fraction6SetL = Literal["calc(1 / 6 * 100%)", "calc(2 / 6 * 100%)", "calc(3 / 6 * 100%)", "calc(4 / 6 * 100%)", "calc(5 / 6 * 100%)"]

GradientColorStopPositionsSetL = Literal["0%", "5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%", "45%", "50%", "55%", "60%", "65%", "70%", "75%", "80%", "85%", "90%", "95%", "100%"]

GrayscaleSetL = Literal["grayscale(0)", "grayscale(100%)"]

HueRotateSetL = Literal["hue-rotate(0deg)", "hue-rotate(15deg)", "hue-rotate(30deg)", "hue-rotate(60deg)", "hue-rotate(90deg)", "hue-rotate(180deg)"]

InvertSetL = Literal["invert(0)", "invert(100%)"]

LineStyleSetL = Literal["dashed", "dotted", "double", "groove", "hidden", "inset", "none", "outset", "ridge", "solid"]

LineWidthSetL = Literal["0px", "1px", "2px", "4px", "8px"]

RadiusSetL = Literal["0px", "0.125rem", "0.25rem", "0.375rem", "0.5rem", "0.75rem", "1rem", "1.5rem", "9999px"]

RotateSetL = Literal["rotate(0deg)", "rotate(1deg)", "rotate(2deg)", "rotate(3deg)", "rotate(6deg)", "rotate(12deg)", "rotate(45deg)", "rotate(90deg)", "rotate(180deg)"]

SaturateSetL = Literal["saturate(0)", "saturate(.5)", "saturate(1)", "saturate(1.5)", "saturate(2)"]

ScaleSetL = Literal["scale(0)", "scale(.5)", "scale(.75)", "scale(.9)", "scale(.95)", "scale(1)", "scale(1.05)", "scale(1.1)", "scale(1.25)", "scale(1.5)"]

ScaleXSetL = Literal["scaleX(0)", "scaleX(.5)", "scaleX(.75)", "scaleX(.9)", "scaleX(.95)", "scaleX(1)", "scaleX(1.05)", "scaleX(1.1)", "scaleX(1.25)", "scaleX(1.5)"]

ScaleYSetL = Literal["scaleY(0)", "scaleY(.5)", "scaleY(.75)", "scaleY(.9)", "scaleY(.95)", "scaleY(1)", "scaleY(1.05)", "scaleY(1.1)", "scaleY(1.25)", "scaleY(1.5)"]

ScreensSetL = Literal["640px", "768px", "1024px", "1280px", "1536px"]

SepiaSetL = Literal["sepia(0)", "sepia(100%)"]

SkewXSetL = Literal["skewX(0deg)", "skewX(1deg)", "skewX(2deg)", "skewX(3deg)", "skewX(6deg)", "skewX(12deg)"]

SkewYSetL = Literal["skewY(0deg)", "skewY(1deg)", "skewY(2deg)", "skewY(3deg)", "skewY(6deg)", "skewY(12deg)"]

SpacingSetL = Literal["1px", "0px", "0.125rem", "0.25rem", "0.375rem", "0.5rem", "0.625rem", "0.75rem", "0.875rem", "1rem", "1.25rem", "1.5rem", "1.75rem", "2rem", "2.25rem", "2.5rem", "2.75rem", "3rem", "3.5rem", "4rem", "5rem", "6rem", "7rem", "8rem", "9rem", "10rem", "11rem", "12rem", "13rem", "14rem", "15rem", "16rem", "18rem", "20rem", "24rem"]

TextDecorationLineSetL = Literal["blink", "grammar-error", "line-through", "none", "overline", "spelling-error", "underline"]

TextDecorationStyleSetL = Literal["dashed", "dotted", "double", "solid", "wavy"]

TextEmphasisStyleSetL = Literal["circle", "dot", "double-circle", "filled", "none", "open", "sesame", "triangle"]

InsetWidthSetL = Literal["auto", SpacingSetL, Fraction2SetL, Fraction3SetL, Fraction4SetL, "100%"]

SizeSetL = Literal["auto", SpacingSetL, Fraction2SetL, Fraction3SetL, Fraction4SetL, Fraction5SetL, Fraction6SetL, Fraction12SetL, "100%", "min-content", "max-content", "fit-content"]

SpacingAutoSetL = Literal["auto", SpacingSetL]

TextDecorationThicknessSetL = Literal["auto", "from-font", LineWidthSetL]

TranslateXSetL = Literal[SpacingSetL, Fraction2SetL, Fraction3SetL, Fraction4SetL, "100%"]

TranslateYSetL = Literal[SpacingSetL, Fraction2SetL, Fraction3SetL, Fraction4SetL, "100%"]

#endregion
#region Rule
Rule = TypedDict("Rule",
  {
    "@media": str,
    ":active": "Rule",
    ":any-link": "Rule",
    ":checked": "Rule",
    ":default": "Rule",
    ":dir": "Rule",
    ":disabled": "Rule",
    ":empty": "Rule",
    ":enabled": "Rule",
    ":focus": "Rule",
    ":focus-visible": "Rule",
    ":focus-within": "Rule",
    ":fullscreen": "Rule",
    ":future": "Rule",
    ":hover": "Rule",
    ":in-range": "Rule",
    ":indeterminate": "Rule",
    ":invalid": "Rule",
    ":lang": "Rule",
    ":left": "Rule",
    ":link": "Rule",
    ":not": "Rule",
    ":optional": "Rule",
    ":out-of-range": "Rule",
    ":read-only": "Rule",
    ":read-write": "Rule",
    ":required": "Rule",
    ":right": "Rule",
    ":root": "Rule",
    ":scope": "Rule",
    ":target": "Rule",
    ":valid": "Rule",
    ":visited": "Rule",

    "accent-color": Literal[ColorSetL, "auto"] | Any,

    "align-content": Literal["baseline", "center", "end", "flex-end", "flex-start", "normal", "space-around", "space-between", "space-evenly", "start", "stretch"],

    "align-items": Literal["baseline", "center", "end", "flex-end", "flex-start", "normal", "self-end", "self-start", "start", "stretch"],

    "align-self": Literal["auto", "baseline", "center", "end", "flex-end", "flex-start", "normal", "self-end", "self-start", "start", "stretch"],

    "all": Literal["inherit", "initial", "unset"],

    "animation": Literal["spin 1s linear infinite", "ping 1s cubic-bezier(0, 0, 0.2, 1) infinite", "pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite"],

    "animation-delay": str,

    "animation-direction": str,

    "animation-duration": str,

    "animation-fill-mode": str,

    "animation-iteration-count": str,

    "animation-name": str,

    "animation-play-state": str,

    "animation-timing-function": str,

    "backdrop-filter": Literal[BlurSetL, BrightnessSetL, ContrastSetL, GrayscaleSetL, HueRotateSetL, InvertSetL, FilterOpacitySetL, SaturateSetL, SepiaSetL],

    "backface-visibility": Literal["hidden", "visible"],

    "background": ColorSetL,

    "background-attachment": Literal["fixed", "local", "scroll"],

    "background-blend-mode": Literal["color", "color-burn", "color-dodge", "darken", "difference", "exclusion", "hard-light", "hue", "lighten", "luminosity", "multiply", "normal", "overlay", "saturation", "screen", "soft-light"],

    "background-clip": Literal["border-box", "content-box", "padding-box", "text"],

    "background-color": ColorSetL | Any,

    "background-image": Literal["none"],

    "background-origin": Literal["border-box", "content-box", "padding-box"],

    "background-position": Literal["bottom", "center", "left", "left bottom", "left top", "right", "right bottom", "right top", "top"],

    "background-repeat": Literal["no-repeat", "repeat", "repeat-x", "repeat-y", "round", "space"],

    "background-size": Literal["auto", "cover", "contain"],

    "block-size": SizeSetL,

    "border": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-block": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-block-color": ColorSetL | Any,

    "border-block-end": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-block-end-color": ColorSetL | Any,

    "border-block-end-style": LineStyleSetL,

    "border-block-end-width": LineWidthSetL,

    "border-block-start": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-block-start-color": ColorSetL | Any,

    "border-block-start-style": LineStyleSetL,

    "border-block-start-width": LineWidthSetL,

    "border-block-style": LineStyleSetL,

    "border-block-width": LineWidthSetL,

    "border-bottom": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-bottom-color": ColorSetL | Any,

    "border-bottom-left-radius": RadiusSetL,

    "border-bottom-right-radius": RadiusSetL,

    "border-bottom-style": LineStyleSetL,

    "border-bottom-width": LineWidthSetL,

    "border-collapse": Literal["collapse", "separate"],

    "border-color": ColorSetL | Any,

    "border-end-end-radius": RadiusSetL,

    "border-end-start-radius": RadiusSetL,

    "border-image": str,

    "border-image-outset": SpacingSetL,

    "border-image-repeat": Literal["repeat", "round", "space", "stretch"],

    "border-image-slice": Literal["fill"],

    "border-image-source": str,

    "border-image-width": Literal["auto"],

    "border-inline": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-inline-color": ColorSetL | Any,

    "border-inline-end": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-inline-end-color": ColorSetL | Any,

    "border-inline-end-style": LineStyleSetL,

    "border-inline-end-width": LineWidthSetL,

    "border-inline-start": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-inline-start-color": ColorSetL | Any,

    "border-inline-start-style": LineStyleSetL,

    "border-inline-start-width": LineWidthSetL,

    "border-inline-style": LineStyleSetL,

    "border-inline-width": LineWidthSetL,

    "border-left": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-left-color": ColorSetL | Any,

    "border-left-style": LineStyleSetL,

    "border-left-width": LineWidthSetL,

    "border-radius": RadiusSetL,

    "border-right": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-right-color": ColorSetL | Any,

    "border-right-style": LineStyleSetL,

    "border-right-width": LineWidthSetL,

    "border-spacing": SpacingSetL,

    "border-start-end-radius": RadiusSetL,

    "border-start-start-radius": RadiusSetL,

    "border-style": LineStyleSetL,

    "border-top": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "border-top-color": ColorSetL | Any,

    "border-top-left-radius": RadiusSetL,

    "border-top-right-radius": RadiusSetL,

    "border-top-style": LineStyleSetL,

    "border-top-width": LineWidthSetL,

    "border-width": LineWidthSetL,

    "bottom": InsetWidthSetL,

    "box-decoration-break": Literal["clone", "slice"],

    "box-shadow": Literal["0 1px 2px 0 rgb(0 0 0 / 0.05)", "0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)", "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)", "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)", "0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)", "0 25px 50px -12px rgb(0 0 0 / 0.25)", "inset 0 2px 4px 0 rgb(0 0 0 / 0.05)", "none"],

    "box-sizing": Literal["border-box", "content-box"],

    "break-after": BreakSetL,

    "break-before": BreakSetL,

    "break-inside": Literal["auto", "avoid", "avoid-column", "avoid-page", "avoid-region"],

    "caption-side": Literal["block-end", "block-start", "bottom", "inline-end", "inline-start", "top"],

    "caret": tuple[ColorSetL | Any, CaretShapeSetL],

    "caret-color": ColorSetL | Any,

    "caret-shape": CaretShapeSetL,

    "clear": Literal["both", "inline-end", "inline-start", "left", "none", "right"],

    "clip": str,

    "clip-path": str,

    "color": ColorSetL | Any,

    "color-scheme": Literal["dark", "light", "light dark", "normal"],

    "column-count": Literal["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],

    "column-fill": Literal["auto", "balance", "balance-all"],

    "column-gap": Literal["normal", SpacingSetL],

    "column-rule": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "column-rule-color": ColorSetL | Any,

    "column-rule-style": LineStyleSetL,

    "column-rule-width": LineWidthSetL,

    "column-span": Literal["all", "none"],

    "column-width": Literal["auto", "16rem", "18rem", "20rem", "24rem", "28rem", "32rem", "36rem", "42rem", "48rem", "56rem", "64rem", "72rem", "80rem"],

    "columns": Literal["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "16rem", "18rem", "20rem", "24rem", "28rem", "32rem", "36rem", "42rem", "48rem", "56rem", "64rem", "72rem", "80rem"],

    "contain": Literal["content", "none", "strict"],

    "contain-intrinsic-block-size": str,

    "contain-intrinsic-height": SizeSetL,

    "contain-intrinsic-inline-size": SizeSetL,

    "contain-intrinsic-size": SizeSetL,

    "contain-intrinsic-width": SizeSetL,

    "container": str,

    "container-name": str,

    "container-type": str,

    "content": Literal["none"],

    "content-visibility": Literal["visible", "auto", "hidden"],

    "counter-increment": str,

    "counter-reset": str,

    "counter-set": str,

    "cursor": Literal["alias", "all-scroll", "auto", "cell", "col-resize", "context-menu", "copy", "crosshair", "default", "e-resize", "ew-resize", "grab", "grabbing", "help", "move", "n-resize", "ne-resize", "nesw-resize", "no-drop", "none", "not-allowed", "ns-resize", "nw-resize", "nwse-resize", "pointer", "progress", "row-resize", "s-resize", "se-resize", "sw-resize", "text", "vertical-text", "w-resize", "wait", "zoom-in", "zoom-out"],

    "direction": Literal["ltr", "rtl"],

    "display": Literal["block", "contents", "flex", "flow", "flow-root", "grid", "inline", "inline-block", "inline-flex", "inline-grid", "inline-list-item", "inline-table", "list-item", "none", "table", "table-caption", "table-cell", "table-column", "table-column-group", "table-footer-group", "table-header-group", "table-row", "table-row-group"],

    "empty-cells": Literal["hide", "show"],

    "filter": Literal[BlurSetL, BrightnessSetL, ContrastSetL, GrayscaleSetL, HueRotateSetL, InvertSetL, FilterOpacitySetL, SaturateSetL, SepiaSetL],

    "flex": Literal["content", "fit-content", "max-content", "min-content", "none", "1 1 0%", "1 1 auto", "0 1 auto"],

    "flex-basis": Literal["auto", SpacingSetL, Fraction2SetL, Fraction3SetL, Fraction4SetL, Fraction5SetL, Fraction6SetL, Fraction12SetL, "100%"],

    "flex-direction": Literal["column", "column-reverse", "row", "row-reverse"],

    "flex-flow": Literal["column", "column-reverse", "nowrap", "row", "row-reverse", "wrap", "wrap-reverse"],

    "flex-grow": Literal["0", "1"],

    "flex-shrink": Literal["0", "1"],

    "flex-wrap": Literal["nowrap", "wrap", "wrap-reverse"],

    "float": Literal["inline-end", "inline-start", "left", "none", "right"],

    "font": str,

    "font-family": Literal["('ui-sans-serif', 'system-ui', 'sans-serif', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji')", "('ui-serif', 'Georgia', 'Cambria', 'Times New Roman', 'Times', 'serif')", "('ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', 'monospace')"] | Any,

    "font-feature-settings": Literal["normal"],

    "font-kerning": Literal["auto", "none", "normal"],

    "font-language-override": Literal["normal"],

    "font-optical-sizing": Literal["auto", "none"],

    "font-palette": Literal["dark", "light", "normal"],

    "font-size": Literal["0.75rem", "0.875rem", "1rem", "1.125rem", "1.25rem", "1.5rem", "1.875rem", "2.25rem", "3rem", "3.75rem", "4.5rem", "6rem", "8rem"],

    "font-size-adjust": Literal["from-font", "none"],

    "font-stretch": Literal["condensed", "expanded", "extra-condensed", "extra-expanded", "normal", "semi-condensed", "semi-expanded", "ultra-condensed", "ultra-expanded"],

    "font-style": Literal["italic", "normal"],

    "font-synthesis": Literal["none", "position", "small-caps", "style", "weight"],

    "font-synthesis-small-caps": Literal["auto", "none"],

    "font-synthesis-style": Literal["auto", "none"],

    "font-synthesis-weight": Literal["auto", "none"],

    "font-variant": str,

    "font-variant-alternates": str,

    "font-variant-caps": Literal["all-petite-caps", "all-small-caps", "normal", "petite-caps", "small-caps", "titling-caps", "unicase"],

    "font-variant-east-asian": Literal["full-width", "jis04", "jis78", "jis83", "jis90", "normal", "proportional-width", "ruby", "simplified", "traditional"],

    "font-variant-emoji": Literal["emoji", "normal", "text", "unicode"],

    "font-variant-ligatures": Literal["common-ligatures", "contextual", "discretionary-ligatures", "historical-ligatures", "no-common-ligatures", "no-contextual", "no-discretionary-ligatures", "no-historical-ligatures", "none", "normal"],

    "font-variant-numeric": Literal["diagonal-fractions", "lining-nums", "normal", "oldstyle-nums", "ordinal", "proportional-nums", "slashed-zero", "stacked-fractions", "tabular-nums"],

    "font-variant-position": Literal["normal", "sub", "super"],

    "font-variation-settings": str,

    "font-weight": Literal["100", "200", "300", "400", "500", "600", "700", "800", "900"],

    "gap": SpacingSetL,

    "grid": str,

    "grid-area": Literal["auto", "span"],

    "grid-auto-columns": Literal["auto", "min-content", "max-content", "minmax(0, 1fr)"],

    "grid-auto-flow": Literal["column", "dense", "row"],

    "grid-auto-rows": Literal["auto", "min-content", "max-content", "minmax(0, 1fr)"],

    "grid-column": Literal["auto", "span 1 / span 1", "span 2 / span 2", "span 3 / span 3", "span 4 / span 4", "span 5 / span 5", "span 6 / span 6", "span 7 / span 7", "span 8 / span 8", "span 9 / span 9", "span 10 / span 10", "span 11 / span 11", "span 12 / span 12", "1 / -1"],

    "grid-column-end": Literal["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"],

    "grid-column-start": Literal["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"],

    "grid-row": Literal["auto", "span 1 / span 1", "span 2 / span 2", "span 3 / span 3", "span 4 / span 4", "span 5 / span 5", "span 6 / span 6", "span 7 / span 7", "span 8 / span 8", "span 9 / span 9", "span 10 / span 10", "span 11 / span 11", "span 12 / span 12", "1 / -1"],

    "grid-row-end": Literal["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"],

    "grid-row-start": Literal["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"],

    "grid-template": str,

    "grid-template-areas": Literal["none"],

    "grid-template-columns": Literal["none", "subgrid", "repeat(1, minmax(0, 1fr))", "repeat(2, minmax(0, 1fr))", "repeat(3, minmax(0, 1fr))", "repeat(4, minmax(0, 1fr))", "repeat(5, minmax(0, 1fr))", "repeat(6, minmax(0, 1fr))", "repeat(7, minmax(0, 1fr))", "repeat(8, minmax(0, 1fr))", "repeat(9, minmax(0, 1fr))", "repeat(10, minmax(0, 1fr))", "repeat(11, minmax(0, 1fr))", "repeat(12, minmax(0, 1fr))"],

    "grid-template-rows": Literal["none", "subgrid", "repeat(1, minmax(0, 1fr))", "repeat(2, minmax(0, 1fr))", "repeat(3, minmax(0, 1fr))", "repeat(4, minmax(0, 1fr))", "repeat(5, minmax(0, 1fr))", "repeat(6, minmax(0, 1fr))", "repeat(7, minmax(0, 1fr))", "repeat(8, minmax(0, 1fr))", "repeat(9, minmax(0, 1fr))", "repeat(10, minmax(0, 1fr))", "repeat(11, minmax(0, 1fr))", "repeat(12, minmax(0, 1fr))"],

    "hanging-punctuation": Literal["allow-end", "first", "force-end", "last", "none"],

    "height": Literal["auto", SpacingSetL, Fraction2SetL, Fraction3SetL, Fraction4SetL, Fraction5SetL, Fraction6SetL, "100%", "100vh", "100svh", "100lvh", "100dvh", "min-content", "max-content", "fit-content"],

    "hyphenate-character": Literal["auto"],

    "hyphenate-limit-chars": Literal["auto"],

    "hyphens": Literal["auto", "manual", "none"],

    "image-orientation": Literal["flip", "from-image"],

    "image-rendering": Literal["auto", "crisp-edges", "pixelated"],

    "inline-size": Literal["auto", "fit-content", "max-content", "min-content"],

    "input-security": Literal["auto", "none"],

    "inset": InsetWidthSetL,

    "inset-block": InsetWidthSetL,

    "inset-block-end": InsetWidthSetL,

    "inset-block-start": InsetWidthSetL,

    "inset-inline": InsetWidthSetL,

    "inset-inline-end": InsetWidthSetL,

    "inset-inline-start": InsetWidthSetL,

    "isolation": Literal["auto", "isolate"],

    "justify-content": Literal["center", "end", "flex-end", "flex-start", "left", "normal", "right", "space-around", "space-between", "space-evenly", "start", "stretch"],

    "justify-items": Literal["baseline", "center", "end", "flex-end", "flex-start", "left", "legacy", "normal", "right", "self-end", "self-start", "start", "stretch"],

    "justify-self": Literal["auto", "baseline", "center", "end", "flex-end", "flex-start", "left", "normal", "right", "self-end", "self-start", "start", "stretch"],

    "left": InsetWidthSetL,

    "letter-spacing": Literal["-0.05em", "-0.025em", "0em", "0.025em", "0.05em", "0.1em", "normal"],

    "line-break": Literal["anywhere", "auto", "loose", "normal", "strict"],

    "line-height": Literal["1", "1.25", "1.375", "1.5", "1.625", "2", ".75rem", "1rem", "1.25rem", "1.5rem", "1.75rem", "2rem", "2.25rem", "2.5rem"],

    "list-style": str,

    "list-style-image": Literal["none"],

    "list-style-position": Literal["inside", "outside"],

    "list-style-type": Literal["none", "disc", "decimal", "square"],

    "margin": SpacingAutoSetL,

    "margin-block": SpacingAutoSetL,

    "margin-block-end": SpacingAutoSetL,

    "margin-block-start": SpacingAutoSetL,

    "margin-bottom": SpacingAutoSetL,

    "margin-inline": SpacingAutoSetL,

    "margin-inline-end": SpacingAutoSetL,

    "margin-inline-start": SpacingAutoSetL,

    "margin-left": SpacingAutoSetL,

    "margin-right": SpacingAutoSetL,

    "margin-top": SpacingAutoSetL,

    "margin-x": SpacingAutoSetL | Any,

    "margin-y": SpacingAutoSetL | Any,

    "mask": str,

    "mask-border": str,

    "mask-border-mode": Literal["alpha", "luminance"],

    "mask-border-outset": SpacingSetL,

    "mask-border-repeat": Literal["repeat", "round", "space", "stretch"],

    "mask-border-slice": Literal["fill"],

    "mask-border-source": str,

    "mask-border-width": LineWidthSetL,

    "mask-clip": Literal["border-box", "content-box", "fill-box", "margin-box", "no-clip", "padding-box", "stroke-box", "view-box"],

    "mask-composite": Literal["add", "exclude", "intersect", "subtract"],

    "mask-image": str,

    "mask-mode": Literal["alpha", "luminance", "match-source"],

    "mask-origin": Literal["border-box", "content-box", "fill-box", "margin-box", "padding-box", "stroke-box", "view-box"],

    "mask-position": Literal["bottom", "center", "left", "right", "top"],

    "mask-repeat": Literal["no-repeat", "repeat", "repeat-x", "repeat-y", "round", "space"],

    "mask-size": Literal["auto", "contain", "cover"],

    "mask-type": Literal["alpha", "luminance"],

    "math-depth": Literal["auto-add"],

    "math-shift": Literal["compact", "normal"],

    "math-style": Literal["compact", "normal"],

    "max-block-size": SizeSetL,

    "max-height": Literal[SpacingSetL, "none", "100%", "100vh", "100svh", "100lvh", "100dvh", "min-content", "max-content", "fit-content"],

    "max-inline-size": SizeSetL,

    "max-width": Literal[SpacingSetL, "none", "20rem", "24rem", "28rem", "32rem", "36rem", "42rem", "48rem", "56rem", "64rem", "72rem", "80rem", "100%", "min-content", "max-content", "fit-content", "65ch", ScreensSetL],

    "min-block-size": SizeSetL,

    "min-height": Literal[SpacingSetL, "100%", "100vh", "100svh", "100lvh", "100dvh", "min-content", "max-content", "fit-content"],

    "min-inline-size": SizeSetL,

    "min-width": Literal[SpacingSetL, "100%", "min-content", "max-content", "fit-content"],

    "mix-blend-mode": Literal["color", "color-burn", "color-dodge", "darken", "difference", "exclusion", "hard-light", "hue", "lighten", "luminosity", "multiply", "normal", "overlay", "plus-lighter", "saturation", "screen", "soft-light"],

    "object-fit": Literal["contain", "cover", "fill", "none", "scale-down"],

    "object-position": Literal["bottom", "center", "left", "left bottom", "left top", "right", "right bottom", "right top", "top"],

    "offset": str,

    "offset-anchor": Literal["auto", "bottom", "center", "left", "right", "top"],

    "offset-distance": SpacingSetL,

    "offset-path": str,

    "offset-rotate": Literal["auto", "reverse"],

    "opacity": Literal["0", "0.05", "0.1", "0.15", "0.2", "0.25", "0.3", "0.35", "0.4", "0.45", "0.5", "0.55", "0.6", "0.65", "0.7", "0.75", "0.8", "0.85", "0.9", "0.95", "1"],

    "order": Literal["-9999", "9999", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],

    "orphans": str,

    "outline": tuple[LineWidthSetL, LineStyleSetL, ColorSetL | Any],

    "outline-color": ColorSetL | Any,

    "outline-offset": LineWidthSetL,

    "outline-style": LineStyleSetL,

    "outline-width": LineWidthSetL,

    "overflow": Literal["auto", "clip", "hidden", "scroll", "visible"],

    "overflow-anchor": Literal["auto", "none"],

    "overflow-block": Literal["auto", "clip", "hidden", "scroll", "visible"],

    "overflow-clip-margin": Literal["border-box", "content-box", "padding-box"],

    "overflow-inline": Literal["auto", "clip", "hidden", "scroll", "visible"],

    "overflow-wrap": Literal["anywhere", "break-word", "normal"],

    "overflow-x": Literal["auto", "clip", "hidden", "scroll", "visible"],

    "overflow-y": Literal["auto", "clip", "hidden", "scroll", "visible"],

    "overscroll-behavior": Literal["auto", "contain", "none"],

    "overscroll-behavior-block": Literal["auto", "contain", "none"],

    "overscroll-behavior-inline": Literal["auto", "contain", "none"],

    "overscroll-behavior-x": Literal["auto", "contain", "none"],

    "overscroll-behavior-y": Literal["auto", "contain", "none"],

    "padding": SpacingSetL,

    "padding-block": SpacingSetL,

    "padding-block-end": SpacingSetL,

    "padding-block-start": SpacingSetL,

    "padding-bottom": SpacingSetL,

    "padding-inline": SpacingSetL,

    "padding-inline-end": SpacingSetL,

    "padding-inline-start": SpacingSetL,

    "padding-left": SpacingSetL,

    "padding-right": SpacingSetL,

    "padding-top": SpacingSetL,

    "padding-x": SpacingSetL | Any,

    "padding-y": SpacingSetL | Any,

    "page": str,

    "page-break-after": Literal["always", "auto", "avoid", "left", "recto", "right", "verso"],

    "page-break-before": Literal["always", "auto", "avoid", "left", "recto", "right", "verso"],

    "page-break-inside": Literal["auto", "avoid"],

    "paint-order": Literal["fill", "markers", "normal", "stroke"],

    "perspective": str,

    "perspective-origin": Literal["bottom", "center", "left", "right", "top"],

    "place-content": Literal["baseline", "center", "end", "flex-end", "flex-start", "normal", "space-around", "space-between", "space-evenly", "start", "stretch"],

    "place-items": Literal["baseline", "center", "end", "flex-end", "flex-start", "normal", "self-end", "self-start", "start", "stretch"],

    "place-self": Literal["auto", "baseline", "center", "end", "flex-end", "flex-start", "normal", "self-end", "self-start", "start", "stretch"],

    "pointer-events": Literal["auto", "fill", "none", "stroke"],

    "position": Literal["absolute", "fixed", "relative", "static", "sticky"],

    "print-color-adjust": Literal["economy", "exact"],

    "quotes": Literal["auto", "none"],

    "resize": Literal["block", "both", "horizontal", "inline", "none", "vertical"],

    "right": InsetWidthSetL,

    "rotate": RotateSetL,

    "row-gap": Literal[SpacingSetL, "normal"],

    "scale": ScaleSetL,

    "scroll-behavior": Literal["auto", "smooth"],

    "scroll-margin": SpacingSetL,

    "scroll-margin-block": SpacingSetL,

    "scroll-margin-block-end": SpacingSetL,

    "scroll-margin-block-start": SpacingSetL,

    "scroll-margin-bottom": SpacingSetL,

    "scroll-margin-inline": SpacingSetL,

    "scroll-margin-inline-end": SpacingSetL,

    "scroll-margin-inline-start": SpacingSetL,

    "scroll-margin-left": SpacingSetL,

    "scroll-margin-right": SpacingSetL,

    "scroll-margin-top": SpacingSetL,

    "scroll-padding": SpacingSetL,

    "scroll-padding-block": Literal[SpacingSetL, "auto"],

    "scroll-padding-block-end": Literal[SpacingSetL, "auto"],

    "scroll-padding-block-start": Literal[SpacingSetL, "auto"],

    "scroll-padding-bottom": Literal[SpacingSetL, "auto"],

    "scroll-padding-inline": Literal[SpacingSetL, "auto"],

    "scroll-padding-inline-end": Literal[SpacingSetL, "auto"],

    "scroll-padding-inline-start": Literal[SpacingSetL, "auto"],

    "scroll-padding-left": Literal[SpacingSetL, "auto"],

    "scroll-padding-right": Literal[SpacingSetL, "auto"],

    "scroll-padding-top": Literal[SpacingSetL, "auto"],

    "scroll-snap-align": Literal["center", "end", "none", "start"],

    "scroll-snap-stop": Literal["always", "normal"],

    "scroll-snap-type": Literal["block", "both", "inline", "none", "x", "y"],

    "scrollbar-color": ColorSetL | Any,

    "scrollbar-gutter": Literal["auto", "both-edges", "stable"],

    "scrollbar-width": Literal["auto", "none", "thin"],

    "shape-image-threshold": str,

    "shape-margin": SpacingSetL,

    "shape-outside": str,

    "tab-size": str,

    "table-layout": Literal["auto", "fixed"],

    "text-align": Literal["center", "end", "justify", "left", "match-parent", "right", "start"],

    "text-align-last": Literal["auto", "center", "end", "justify", "left", "right", "start"],

    "text-combine-upright": Literal["all", "digits", "none"],

    "text-decoration": tuple[TextDecorationLineSetL, TextDecorationStyleSetL, TextDecorationThicknessSetL, ColorSetL | Any],

    "text-decoration-color": ColorSetL | Any,

    "text-decoration-line": TextDecorationLineSetL,

    "text-decoration-skip-ink": Literal["all", "auto", "none"],

    "text-decoration-style": TextDecorationStyleSetL,

    "text-decoration-thickness": TextDecorationThicknessSetL,

    "text-emphasis": tuple[TextEmphasisStyleSetL, ColorSetL | Any],

    "text-emphasis-color": ColorSetL | Any,

    "text-emphasis-position": Literal["left", "over", "right", "under"],

    "text-emphasis-style": TextEmphasisStyleSetL,

    "text-indent": SpacingSetL,

    "text-justify": Literal["auto", "inter-character", "inter-word", "none"],

    "text-orientation": Literal["mixed", "sideways", "upright"],

    "text-overflow": Literal["clip", "ellipsis"],

    "text-rendering": Literal["auto", "geometricPrecision", "optimizeLegibility", "optimizeSpeed"],

    "text-shadow": Literal["none"],

    "text-transform": Literal["capitalize", "lowercase", "none", "uppercase"],

    "text-underline-offset": Literal["auto", LineWidthSetL],

    "text-underline-position": Literal["auto", "from-font", "left", "right", "under"],

    "text-wrap": Literal["balance", "nowrap", "pretty", "stable", "wrap"],

    "top": InsetWidthSetL,

    "touch-action": Literal["auto", "manipulation", "none", "pan-down", "pan-left", "pan-right", "pan-up", "pan-x", "pan-y", "pinch-zoom"],

    "transform": Literal[RotateSetL, ScaleSetL, ScaleXSetL, ScaleYSetL, SkewXSetL, SkewYSetL, TranslateXSetL, TranslateYSetL],

    "transform-box": Literal["border-box", "content-box", "fill-box", "stroke-box", "view-box"],

    "transform-origin": Literal["center", "top", "top right", "right", "bottom right", "bottom", "bottom left", "left", "top left"],

    "transform-style": Literal["flat", "preserve-3d"],

    "transition": Literal["none"],

    "transition-delay": Literal["0s", "75ms", "100ms", "150ms", "200ms", "300ms", "500ms", "700ms", "1000ms"],

    "transition-duration": Literal["150ms", "0s", "75ms", "100ms", "150ms", "200ms", "300ms", "500ms", "700ms", "1000ms"],

    "transition-property": Literal["none", "all", "color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter", "color, background-color, border-color, text-decoration-color, fill, stroke", "opacity", "box-shadow", "transform"],

    "transition-timing-function": Literal["cubic-bezier(0.4, 0, 0.2, 1)", "linear", "cubic-bezier(0.4, 0, 1, 1)", "cubic-bezier(0, 0, 0.2, 1)", "cubic-bezier(0.4, 0, 0.2, 1)"],

    "translate": SizeSetL,

    "unicode-bidi": Literal["bidi-override", "embed", "isolate", "isolate-override", "normal", "plaintext"],

    "user-select": Literal["all", "auto", "contain", "none", "text"],

    "vertical-align": Literal["baseline", "bottom", "middle", "sub", "super", "text-bottom", "text-top", "top"],

    "visibility": Literal["collapse", "hidden", "visible"],

    "white-space": Literal["break-spaces", "normal", "nowrap", "pre", "pre-line", "pre-wrap"],

    "white-space-collapse": Literal["break-spaces", "collapse", "discard", "preserve", "preserve-breaks", "preserve-spaces"],

    "widows": str,

    "width": Literal["auto", SpacingSetL, Fraction2SetL, Fraction3SetL, Fraction4SetL, Fraction5SetL, Fraction6SetL, Fraction12SetL, "100%", "100vw", "100svw", "100lvw", "100dvw", "min-content", "max-content", "fit-content"],

    "will-change": Literal["auto", "scroll-position", "contents", "transform"],

    "word-break": Literal["break-all", "break-word", "keep-all", "normal"],

    "word-spacing": Literal["normal"],

    "word-wrap": Literal["break-word", "normal"],

    "writing-mode": Literal["horizontal-tb", "sideways-lr", "sideways-rl", "vertical-lr", "vertical-rl"],

    "z-index": Literal["auto", "0", "10", "20", "30", "40", "50"],

  },
  total=False
)

Style = dict[str, Rule]
#endregion
