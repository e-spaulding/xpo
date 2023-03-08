import json
import argparse
import os
import re
import logging
from qwikidata.entity import WikidataItem, WikidataProperty # type: ignore
from qwikidata.linked_data_interface import get_entity_dict_from_api # type: ignore

parser = argparse.ArgumentParser()
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

parser.add_argument(
    '--file',
    type=str,
    required=False,
    help='The location of the xpo file to be checked. If not provided, it will be inferred.'
)
parser.add_argument(
    '--log_level',
    type=str,
    required=False,
    help='Log level for the logger. Set to WARNING by default. One of DEBUG, INFO, WARNING, ERROR, or CRITICAL.'
)
parser.add_argument(
    '--make_corrections',
    type=str,
    required=False,
    help='Whether or not to make corrections and output them in a new JSON file. By default, set to true.'
)

def infer_filename():
    dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

    # first, strict search
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            pattern = 'xpo_v[0-9]\.[0-9]([a-z]?|(\.[0-9])?)\.json'
            if re.fullmatch(pattern=pattern, string=str(file)):
                return root + '/' + str(file)
    
    # if it couldn't be found with the above pattern, a simpler check
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if 'xpo' in str(file) and '.json' in str(file):
                return root + '/' + str(file)
    
    return ''

def is_in_order(arg_names):
    for i in range(len(arg_names) - 1):
        if arg_names[i] > arg_names[i + 1]:
            return False
    return True

def is_in_dict(qnode, xpo):
    would_be_dwd_key = 'DWD_' + qnode
    for key in xpo.keys():
        if key == 'version':
            continue
        if would_be_dwd_key in xpo[key].keys():
            return True
    return False

