import json
import argparse
import os
import re
import logging
from qwikidata.entity import WikidataItem, WikidataProperty
from qwikidata.linked_data_interface import get_entity_dict_from_api

parser = argparse.ArgumentParser()
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

parser.add_argument(
    '--qnodes',
    type=str,
    required=True,
    help='The location of the file containing qnodes to be added.'
)
parser.add_argument(
    '--qnode_type',
    type=str,
    required=True,
    help='To which overlay section should the qnodes be added? Entities, or events?'
)
parser.add_argument(
    '--xpo',
    type=str,
    required=False,
    help='The location of the XPO overlay file to be modified. If no filename is provided, it will be inferred.'
)
parser.add_argument(
    '--log_level',
    type=str,
    required=False,
    help='Log level for the logger. Set to WARNING by default. One of DEBUG, INFO, WARNING, ERROR, or CRITICAL.'
)

def infer_filename():
    dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

    # first, strict search
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            pattern = 'xpo_v[0-9]\.[0-9][a-z]?\.json'
            if re.fullmatch(pattern=pattern, string=str(file)):
                return root + '/' + str(file)
    
    # if it couldn't be found with the above pattern, a simpler check
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if 'xpo' in str(file) and '.json' in str(file):
                return root + '/' + str(file)
    
    return ''

if __name__ == '__main__':

    args = parser.parse_args()

    if args.log_level:
        logger.setLevel(args.log_level)
    if not args.xpo:
        filename = infer_filename()
        logger.warning(f'Filename not provided, inferred as "{filename}"')
    else:
        filename = args.xpo
    if args.qnode_types not in ['entities', 'events']:
        logger.error(f'Can only add Qnodes that are "entities" or "events"')
        quit()

    f = open(filename)
    xpo = json.load(f)
    f.close()
    
    f = open(args.qnodes)
    added = 0

    for line in f.readlines():
        qnode_string = line.strip()
        qdict = get_entity_dict_from_api(qnode_string)
        if 'Q' in qnode_string:
            q = WikidataItem(qdict)
        else:
            q = WikidataProperty(qdict)
        id_ = q.entity_id
        name = q.get_label().lower().replace(' ', '_')
        desc = q.get_description()

        dwd_key = 'DWD_' + qnode_string

        if dwd_key in xpo['events'] or dwd_key in xpo['entities'] or dwd_key in xpo['relations'] or dwd_key in xpo['temporal_relations']:
            logger.warning(f'About to add entry {dwd_key} in {args.qnode_types}, but it already exists! Skipping this addition...')
            continue
        
        if args.qnode_types == 'entities':
            type_string = 'entity_type'
        else:
            type_string = 'event_type'

        xpo[args.qnode_types][dwd_key] = {}
        xpo[args.qnode_types][dwd_key]['type'] = type_string
        xpo[args.qnode_types][dwd_key]['name'] = name
        xpo[args.qnode_types][dwd_key]['wd_node'] = id_
        xpo[args.qnode_types][dwd_key]['wd_description'] = desc
        xpo[args.qnode_types][dwd_key]['overlay_parents'] = []
        xpo[args.qnode_types][dwd_key]['curated_by'] = 'xpo'
        xpo[args.qnode_types][dwd_key]['ldc_types'] = []
        xpo[args.qnode_types][dwd_key]['similar_nodes'] = []
        added += 1

    logger.info(f'Added {added} qnodes.')
    of = open('updated_xpo_please_rename.json', 'w')
    json.dump(xpo, of, indent=4)
    of.close()