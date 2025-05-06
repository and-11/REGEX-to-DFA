
from collections import defaultdict



nfa = {
        "states": set(),
        "alphabet": set(),
        "transitions": defaultdict( lambda: defaultdict(list) ),            #schema lambda
        "start": "",
        "accept": set()
    }

print(nfa)