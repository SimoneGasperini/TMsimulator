def parse_string(s, par='{}', sep=',', ret=set):
    s = s.strip(par[0]).strip(par[1])
    return ret(s.split(sep))


def parse_text(lines):
    lines = [l.strip('\n').replace(' ', '') for l in lines if l != '\n']
    for line in lines:
        if line.startswith('NUM_TAPES='):
            num_tapes = int(line.strip('NUM_TAPES='))
        elif line.startswith('ALPHABET='):
            alphabet = parse_string(line.strip('ALPHABET='))
        elif line.startswith('STATES='):
            states = parse_string(line.strip('STATES='))
        elif line.startswith('TRANSITION_FUNC='):
            transitions = lines[lines.index(line)+1:]
            break
    return num_tapes, alphabet, states, transitions


def get_delta_dict(transitions, alphabet):
    transitions_list = [t.replace('*', s) for s in alphabet
                        for t in transitions if '*' in t]
    transitions_list.extend([t for t in transitions if '*' not in t])
    delta_dict = {parse_string(string.split('-->')[0], par='()', ret=tuple):
                  parse_string(string.split('-->')[1], par='()', ret=tuple)
                  for string in transitions_list}
    return delta_dict
