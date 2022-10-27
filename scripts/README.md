# Scripts

This directory contains some scripts to help with the management of the JSON file.

## Verification script

The script `verification.py` checks for several items in the JSON and produces a number of text files summarizing notable information. Running this script can act as a sanity check after making changes to the JSON. The script checks for, and outputs:

* Any mention of a Qnode that is NOT included in the overlay (either as an argument constraint, or an overlay parent)
* Deprecated Qnodes (when the Qnode ID changes in Wikidata and is redirected to a new Qnode ID)
* Minor issues: nodes missing names, nodes missing wd_descriptions, and nodes not following an alphabetical argument ordering
* Number of entities, events, relations, and temporal relations, respectively
* Number of _top level_ entities, events, relations, and temporal relations, respectively. Also, outputs top level nodes to a text file for easy human browsing.

Usage:

```
verification.py [-h] [--file FILE] [--log_level LOG_LEVEL] [--make_corrections MAKE_CORRECTIONS]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           The location of the xpo file to be checked. If not provided, it will be inferred.
  --log_level LOG_LEVEL
                        Log level for the logger. Set to WARNING by default. One of DEBUG, INFO, WARNING, ERROR, or CRITICAL.
  --make_corrections MAKE_CORRECTIONS
                        Whether or not to make corrections and output them in a new JSON file. By default, set to true.
```

## Node addition script

There is also a simple script `add_nodes.py` that adds nodes (of the same type) en masse. It accepts a text file of newline-separated Qnode IDs, like so:

```
Q3302947
Q180856
Q30612
```

It adds the Qnodes, along with their type \[`entity_type`, `event_type`, etc.\], name, and description. By default, they will have no `overlay_parents`, `ldc_types`, or `similar_nodes`. If the need arises to add these values en masse, the script and input file format will be modified to do so.

Usage:

```
add_nodes.py [-h] --qnodes QNODES --qnode_type QNODE_TYPE [--xpo XPO] [--log_level LOG_LEVEL]

optional arguments:
  -h, --help            show this help message and exit
  --qnodes QNODES       The location of the file containing qnodes to be added.
  --qnode_type QNODE_TYPE
                        To which overlay section should the qnodes be added? Entities, or events?
  --xpo XPO             The location of the XPO overlay file to be modified. If no filename is provided, it will be inferred.
  --log_level LOG_LEVEL
                        Log level for the logger. Set to WARNING by default. One of DEBUG, INFO, WARNING, ERROR, or CRITICAL.
```