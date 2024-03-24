import pytest
from bricka.style import Style
from bricka.stylesheet import StyleSheet
from bricka.node import Element

sheet = StyleSheet()

class TestRuleNormalizing():
  def test_normalizing_a_rule_with_default_media(self):
    style: Style = {
      "rule": {
        "color": "black",
        "background-color": "white",
        ":hover": {
          "background-color": "blue"
        }
      }
    }

    assert sheet._normalize(style["rule"]) == {
      # "": {
        "@media": "",
        "color": "black",
        "background-color": "white", 
        "background-color:hover": "blue", 
      # }
    }

    assert list(sheet._normalize(style["rule"]).keys()) == [
      "@media",
      "color", 
      "background-color", 
      "background-color:hover"
    ]

  def test_normalizing_a_rule_with_media(self):
    style: Style = {
      "rule": {
        "@media": "(min-width: 700px)",
        "color": "black",
        "background-color": "white",
        ":hover": {
          "@media": "(max-width: 1200px)", # Child media is ignored
          "background-color": "blue"
        }
      }
    }

    assert sheet._normalize(style["rule"]) == {
      # "(min-width: 700px)": {
        "@media": "(min-width: 700px)",
        "background-color": "white", 
        "background-color:hover": "blue", 
        "color": "black"
      # }
    }

  def test_normalizing_a_simple_pseudo_class(self):
    style: Style = {
      "rule": {
        ":hover": {
          "background-color": "black"
        }
      }
    }

    assert sheet._normalize_pseudo_class(":hover", style["rule"][":hover"]) == {"background-color:hover": "black"}

  def test_normalizing_nested_pseudo_classes(self):
    style: Style = {
      "rule": {
        ":hover": {
          "background-color": "black",
          ":disabled": {
            "color": "white"
          }
        }
      }
    }

    assert sheet._normalize_pseudo_class(":hover", style["rule"][":hover"]) == {
      "background-color:hover": "black", 
      "color:hover:disabled": "white"
    }

  def test_normalizing_deeply_nested_pseudo_classes(self):
    style: Style = {
      "rule": {
        ":hover": {
          "background-color": "black",
          ":disabled": {
            "color": "white",
            ":active": {
              "border-style": "solid"
            }
          }
        }
      }
    }

    normalized = sheet._normalize_pseudo_class(":hover", style["rule"][":hover"])

    assert normalized == {
      "background-color:hover": "black", 
      "color:hover:disabled": "white",
      "border-style:hover:disabled:active": "solid"
    }

    assert list(normalized.keys()) == [
      "background-color:hover", 
      "color:hover:disabled", 
      "border-style:hover:disabled:active"
    ]

class TestRuleMerging():
  def test_merging_two_rules(self):
    style: Style = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      }
    }

    s = StyleSheet(style["rule1"], style["rule2"])
    
    # assert sheet.merge(style["rule1"], style["rule2"]) == {
    assert s.raw_style() == {
      "": {
        "background-color": "blue", 
        "color": "black",
        "background-color:hover": "red", 
      }
    }    

    # assert list(sheet.merge(style["rule1"], style["rule2"])[""].keys()) == [
    assert list(s.raw_style()[""].keys()) == [
      "color", 
      "background-color", 
      "background-color:hover",
    ]
  def test_merging_two_rules_with_different_media(self):
    style: Style = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "@media": "min-width(700px)",
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      }
    }

    assert sheet._merge(style["rule1"], style["rule2"]) == {
      "": {
        "background-color": "white", 
        "color": "black",
        "background-color:hover": "blue", 
      },
      "min-width(700px)": {
        "background-color": "blue", 
        "background-color:hover": "red"
      }
    }    
    
class TestPropResolution():    
  def test_counting_conflicts_with_empty_conflicts(self):
    # Returns -1, as the prop is not present in the conflicts
    conflicts = {
    } 
    layer = sheet._conflict_count("border-color", conflicts)

    assert layer == -1

  def test_counting_conflicts_with_a_non_conflicting_prop(self):
    # Returns the conflicting count of the prop
    conflicts = {
      'color': 0,
      'color$': 2,
    } 

    # rule = CssRule()
    assert sheet._conflict_count("color", conflicts) == 2

  def test_counting_conflicts_with_a_conflicting_prop(self):
    # Returns the max count of all conflicting props
    conflicts = {
      'border-color': 0, 
      'border-color$': 0,
      'border-bottom-color$': 0, 
      'border-left-color$': 3, 
      'border-right-color$': 1, 
      'border-top-color$': 0, 
      'border-top-style$': 10, 
      'color': 6,
    } 
    # rule = CssRule()
    count = sheet._conflict_count("border-color", conflicts)

    assert count == 3 

  def test_resolving_conflicts(self):
    # Updates the conflicts dict for all conflicting props
    conflicts = {
      'border-color': 0, 
      'border-color$': 0,
      'border-bottom-color$': 0, 
      'border-left-color$': 3, 
      'border-right-color$': 1, 
      'border-top-color$': 0, 
      'border-top-style$': 10, 
      'color': 6,
    } 
    # rule = CssRule()
    sheet._resolve("border-color", conflicts)

    assert conflicts == {
      'border-color': 4, 
      'border-color$': 4,
      'border-bottom-color$': 4, 
      'border-left-color$': 4, 
      'border-right-color$': 4, 
      'border-top-color$': 4, 
      'border-top-style$': 10, 
      'color': 6,
    }

    sheet._resolve("border-top-color", conflicts)

    assert conflicts == {
      'border-color': 4, 
      'border-color$': 4,
      'border-top-color': 5, 
      'border-bottom-color$': 4, 
      'border-left-color$': 4, 
      'border-right-color$': 4, 
      'border-top-color$': 5, 
      'border-top-style$': 10, 
      'color': 6,
    }

