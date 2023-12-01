# DWD Overlay Version 5.5.2

The DWD overlay is a subset of the DWD along with mappings to PropBank rolesets, their argument structures, and LDC tagsets. The overlay, which is in JSON format, is split into four sub-dictionaries: events, entities, relations, and temporal relations. Each key is the identifier for the DWD node, and each value contains a dictionary with various fields giving information for that node.

We intend for the mappings contained in the overlay to eventually be completely integrated into Wikidata itself so that the data no longer needs to be hosted in this JSON file. See the [project page](https://www.wikidata.org/wiki/Wikidata:WikiProject_Events_and_Role_Frames) for further details on this project.

## Current coverage

| ERE Type | Total | Annotated |
| -------- | ----- | --------- |
| Entities | 280   | 280	   |
| Events   | 5764  | 2224      |
| Relations| 216   | 216       |
| Temporal Relations | 8 | 8   |

Additionally, each of the 5,764 events has an event template, which are also undergoing annotation. There are currently *2,461* annotated templates.

Finally, the PropBank-Wikidata mapping annotators record every time they find a roleset that has no viable mapping in Wikidata, There are currently *9,011* rolesets that annotators have marked as "gaps."

## Fields

- `type` - the type of node. one of `event_type`, `entity_type`, or `relation_type`
- `wd_node` - Q or P identifier from Wikidata
- `name` - Qnode or Pnode label from Wikidata
- `wd_description` - description from Wikidata
- `curated_by` - how was the node added to the overlay? If the value is `cmu`, the node was added semi-automatically along with a PropBank roleset. (As such, those entries may be imperfect, so please submit any errors you find as an [issue](https://github.com/e-spaulding/xpo/issues/new).) If the value is `xpo`, the node was added after a manual curation process and at least double-annotated. If the value is `xpo_partial`, the mapping is from one annotator's single pass.
- `pb_roleset` and `additional_rolesets` - the PropBank roleset mappings for the node. `additional_rolesets` gives additional mappings that are as compatible with the main `pb_roleset` mapping, but added to the overlay later.
- `arguments` - a list of arguments with their names and slot constraints. Note that the slot constraints should be taken as a suggestion rather than a strict constraint, unless `mapping_types` says otherwise.
	- Relations have a `wd_slot` and possibly a `pb_mapping` with `mapping_types`. The `wd_slot` gives the Pnode slot in Wikidata (either subject or object); `pb_mapping` gives the PropBank argument name corresponding the the WD slot; and `mapping_types` gives a list of flags warning users when a mapping may not work. (The only type right now is `strict_constraints`, which means a PropBank event cannot be used to generate a Pnode with this mapping unless the constraints are met.)
- `overlay_parents` - direct superclasses of the node within the sub-ontology of the overlay (ie, in Wikidata, the parent may not be a direct superclass, but an ancestor further up the tree)
- `ldc_types` - a list of LDC types that are mapped to the DWD node. One DWD node can have several LDC types. This dictionary also contains arguments for the LDC event types which can be cross-referenced to the DWD arguments using the field `dwd_arg_name`
- `similar_nodes` - a list of similar Qnodes. The type of similarity can be `SS` (semantic similarity) or `NN` (nearest neighbor) 
- `related_qnodes` - for Pnodes, the "Wikidata item of this property" Qnode can be found in this section
- `template` - A template which allows users to automatically generate a natural language sentence with an event and its argument instantiation. Only for events.
- `template_curation` - The curation status of the template. Either manually vetted by XPO (`xpo`) or automatically generated, and possibly an unnatural or incorrect sentence (`auto`).

## Changes from 5.5.1

Full changelog in [CHANGELOG.md](https://github.com/e-spaulding/xpo/blob/main/CHANGELOG.md).

### Changes (2023-12-01)

Revisited original LDC-XPO mappings and rolesets on those mappings.

#### Changed

Mappings may have changed on the following nodes. Where mappings changed, templates were changed accordingly. See [here](https://docs.google.com/spreadsheets/d/1fcSSrFXIQfnCAij1xEBph11RIBZAqUWh/edit?usp=sharing&ouid=116351218637855731324&rtpof=true&sd=true) for further details.

- DWD_Q22445448
- DWD_Q707125
- DWD_Q3241045
- DWD_Q168983
- DWD_Q83267
- DWD_Q321839
- DWD_Q98398200
- DWD_Q3537603
- DWD_Q841236
- DWD_Q21004260
- DWD_Q179661
- DWD_Q192995
- DWD_Q57699905
- DWD_Q7590
- DWD_Q12136

#### Removed

- DWD_Q2112782 (a typo)