### Changes (2023-05-01)

Updated labels and descriptions with the most up-to-date info from Wikidata. 

#### Changed

- `name` of 180 nodes, see tab 1 [here](https://docs.google.com/spreadsheets/d/1LjV3N1T31RfHka2VVaVM26Ps7z0ldN8YN52ueQ_2Rww/edit?usp=sharing)
- `wd_description` of 917 nodes, see tab 2 [here](https://docs.google.com/spreadsheets/d/1LjV3N1T31RfHka2VVaVM26Ps7z0ldN8YN52ueQ_2Rww/edit?usp=sharing)
- `name` in 308 subdictionaries (`overlay_parents` and `constraints` in `arguments`) wherever the name change above appeared

### Changes (2023-04-17)

#### Removed

- DWD_Q779970: inaccurate mapping

### Changes (2023-04-10)

#### Changed

Reverted some changes from 5.4.4 that caused problems for those using DWD. Issue [#27](https://github.com/e-spaulding/xpo/issues/27)

#### Removed

- DWD_Q424737: it was added by error

### Changes (2023-04-07)

#### Added

Suggestions based on gaps in CMU's schema library:

- Q788790 as an entity rather than an event, parent DWD_Q11028
- Q24229398
- Q12737077
- Q12870, parent DWD_Q79529

#### Changed

Based on Issue [#24](https://github.com/e-spaulding/xpo/issues/24)

- DWD_Q10676833 --> DWD_Q424737
- DWD_Q12779002 --> DWD_Q99348376
- Also fixed a small amount of redirects

### Changes (2023-04-04)

Added more PB-WD mappings.

#### Added

- Event nodes with PB mappings on the first tab [here](https://docs.google.com/spreadsheets/d/1diOybJQ12Awt54lk66Jabs_GeWnq8eKRZ3HGAwEgvRk/edit?usp=sharing)

#### Changed

- Mappings for DWD nodes on the second tab [here](https://docs.google.com/spreadsheets/d/1diOybJQ12Awt54lk66Jabs_GeWnq8eKRZ3HGAwEgvRk/edit?usp=sharing)
- Corrected PB mapping in DWD_Q26972
- Constraints on A1 of DWD_Q4254955
- PB mapping for DWD_Q10843872 and updating its name

### Changes (2023-03-31)

Fixing various small issues.

#### Changed

- Template for DWD_Q83267 (and added an argument)

#### Added

- Missing templates for ~300 events. All events should now have templates.

#### Removed

- DWD_Q930412 (no arguments, only partial mapping)
- Fixed DWD_Q1191527 wd_node field

Following are not in DWD but were added to 5.4 ([#20](https://github.com/e-spaulding/xpo/issues/20)):

- DWD_Q112803924
- DWD_Q113280972
- DWD_Q113594218
- DWD_Q115158676
- DWD_Q115287494
- DWD_Q115298947
- DWD_Q115397708
- DWD_Q116771298

### Changes (2023-03-30)

Final chemical spill additions.

#### Added

- Q275459_radiation_syndrome

#### Changed

- Specific diseases mapping to ill.01 now have strict constraints for A2 as themselves

### Changes (2023-03-20)

Curated events identified as part of the chemical spill domain. Several events were already in the overlay; those that were automatically added in the past were manually vetted and occasionally modified slightly. All curation statuses were updated to show that the events have been vetted manually.

#### Added

- Q383973_electricity_generation

#### Changed

- Q25536342_toxin_exposure A2_gol_exposed_to restricted to "toxin"
- Q87412590_nuclear_hazard AM_mnr_endangering_thing added and restricted to "nuclear_material"
- Q1175042_supervision curation status updated
- Q105825117_dumping curation status updated
- Q828827_power_outage A1_ppt_thing_lost restricted to "electric_power_distribution"

### Changes (2023-03-15)

#### Added

18 entity nodes and their parents in the overlay (chemical spill domain)

- See entity nodes in the third tab in [this sheet](https://docs.google.com/spreadsheets/d/1QTHOOoiVgqvwZpB1hemYjmPxvOE63HB9laSPA4zjVjw/edit?usp=sharing)

#### Removed

- right_Q22059430: redirects to right_Q2386606; fixing error in previous merge ([#19](https://github.com/e-spaulding/xpo/issues/19))

### Changes (2023-03-14)

#### Changed

Updated redirects

- equipment_Q16798631 updated to equipment_Q10273457 ([#19](https://github.com/e-spaulding/xpo/issues/19))

### Changes (2023-03-07)

Disambiguated some PB-WD mappings in which more than one roleset was mapped to a Qnode.

#### Changed

Roleset mappings for the following 21 event nodes:

- DWD_Q105460363
- DWD_Q110458263
- DWD_Q1121708
- DWD_Q11639276
- DWD_Q1643184
- DWD_Q204015
- DWD_Q23090331
- DWD_Q241625
- DWD_Q28972820
- DWD_Q29017603
- DWD_Q29485
- DWD_Q3933467
- DWD_Q4026292
- DWD_Q47496130
- DWD_Q65757353
- DWD_Q8070
- DWD_Q8081
- DWD_Q83500
- DWD_Q878143
- DWD_Q9073584
- DWD_Q930933

### Changes (2023-03-02)

Integrated event mappings from the PropBank-Wikidata mapping annotation project. 

#### Added

- 235 new event nodes with PropBank mappings (see [here](https://docs.google.com/spreadsheets/d/1dj5Q9xXIjWNrtWOpI5bV4zJzHnpvMQdS8iHmKosPc2w/edit?usp=sharing), tab "Nodes that were ADDED")

#### Changed

- PropBank mappings for ~111 event nodes (see [here](https://docs.google.com/spreadsheets/d/1dj5Q9xXIjWNrtWOpI5bV4zJzHnpvMQdS8iHmKosPc2w/edit?usp=sharing), tab "Nodes for which the PB mapping CHANGED")
- Field `mapping_flags` to `mapping_types`

### Changes (2023-03-01)

Added event templates.

#### Added

- New fields "template" and "template_curation" to every event node with their respective templates and curation values. `xpo` means the template has been manually vetted by the XPO subcommittee; `auto` means the template was automatically generated and may be errorful.

### Changes (2023-02-28)

Added relations from Rosario's relation overlay. 49 new Pnodes were added to the relations with PropBank mappings and 34 mappings were added to existing DWD Pnodes. 

#### Added

- Mappings from [this](https://docs.google.com/spreadsheets/d/1UE-suWHWghrSxsY0_rDnX8k6oYs5ISFXpLr_Muss5pA/edit?usp=sharing) list

#### Changed

- Added new keys to arguments for relations: "wd_slot" and "mapping_flags". Notes:
	- "wd_slot" is redundant with "name", but is more descriptive. The "wd_slot" key gives the name of the Pnode slot in Wikidata for each argument mapping. "name" will be kept to avoid breaking code using previous JSONs, even though "name": "A0" always corresponds to "wd_slot": "subject" and "name": "A1" always corresponds to "wd_slot": "object". 
	- "mapping_flags" lists flags users should pay attention to when mapping from relations to PropBank and vice-versa. The only flag we currently have is "strict_constraints" which indicates that a Pnode cannot be inferred from a PropBank event mention unless the constraints are met for each argument. We expect to add more flags (and documentation for their meanings) as we add more complex PropBank mappings.

### Changes (2023-02-20)

Removed a loop in the hierarchy.

#### Changed

- Removed parent of DWD_Q2434238_heritage (the parent was DWD_Q2434238 itself)

### Changes (2023-01-24)

Incorrect PB mapping and arguments fixed.

#### Changed

- PB mapping and arguments for casting_Q849891 (Issue [#14](https://github.com/e-spaulding/xpo/issues/14))

### Changes (2022-12-23)

Entity node changes in Wikidata required changes in the overlay.

#### Qnodes changed

- right_Q22059430 --> right_Q2386606
- equipment_Q16798631 --> equipment_Q10273457

### Changes (2022-12-06)

Entity and event node additions based on suggestions from ISI, plus a handful of relations.

#### New DWD Nodes Added

- Q18351973_disembarkation
- Q7126717_download
- Q176274_recess
- Q110458263_taking
- Q16944487_waiting
- Q43059_drought
- Q50380088_protective agent
- Q3863_asteroid
- Q93352_coast
- Q251777_custom
- Q852835_customer
- Q1088842_detonator
- Q4115986_disaster area
- Q65088916_dummy
- Q141022_eclipse
- Q1096907_electrical grid
- Q3053337_employer
- Q3196_fire
- Q58197759_hurricane
- Q16886469_importance
- Q16358610_instructor
- Q7239_organism
- Q105810946_physical location
- Q11997597_representative
- Q2995644_result
- Q1020013_share price
- Q6671777_structure
- Q66254282_target
- Q17502905_the media
- Q11471_time
- P1264_valid in period
- P4250_defined daily dose
- P2257_event interval

### Changes (2022-12-05)

Minor typos and errors in the JSON fixed, plus, standardized AM_loc.* argument constraints.

#### Removed

- Slot constraint geographic_entity from A2 of DWD_Q245359

#### Changed

- Every instance of \{"AM_loc_location", "AM_loc__location"\} to "AM_loc" (Issue [#11](https://github.com/e-spaulding/xpo/issues/11))
- Standardized ordering of keys in argument dictionaries. Ordering is now ("short_name", "name", "constraints"). (Issue [#11](https://github.com/e-spaulding/xpo/issues/11))

### Changes (2022-12-01)

Minor typos and errors in the JSON fixed.

#### Removed

- Some duplicate AM_loc arguments
- DWD_Q2349814 (duplicate of/too similar to DWD_Q210978)

#### Changed

- Standardized case for argument modifier slots (issue [#10](https://github.com/e-spaulding/xpo/issues/10))
- DWD_Q647578 - nodes "piracy" and "copyright_infringement" seem to have merged. Updated name to "copyright_infringement" and removed overlay_parent which is the same node

### Changes (2022-11-08)

Minor change as suggested in the 2022-11-01 XPO subcommittee call. In Wikidata, "plan" and "information" are siblings (both are direct subclasses of "abstract_object"). In DWD, we want "plan" to inherit from "information" (and "information" will inherit from "abstract_object" as usual).

#### New parent added

- plan_Q1371819 --> information_Q11028

### Changes (2022-10-25)

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

### Changes from 5.2 (2022-09-13)

5.2 was mistakenly generated from an older version of the JSON (5.1). 5.2a is all the changes from 5.2, but generated using 5.1a. 5.1a had updated PropBank mappings for nodes such as DWD_Q34394_belief, so the current 5.2a now reflects those updated mappings.

#### Added

* A `"version"` entry to the JSON.

### Changes from 5.1a

#### Changed

* Updated [50 redirected qnodes](https://github.com/e-spaulding/xpo/issues/4#issue-1371674763)
* Changed all instances of "curated_by": "xpo team" to "curated_by": "xpo"

#### Removed

* DWD_Q7316896 from overlay (it is not in DWD)
* Space from `"wd_node": "Q6657015 "`
  * Removed all other instances of trailing whitespaces in strings (mainly in LDC argument mappings)
