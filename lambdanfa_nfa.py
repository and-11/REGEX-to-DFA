

from collections import defaultdict


def generate_epsilon_closure( lambdanfa, state_name ):
    ans = set()
    process = set()
    process.add( state_name )

    while len(process) > 0 :
        current = process.pop()
        if current in ans: 
            continue
        ans.add(current)

        for x in lambdanfa["transitions"].get(current, {}).get("ε", set()) :
             if x not in ans :
                process.add(x) 

    return ans


def lambdanfa_to_nfa( lambdanfa ):

    nfa = {
    "states": set(),
    "alphabet": set(),
    "transitions": defaultdict( lambda : defaultdict(set) ),
    "start": "",
    "accept": set()
    }
    
    epsilon_closure = defaultdict(set)

    for state in lambdanfa["states"]:
        epsilon_closure[ state ] = generate_epsilon_closure( lambdanfa,state )

    # # Step 2: build new transitions

    for state in lambdanfa["states"] :
        ec = epsilon_closure[ state ] 
        for nod in ec :
            for lit in lambdanfa["alphabet"] :
                for x in lambdanfa["transitions"].get(nod, {}).get(lit, set()):                
                    nfa["transitions"][state][lit].update( epsilon_closure[x] ) 

    # # Step 3: determine new accept states

    for state in lambdanfa["states"]:
        if epsilon_closure[state] & lambdanfa["accept"]:
            nfa["accept"].add(state)

    nfa["start"] = lambdanfa["start"]
    nfa["states"] = lambdanfa["states"]
    nfa["alphabet"] = lambdanfa["alphabet"]
    
    return nfa

# lambdanfa = {
#     "states": set(),
#     "alphabet": set(),
#     "transitions": defaultdict( lambda : defaultdict(set) ),
#     "start": "",
#     "accept": set()
# }

lambdanfa = {
    "states": {"q0","q1","q3","q2","q4","q5"},
    "alphabet": {"a","b"},
    "transitions": {
        "q0": {
            "a": {"q1"},
            "ε": {"q1"},
            "b": {"q3"}
        },
        "q1": {
            "ε": {"q2"}
        },
        "q2": {
            "ε": {"q5"},
            "a":{"q5"}
        },
        "q3": {
            "ε": {"q1"}
        },
        "q4": {
            "ε": {"q3"}
        },
        "q5": {
        }
    },
    "start": "q0",
    "accept": {"q5"}
}

# print( lambdanfa_to_nfa(lambdanfa) )