class TestRuleLayers():    
  def test_calling_rule_layers_with_non_conflicting_props(self):
    # Returns all the props within the same layer
    style: Style = {
      "rule1": {
        "border-width": "1px",
        "border-style": "solid",
      },
      "rule2": {        
        "border-width": "2px",
      }
    }

    sheet = StyleSheet(style["rule1"], style["rule2"])

    assert sheet.media_layers() == {
      "": [{ # Single layer
        "f900f0eb": "border-width: 2px;", 
        "f594b855": "border-style: solid;"
      }]
    }

  def test_calling_rule_layers_with_non_conflicting_props_and_media(self):
    # Returns all the props within the same layer
    style: Style = {
      "rule1": {
        "border-width": "1px",
        "border-style": "solid",
      },
      "rule2": {       
        "@media": "media", 
        "border-width": "2px",
      }
    }

    sheet = StyleSheet(style["rule1"], style["rule2"])

    assert sheet.media_layers() == {
      "": [
        {
          "f8d6e0e8": "border-width: 1px;", 
          "f594b855": "border-style: solid;"
        }
      ],
      "media": [
        {
          "f9d6586b": "border-width: 2px;"
        }
      ]
    }

  def test_calling_rule_layers_with_conflicting_props(self):
    # Returns the conflicting props in different layers
    # The last layer will have higher specifity than the first one
    style: Style = {
      "rule": {
        "border-width": "1px",
        "border-style": "solid",
        "border-top-style": "dotted",
      }
    }

    sheet = StyleSheet(style["rule"])
    assert sheet.media_layers() == {
      "": [
        { # Layer 1
        "f8d6e0e8": "border-width: 1px;", 
        "f594b855": "border-style: solid;"
        },
        { # Layer 2
        "f051471b": "border-top-style: dotted;", 
        }
      ]
    }

  def test_merging_rule_layers_2(self):
    # 
    style: Style = {
      "rule1": {
        "@media": "media",
        "border-width": "1px",
      },
      "rule2": {
        "border-style": "dotted",
        "border-top-style": "groove"
      },
      "rule3": {
        "border-width": "2px",
        "border-top-style": "ridge",
      },
      "rule4": {
        "@media": "media",
        "border-style": "solid",
      },
    }

    sheet1 = StyleSheet(style["rule1"], style["rule2"])
    sheet2 = StyleSheet(style["rule3"], style["rule4"])

    layers = StyleSheet.merge_media_layers(sheet1.media_layers(), sheet2.media_layers())

    assert layers == {
      "": [
        {
          "f987ead0": "border-style: dotted;", 
          "f900f0eb": "border-width: 2px;",
          "f36b21eb": "border-top-style: ridge;",
        },
        {
          "f38c323c": "border-top-style: groove;"
        },
      ],
      "media": [
        {
          "f77d5393": "border-width: 1px;", 
          "f633a431": "border-style: solid;"
        }
      ]
    }

class TestStyling():
  def test_element_with_no_css(self):
    # Does not raise exception
    foo = Element()
  
  def test_element_css(self):
    style: Style = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      }
    }

    foo = Element(css=[style["rule1"], style["rule2"]])
    # assert foo.css.media_layers() == {
    assert foo.media_layers() == {
      "": [
        {
          "f6fa6fa2": "background-color: blue;", 
          "f94fac93": "color: black;"
        }, 
        {
          "f4fcc55d:hover": "background-color: red;"
        }
      ]
    }

  def test_element_class_names(self):
    style: Style = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      }
    }

    foo = Element(css=[style["rule1"], style["rule2"]])
    assert foo.class_names() == ['f94fac93', 'f6fa6fa2', 'f4fcc55d1']

  def test_element_render_css(self):
    style: Style = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      },
      "rule3": {
        "@media": "(min-width: 700px)",
        "text-align": "center",
        ":hover": {
          "color": "black"
        }
      },
    }

    foo = Element(css=[style["rule1"], style["rule2"], style["rule3"]])
    with open("output.css", "w") as f:
      f.write(foo.render_css())

    assert foo.render_css() == """\
.f94fac93 { color: black; }
.f6fa6fa2 { background-color: blue; }
.f4fcc55d1:hover { background-color: red; }

@media (min-width: 700px) {
  .fcb87822 { text-align: center; }
  .ff0d072f:hover { color: black; }
}
"""