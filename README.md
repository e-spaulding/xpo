# XPO Version 5.2a

This JSON file contains the DWD Overlay and a mapping to the LDC tagsets.

### Changes from 5.2

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
