# DWD Overlay Version 5.2b (Unreleased)

This version is not yet released. For now, the latest official release (v5.2a) can be found [here](https://github.com/e-spaulding/xpo/releases/tag/v5.2a).

The DWD overlay is a subset of the DWD along with mappings to PropBank rolesets, their argument structures, and LDC tagsets. The overlay, which is in JSON format, is split into four sub-dictionaries: events, entities, relations, and temporal relations. Each key is the identifier for the DWD node, and each value contains a dictionary with various fields giving information for that node.

## Fields

```
"type" - the type of node. one of "event_type", "entity_type", or "relation_type"
"wd_node" - Q or P identifier from Wikidata
"name" - Qnode or Pnode label from Wikidata
"wd_description" - description from Wikidata
"curated_by" - how was the node added to the overlay? If the value is "cmu", the node was added automatically along with a PropBank roleset. If the value is "xpo", the node was added after a manual curation process
"arguments" - a list of arguments with their names and slot constraints
"overlay_parents" - direct superclasses of the node within the sub-ontology of the overlay (ie, in Wikidata, the parent may not be a direct superclass, but an ancestor further up the tree)
"ldc_types" - a list of LDC types that are mapped to the DWD node. One DWD node can have several LDC types. This dictionary also contains arguments for the LDC event types which can be cross-referenced to the DWD arguments using the field "dwd_arg_name"
"similar_nodes" - a list of similar Qnodes. The type of similarity can be "SS" (semantic similarity) or "NN" (nearest neighbor) 
"related_qnodes" - for Pnodes, the "Wikidata item of this property" Qnode can be found in this section
```

## Changelog

### Changes (2022-11-08)

Minor change as suggested in the 2022-11-01 XPO subcommittee call. In Wikidata, "plan" and "information" are siblings (both are direct subclasses of "abstract_object"). In DWD, we want "plan" to inherit from "information" (and "information" will inherit from "abstract_object" as usual).

#### New parent added

- plan_Q1371819 --> information_Q11028

### Changes (2022-10-25)

See the [changelog](https://github.com/e-spaulding/xpo/blob/main/CHANGELOG.md) for the full list of changes, dated to this repository's beginning.

Made changes suggested in issues [#1](https://github.com/e-spaulding/xpo/issues/1), [#2](https://github.com/e-spaulding/xpo/issues/2), [#3](https://github.com/e-spaulding/xpo/issues/3), and [#5](https://github.com/e-spaulding/xpo/issues/5).

The most notable update adds several DWD nodes and updates parents in the ontology, as suggested in issues [#2](https://github.com/e-spaulding/xpo/issues/2) and [#3](https://github.com/e-spaulding/xpo/issues/3) and further refined by Anatole Gershman.

#### New DWD Nodes Added (Issues [#2](https://github.com/e-spaulding/xpo/issues/2) and [#3](https://github.com/e-spaulding/xpo/issues/3))

- abstract_object_Q7184903
- rule_Q1151067
- male_Q6581097
- female_Q6581072
- concrete_object_Q4406616
- patient_Q181600
- sick_person_Q12722854
- human_Q5
- medication_Q12140
- chemical_substance_Q79529
- physical_substance_Q28732711
- food_Q2095
- gas_Q11432
- fluid_Q102205
- liquid_Q11435
- medical_test_result_Q91615389
- source_Q31464082
- tweet_Q56119332
- post_Q7216866
- organism_Q7239

#### New Parents Added (Issues [#2](https://github.com/e-spaulding/xpo/issues/2) and [#3](https://github.com/e-spaulding/xpo/issues/3)) 

Note: Read "-->" as "is child of"

- rule_Q1151067 --> message_Q628523 --> information_Q11028 --> abstract_object_Q7184903
- plan_Q1371819 --> abstract_object_Q7184903
- title_Q216353 --> abstract_object_Q7184903
- rank_Q4189293 --> abstract_object_Q7184903
- male_Q6581097 --> abstract_object_Q7184903
- female_Q6581072 --> abstract_object_Q7184903
- patient_Q181600 --> sick_person_Q12722854 --> human_Q5 --> person_Q215627 --> concrete_object_Q4406616
- medication_Q12140 --> drug_Q8386 --> chemical_substance_Q79529 --> physical_substance_Q28732711 --> concrete_object_Q4406616
- food_Q2095 --> concrete_object_Q4406616
- gas_Q11432 --> fluid_Q102205 --> physical_substance_Q28732711
- liquid_Q11435 --> fluid_Q102205
- medical_test_result_Q91615389 --> information_Q11028
- person_Q215627 --> source_Q31464082
- group_of_humans_Q16334295 --> source_Q31464082
- document_Q49848 --> source_Q31464082
- tweet_Q56119332 --> broadcasting_Q15078788
- post_Q7216866 --> broadcasting_Q15078788
- organism_Q7239 --> concrete_object_Q4406616
- bacteria_Q10876 --> organism_Q7239

#### Changed
 
- (Issue [#3](https://github.com/e-spaulding/xpo/issues/3)) health_problem_2057971 is no longer a parent of bacteria_Q10876
- (Issue [#1](https://github.com/e-spaulding/xpo/issues/1)) Added missing "ldc_argument_output_value"s for the following LDC type mappings:
	- Evaluate.Belief.CommittedBelief
	- Evaluate.Belief.NonCommittedBelief
	- Evaluate.Sentiment.Negative
	- Evaluate.Sentiment.Positive
	- Evaluate.Status.HoaxFraud
	- Physical.LocatedNear.Surround
	- ResponsibilityBlame.ClaimResponsibility.ClaimResponsibility
	- ResponsibilityBlame.AssignBlame.AssignBlame
- (Issue [#5](https://github.com/e-spaulding/xpo/issues/5)) Standardized the ordering of DWD arguments to be in alphabetical order. Affected nodes:
	- DWD_Q28777323
	- DWD_Q815758
	- DWD_Q175111
	- DWD_Q2727213
	- DWD_Q53706
	- DWD_Q1933595
	- DWD_Q11499267
	- DWD_Q1145523
	- DWD_Q1425577
	- DWD_Q567303
	- DWD_Q1472062
	- DWD_Q11024
	- DWD_Q3030248
	- DWD_Q52943
	- DWD_Q26398
	- DWD_Q202875
	- DWD_Q170028
	- DWD_Q52947181
	- DWD_Q22445448
	- DWD_Q707125
	- DWD_Q325980
	- DWD_Q3075355
	- DWD_Q210603
	- DWD_Q166231
	- DWD_Q193078
	- DWD_Q192995
	- DWD_Q606332
	- DWD_Q57699905
	- DWD_Q107434802
	- DWD_Q61509
	- DWD_Q7590
	- DWD_Q6206738
	- DWD_Q464858
	- DWD_Q574433
	- DWD_Q1318578
	- DWD_Q40231
	- DWD_Q20826785
	- DWD_Q17052147
	- DWD_Q796919
	- DWD_Q899277
	- DWD_Q2827815
	- DWD_Q707482
	- DWD_Q21651837
	- DWD_Q1763090
	- DWD_Q12136
	- DWD_Q3629144
	- DWD_Q4681306
	- DWD_Q459428
	- DWD_Q4698318
	- DWD_Q4698686
	- DWD_Q177414
	- DWD_Q2357982
	- DWD_Q4381136
	- DWD_Q450743
	- DWD_Q1499786
	- DWD_Q191671
	- DWD_Q257506
	- DWD_Q25496170
	- DWD_Q1931037
	- DWD_Q4456944
	- DWD_Q5195029
	- DWD_Q74026205
	- DWD_Q18603731
	- DWD_Q11896502
	- DWD_Q11651
	- DWD_Q11868838
	- DWD_Q56298508
	- DWD_Q12142910
	- DWD_Q140028
	- DWD_Q30017
	- DWD_Q3178478
	- DWD_Q6468645
	- DWD_Q1812889
	- DWD_Q16686611
	- DWD_Q98953195
	- DWD_Q1971485
	- DWD_Q106008354
	- DWD_Q7371358
	- DWD_Q7456126
	- DWD_Q331902
	- DWD_Q68133333
	- DWD_Q306518
	- DWD_Q732722
	- DWD_Q83462
	- DWD_Q1192097


