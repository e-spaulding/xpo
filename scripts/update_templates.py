import json

PATH_TO_XPO = '/Users/elizabeth/Code/kairos/xpo/xpo_v5.5.json' # change this to the path of the xpo file
PATH_TO_TEMPLATES = '/Users/elizabeth/Code/kairos/xpo/templates.tsv' # change this to the path of the templates file
# Template file should be a TSV file with the following columns:
# DWD key, Template, Curation status
NEW_XPO_PATH = '/Users/elizabeth/Code/kairos/xpo/xpo_v5.6.json' # change this to the path of the new xpo file

f = open(PATH_TO_XPO)
xpo = json.load(f)
f.close()

f = open(PATH_TO_TEMPLATES)
f.readline()
only_curation_change = 0
template_change = 0
no_change = 0
template_add = 0
key_not_found = 0
relations_add = 0
for line in f.readlines():
    tokens = line.split('\t')
    dwd_key = tokens[0].strip()
    template = tokens[1].strip()
    curation = 'xpo' if tokens[2].strip() == 'XPO' else 'auto'
    if dwd_key in xpo['events']:
        where = 'events'
    # Uncomment below if you want to update templates in entities and relations
    # elif dwd_key in xpo['entities']:
    #     where = 'entities'
    # elif dwd_key in xpo['relations']:
    #     where = 'relations'
    #     relations_add += 1
    else:
        print(f'Key not found: {dwd_key}')
        key_not_found +=1 
        continue


    if 'template' not in xpo[where][dwd_key].keys():
        xpo[where][dwd_key]['template'] = template
        xpo[where][dwd_key]['template_curation'] = curation
        template_add += 1
        continue

    if xpo[where][dwd_key]['template'] == template:
        if xpo[where][dwd_key]['template_curation'] != curation:
            xpo[where][dwd_key]['template_curation'] = curation
            only_curation_change += 1
        else:
            no_change += 1
    else:
        xpo[where][dwd_key]['template'] = template
        xpo[where][dwd_key]['template_curation'] = curation
        template_change += 1

print(f'Only the curation status changed, but not the template: {only_curation_change}')
print(f'Both the curation status and the template was changed: {template_change}')
print(f'Templates added: {template_add}')
print(f'No change: {no_change}')
print(f'Key not found: {key_not_found}')
# print(f'Template in relations: {relations_add}')
f.close()
f = open(NEW_XPO_PATH, 'w')
json.dump(xpo, f, indent=4)
f.close()