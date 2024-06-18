from pattern3.text.en import conjugate,PAST

class TemplateGenerator():

    def __init__(self):
        # these prepositions are to be appended in front of each arg in the template:
        self.prepositions = self.generate_arg_inflections() 

    def generate_template(
            self,
            event,
            arg_dicts
        ):
        template = ''

        if '_' in event:
            event_tokens = event.split('_')
            try:
                past_tense_verb = conjugate(event_tokens[0], tense=PAST) + '_' + '_'.join(event_tokens[1:])
            except:
                past_tense_verb = conjugate(event_tokens[0], tense=PAST) + '_' + '_'.join(event_tokens[1:])
        elif ' ' in event:
            event_tokens = event.split(' ')
            try:
                past_tense_verb = conjugate(event_tokens[0], tense=PAST) + ' ' + ' '.join(event_tokens[1:])
            except:
                past_tense_verb = conjugate(event_tokens[0], tense=PAST) + ' ' + ' '.join(event_tokens[1:])
        else:
            try:
                past_tense_verb = conjugate(event, tense=PAST)
            except:
                # idk what's going on with pattern3 but running conjugate() twice
                # seems to do the trick
                past_tense_verb = conjugate(event, tense=PAST)

        # Start with A0 and A1:

        if len(arg_dicts) > 0:
            template += f'<{arg_dicts[0]["name"]}> {past_tense_verb}'
        else:
            template = past_tense_verb

        if len(arg_dicts) > 1:
            template += f'{self.get_preposition(arg_dicts[1])}<{arg_dicts[1]["name"]}>'

        # Assuming the arg dict is correctly ordered, which it *should* be
        for arg_dict in arg_dicts[2:]:
            template += f'{self.get_preposition(arg_dict)}<{arg_dict["name"]}>'

        return template

    def get_preposition(self, arg_dict):
        if arg_dict['name'] in self.prepositions:
            return ' ' + self.prepositions[arg_dict['name']] + ' '
        elif arg_dict['short_name'] in self.prepositions:
            return ' ' + self.prepositions[arg_dict['short_name']] + ' '
        else:
            return ' '
        
    def generate_arg_inflections(self):
        f = open('scripts/arg_inflections.tsv')
        arg_inflections = {}
        for line in f.readlines():
            tokens = line.split('\t')
            arg_inflections[tokens[0]] = tokens[1].strip()
        return arg_inflections
    
# template_gen = TemplateGenerator()

# xpof = open('/Users/elizabeth/Code/kairos/xpo/xpo_v5.4.9.json')
# import json
# xpo = json.load(xpof)

# print(template_gen.generate_template(xpo['events']['DWD_Q110013332']['name'], xpo['events']['DWD_Q110013332']['arguments']))