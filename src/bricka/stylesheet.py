from bricka.conflicts import CONFLICTS
from bricka.style import Rule, EXTRA_PROPS
from typing import cast
import hashlib

class StyleSheet:    
  def __init__(self, *rules: Rule) -> None:
    self.at_rules: dict[str, dict[str, str]] = {}

    # for rule in rules:
    #   if type(rule) != dict:
    #     raise TypeError(f"Argument 'rule' must be of type 'Rule': {rule}")
    
    self.at_rules = self._merge(*rules)

  def append_rule(self, rule: Rule) -> None:
    self._merge(rule)

  def _normalize(self, rule: Rule) -> dict[str, str]:
    style: dict[str, str] = {}

    expanded_rule: Rule = {}

    for prop, value in rule.items():
      if prop not in EXTRA_PROPS:
        expanded_rule[prop] = value
      else:
        for p, v in self.expand_extra_prop(prop, [str(value)]).items():
          expanded_rule[p] = v  

    rule = expanded_rule

    media = rule.get("@media", "")
    style["@media"] = media

    for prop, value in rule.items():
      if prop.startswith("@"):
        continue
      elif prop.startswith(":"):
        style |= self._normalize_pseudo_class(prop, cast(Rule, value))
      else:
        if type(value) == tuple:
          style[prop] = " ".join(value) # TODO: DRY
        else:
          style[prop] = str(value)

    return style
  
  def expand_extra_prop(self, prop_name: str, values: list[str]) -> dict[str, str]:
    props: dict[str, str] = {}
    if prop_name in EXTRA_PROPS:
      if len(EXTRA_PROPS[prop_name]) != len(values):
        raise Exception(f"Invalid number of parameters for extra prop: {prop_name}, {values}")

      for i, params in enumerate(EXTRA_PROPS[prop_name]):
        for param in params:
          props[param] = values[i]

    return props  

  def _normalize_pseudo_class(self, pseudo_class: str, rule: Rule, parent: str = "") -> dict[str, str]:
    style: dict[str, str] = {}

    if not pseudo_class.startswith(":"):
      raise TypeError(f'Pseudo class must start with a colon: {pseudo_class}')

    for prop, value in rule.items():
      if prop.startswith("@"):
        continue
      elif prop.startswith(":"):
        style |= self._normalize_pseudo_class(prop, cast(Rule, value), parent)
      else:
        parent += pseudo_class
        if type(value) == tuple:
          style[prop + parent] = " ".join(value)
        else:  
          style[prop + parent] = str(value)

    return style
  
  def _media(self, rule: Rule) -> str:
    return rule.get("@media", "")

  def _merge(self, *rules: Rule) -> dict[str, dict[str, str]]:
    # media_queries: dict[str, dict[str, str]] = {}
    media_queries: dict[str, dict[str, str]] = self.at_rules

    for rule in rules:
      normalized_rule = self._normalize(rule)
      media = self._media(rule)
      if media not in media_queries:
        media_queries[media] = normalized_rule.copy()
        del media_queries[media]["@media"]
      else:
        for prop, value in normalized_rule.items():
          if prop.startswith("@media"):
            continue

          if prop in media_queries[media]:
            del media_queries[media][prop]
        
          media_queries[media][prop] = str(value)
    
    return media_queries
  
  def raw_style(self) -> dict[str, dict[str, str]]:
    return self.at_rules
  
  def _base_name(self, prop_name: str) -> str:
    return prop_name.split(":")[0]

  def _pseudo_name(self, prop_name: str) -> str:
    parts = prop_name.split(":", 2)
    if len(parts) >= 2:
      return ":" + parts[1] # TODO: DRY ':'
    
    return ""  
  
  def declaration(self, prop_name: str, media: str = "") -> str:
    name = self._base_name(prop_name)
    return f'{name}: {self.at_rules[media][prop_name]};'   

  def class_name(self, prop_name, media: str = "") -> str:
    name_length = 7
    declaration = self.declaration(prop_name, media)

    return "f" + hashlib.sha1((media + prop_name + declaration).encode()).hexdigest()[:name_length]
  
  def selector(self, prop_name, media: str = "") -> str:
    return self.class_name(prop_name, media) + self._pseudo_name(prop_name)
  
  def _conflict_count(self, prop_name: str, conflicts: dict[str, int]) -> int:
    name = self._base_name(prop_name)
    sub_props = CONFLICTS[name]
    count = -1

    count = max(count, conflicts.get(name + "$", -1))
    if type(sub_props) == list:
      for sp in sub_props:
        count = max(count, self._conflict_count(sp, conflicts))

    return count  
  
  def _resolve(self, prop_name: str, conflicts: dict[str, int], layer: int | None = None) -> None:
    name = self._base_name(prop_name)
    sub_props = CONFLICTS[name]

    if layer is None:
      layer = self._conflict_count(name, conflicts) + 1
      conflicts[name] = layer

    conflicts[name + "$"] = layer

    if type(sub_props) == list:
      for sp in sub_props:
        self._resolve(sp, conflicts, layer) 

  def media_layers(self) -> dict[str, list[dict[str, str]]]:
    layers: dict[str, list[dict[str, str]]] = {}

    for media, props in self.raw_style().items():
      media_conflicts: dict[str, int] = {}

      l = []
      for prop in props: 
        self._resolve(prop, media_conflicts)
        conflict_count = media_conflicts[self._base_name(prop)]

        while len(l) <= conflict_count:
          l.append({})

        l[conflict_count][self.selector(prop, media)] = self.declaration(prop, media)  

      layers[media] = l

    return layers     

  @classmethod
  def merge_media_layers(cls, *layers: dict[str, list[dict[str, str]]]) -> dict[str, list[dict[str, str]]]: 
    new_layers: dict[str, list[dict[str, str]]] = {}

    for css in layers:
      for media, layers_list in css.items():
        new_list = new_layers.get(media, None)
        if new_list is None:
          new_list = []
          new_layers[media] = new_list

        for i, props_dict in enumerate(layers_list):
          max_length = max(len(new_list), len(layers_list)) 

          while len(new_list) < max_length:
            new_list.append({}) 

          while len(layers_list) < max_length:
            layers_list.append({}) 

          for i in range(max_length):
            new_list[i] |= layers_list[i]       
    
    return new_layers   
  