if __name__ == '__main__':

    args = parser.parse_args()

    if args.log_level:
        logger.setLevel(args.log_level)
    if not args.file:
        filename = infer_filename()
        logger.warning(f'Filename not provided, inferred as "{filename}"')
    else:
        filename = args.file
    if args.make_corrections and (args.make_corrections == 'false' or args.make_corrections == 'False'):
        make_corrections = False
    else:
        make_corrections = True

    f = open(filename)
    xpo = json.load(f)
    f.close()

    stats = {'entities': {}, 'events': {}, 'relations': {}, 'temporal_relations': {}}
    for key in stats.keys():
        stats[key]['total'] = 0
        stats[key]['with_pb_mappings'] = 0
        stats[key]['num_top_level'] = 0
        stats[key]['list_top_level'] = []

    uncontained_nodes = []
    bad_argument_orderings = []
    missing_descriptions = []
    missing_names = []
    deprecated_nodes = []

    for dict_type in xpo.keys():
        if dict_type == 'version':
            continue

        dictionary = xpo[dict_type]

        # get # of entities, events, relations, and temporal relations
        if dict_type == 'entities':
            stats[dict_type]['total'] = len(dictionary)
        elif dict_type == 'events':
            stats[dict_type]['total'] = len(dictionary)
        elif dict_type == 'relations':
            stats[dict_type]['total'] = len(dictionary)
        elif dict_type == 'temporal_relations':
            stats[dict_type]['total'] = len(dictionary)

        for dwd_key in dictionary.keys():
            q_from_key = dwd_key.split('_')[-1]
            dwd_entry = dictionary[dwd_key]
            qdict = get_entity_dict_from_api(q_from_key)
            if 'Q' in q_from_key:
                q = WikidataItem(qdict)
            else:
                q = WikidataProperty(qdict)
            id_from_wd = q.entity_id
            name_from_wd = q.get_label().lower().replace(' ', '_')
            desc_from_wd = q.get_description()

            if 'wd_node' not in dwd_entry.keys():
                wd_node = 'UNKNOWN_WD_NODE'
                logger.warning(f'Unknown wd_node in {dwd_key}')
                if make_corrections:
                    logger.warning(f'Correcting to {q_from_key}')
                    xpo[dict_type][dwd_key]['wd_node'] = q_from_key
            else:
                wd_node = dwd_entry['wd_node']

            if wd_node != id_from_wd:
                deprecated_nodes.append((dwd_key, name))

            if 'name' not in dwd_entry.keys():
                name = 'UNKNOWN_NAME'
                missing_names.append((dwd_key, name))
                if make_corrections:
                    logger.info(f'Missing name for {dwd_key}. Correcting to "{name_from_wd}"')
                    xpo[dict_type][dwd_key]['name'] = name_from_wd
            else:
                name = dwd_entry['name']

            if 'wd_description' not in dwd_entry.keys():
                description = 'UNKNOWN_WD_DESCRIPTION'
                missing_descriptions.append((dwd_key, name))
                if make_corrections:
                    logger.info(f'Missing description for {dwd_key}. Correcting to "{desc_from_wd[:10]}..."')
                    xpo[dict_type][dwd_key]['wd_description'] = desc_from_wd
            else:
                description = dwd_entry['wd_description']
            
            if 'arguments' in dwd_entry.keys():
                # check that constraints are contained
                for argument in dwd_entry['arguments']:
                    for constraint in argument['constraints']:
                        if not is_in_dict(constraint['wd_node'], xpo):
                            uncontained_nodes.append((dwd_key, name, constraint['wd_node'], constraint['name'], 'c'))

                # check ordering
                ordering = [arg['name'][:2] for arg in dwd_entry['arguments']]
                if not is_in_order(ordering):
                    bad_argument_orderings.append((dwd_key, name))
                    if make_corrections:
                        logger.info(f'Bad argument ordering for {dwd_key}. Correcting to standard ordering (alphabetical).')
                        xpo[dict_type][dwd_key]['arguments'] = sorted(dwd_entry['arguments'], key=lambda x: x['name'])

            if 'overlay_parents' in dwd_entry.keys() and len(dwd_entry['overlay_parents']) > 0:
                for parent in dwd_entry['overlay_parents']:
                    if not is_in_dict(parent['wd_node'], xpo):
                        uncontained_nodes.append((dwd_key, name, parent['wd_node'], parent['name'], 'p'))
            else:
                stats[dict_type]['list_top_level'].append((dwd_key, name))
                stats[dict_type]['num_top_level'] += 1
            
            if 'pb_roleset' in dwd_entry.keys() and len(dwd_entry['pb_roleset']) > 0:
                stats[dict_type]['with_pb_mappings'] += 1

    if make_corrections and (missing_names or missing_descriptions or bad_argument_orderings):
        of = open('corrected_xpo.json', 'w')
        json.dump(xpo, of, indent=4)
        of.close()

    # write report
    of = open('stats.txt', 'w')

    for key in stats.keys():
        of.write(f'Stats for {key} ----\n\n')
        of.write(f'Total {key}: {stats[key]["total"]}\n')
        of.write(f'{key} with PB mappings: {stats[key]["with_pb_mappings"]}\n')
        of.write(f'Top level nodes: {stats[key]["num_top_level"]}\n\n')

        oof = open(f'top_level_{key}.txt', 'w')
        for dwd_key, name in stats[key]['list_top_level']:
            oof.write(f'{dwd_key}\t{name}\n')
        oof.close()

    of.close()


    if deprecated_nodes:
        of = open('deprecated_from_wd.txt', 'w')
        for d in deprecated_nodes:
            of.write(d[0] + '\t' + d[0].split('_')[1] + '\t' + d[1] + '\n')
        of.close()
    
    if uncontained_nodes:
        of = open('uncontained_nodes.txt', 'w')
        of.write('DWD Node\tName\tWhere?\tUncontained node\tUncontained name\n')
        for d in uncontained_nodes:
            where = 'arg constraints' if d[-1] == 'c' else 'overlay parent'
            of.write(d[0] + '\t' + d[1] + '\t' + where + '\t' + d[2] + '\t' + d[3] + '\n')
        of.close()

    of = open('minor_issues.txt', 'w')
    if make_corrections:
        of.write('(Corrected) DWD entries missing names:\n')
    else:
        of.write('DWD entries missing names:\n')
    for d in missing_names:
        of.write(d[0] + '\t' + d[0].split('_')[1] + '\t' + d[1] + '\n')
    if make_corrections:
        of.write('(Corrected) DWD entries missing descriptions:\n')
    else:
        of.write('DWD entries missing descriptions:\n')
    for d in missing_descriptions:
        of.write(d[0] + '\t' + d[0].split('_')[1] + '\t' + d[1] + '\n')
    if make_corrections:
        of.write('(Corrected) DWD entries with bad argument ordering:\n')
    else:
        of.write('DWD entries with bad argument ordering:\n')
    for d in bad_argument_orderings:
        of.write(d[0] + '\t' + d[0].split('_')[1] + '\t' + d[1] + '\n')
    of.close()
