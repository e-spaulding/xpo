import re

f = open('snapshot-4-23-24.tsv') # Change this to the path of the spreadsheet tab downloaded in tsv format with only the following columns:/
# Status, Roleset with description, Best Qnode, Second best Qnode
q2pb_file = open('q2pb.tsv', 'w') # Change this to the path of the output file
problem_file = open('ss2tsv_problems.txt', 'w') # File to log problems
wd_gaps_file = open('wd_gaps.tsv', 'w') # File to log WD gaps
q_pattern = 'Q[0-9]+'
r_pattern = '[a-z]+(_[a-z]+)*\.[0-9][0-9]'
f.readline()
for i, line in enumerate(f.readlines()):
    tokens = line.split('\t')
    status = tokens[0].strip()
    roleset_with_desc = tokens[1].strip()
    m = re.search(pattern=r_pattern, string=roleset_with_desc)
    if m:
        roleset = m.group()
    else:
        print(f'Error finding roleset on line {i+2}.')
        problem_file.write(f'Line {i+1}\n')
        continue
    best_qnode = tokens[2].strip()
    if len(tokens) > 3:
        second_best_qnode = tokens[3].strip()
    
    if status == 'Gold' or status == 'Double':
        curated_by = 'xpo'
    elif status == 'Single':
        curated_by = 'xpo_partial'
    else:
        curated_by = 'xpo_partial' # ?

    if best_qnode.startswith('Q_'):
        wd_gaps_file.write(roleset + '\t' + best_qnode + '\n')
        continue
    else:
        m = re.search(pattern=q_pattern, string=best_qnode)
        if m:
            q = m.group()
            q2pb_file.write(q + '\t' + roleset + '\t' + curated_by + '\n')
        else:
            print(f'Error finding best Qnode for {roleset}')
            problem_file.write(roleset + '\n')

    if len(tokens) > 3 and len(second_best_qnode) > 0:
        if second_best_qnode.startswith('Q_'):
            # skip.
            print(f'Second-best Qnode identified as a WD gap for {roleset}.')
            problem_file.write(roleset + '\n')
            continue
        else:
            m = re.search(pattern=q_pattern, string=second_best_qnode)
            if m:
                q = m.group()
                # demote curated_by to xpo_partial??
                if curated_by == 'xpo':
                    curated_by = 'xpo_partial'
                    print(f'Second-best Qnode for {roleset} had annotation status GOLD but has been demoted to xpo_partial.')
                q2pb_file.write(q + '\t' + roleset + '\t' + curated_by + '\n')
            else:
                problem_file.write(roleset + '\n')
                print(f'Error finding second best Qnode for {roleset}')

q2pb_file.close()
f.close()
problem_file.close()
wd_gaps_file.close()