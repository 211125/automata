states = {
        'q0': {'f': ('q1')},
        'q1': {'o': ('q2')},
        'q2': {'r': ('q3')},
        'q3': {'(': ('q4')},
        'q4': {' ': ('q5')},
        'q5': {'i': ('q6')},
        'q6': {'=': ('q7')},
        'q7': {'0': ('q8'), '1': ('q8', None), '2': ('q8', None), '3': ('q8', None), '4': ('q8', None), '5': ('q8', None), '6': ('q8', None), '7': ('q8', None), '8': ('q8', None), '9': ('q8', None)},
        'q8': {' ': ('q9')},
        'q9': {'<': ('q10')},
        'q10': {'=': ('q11')},
        'q11': {'0': ('q12'), '1': ('q12', None), '2': ('q12', None), '3': ('q12', None), '4': ('q12', None), '5': ('q12', None), '6': ('q12', None), '7': ('q12', None), '8': ('q12', None), '9': ('q12', None)},
        'q12': {';': ('q13')},
        'q13': {' ': ('q14')},
        'q14': {'j': ('q15')},
        'q15': {'+': ('q16')},
        'q16': {'=': ('q17')},
        'q17': {'0': ('q18'), '1': ('q18', None), '2': ('q18', None), '3': ('q18', None), '4': ('q18', None), '5': ('q18', None), '6': ('q18', None), '7': ('q18', None), '8': ('q18', None), '9': ('q18', None)},
        'q18': {')': ('q19')},
        'q19': {'{': ('q20')},
        'q20': {'}': ('q_accept')},
        'q_err': {}
    }

print(states[0])