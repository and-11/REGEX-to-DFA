
from collections import defaultdict

class State:
    def __init__(self,name):
        self.name = name
        self.epsilon = []
        self.transitions = defaultdict(list)  
        pass

class Fragment:
    def __init__(self,start,accept):
        self.start = start
        self.accept = accept
        pass

def literal(token):
    return token not in {'*', '+', '?', '|', '.'}

def postfix_to_nfa(postfix):
    stack = []
    counter = 0

    for token in postfix:
        if literal( token ) :
            s1 = State("q"+str(counter))
            counter+=1
            s2 = State("q"+str(counter))
            counter+=1

            s1.transitions[token].append(s2)

            stack.append( Fragment(s1,s2) )

        elif token == '.':
            f2 = stack.pop()
            f1 = stack.pop()
            
            f1.accept.epsilon.append(f2.start)
            stack.append( Fragment( f1.start,f2.accept ) )            # se modif

        elif token == '|':
            f2 = stack.pop()
            f1 = stack.pop()

            s1 = State("q"+str(counter))
            counter+=1
            s2 = State("q"+str(counter))
            counter+=1

            s1.epsilon.append( f1.start )
            s1.epsilon.append( f2.start )

            f1.accept.epsilon.append( s2 )
            f2.accept.epsilon.append( s2 )

            stack.append( Fragment(s1,s2) )

        elif token == '*':
            f = stack.pop()

            s1 = State("q"+str(counter))
            counter+=1
            s2 = State("q"+str(counter))
            counter+=1

            s1.epsilon.append( f.start )
            s1.epsilon.append( s2 )

            f.accept.epsilon.append( f.start )
            f.accept.epsilon.append( s2 )

            stack.append( Fragment(s1,s2) )

        elif token == '+':
            f = stack.pop()

            s1 = State("q"+str(counter))
            counter+=1
            s2 = State("q"+str(counter))
            counter+=1

            s1.epsilon.append( f.start )

            f.accept.epsilon.append( f.start )
            f.accept.epsilon.append( s2 )

            stack.append( Fragment(s1,s2) )

        elif token == '?':
            f = stack.pop()

            s1 = State("q"+str(counter))
            counter+=1
            s2 = State("q"+str(counter))
            counter+=1

            s1.epsilon.append( f.start )
            s1.epsilon.append( s2 )

            f.accept.epsilon.append( s2 )

            stack.append( Fragment(s1,s2) )

    nfa = {
        "states": set(),
        "alphabet": set(),
        "transitions": defaultdict( lambda : defaultdict(set) ),
        "start": "",
        "accept": set()
    }

    ans = stack[0]
    
    nfa["start"] = ans.start.name
    nfa["accept"].add( ans.accept.name )


    processed_states = set()
    unprocessed_states = set()
    
    unprocessed_states.add( ans.start )
    unprocessed_states.add( ans.accept )

    while len(unprocessed_states) > 0 :
        current = unprocessed_states.pop()
        if current.name in processed_states :
            continue
        processed_states.add( current.name )

        nfa["states"].add( current.name )
        for lit in current.transitions :
            nfa["alphabet"].add(lit)
            for x in current.transitions[lit] :
                nfa["transitions"][ current.name ][ lit ].add( x.name )
                if( x.name not in processed_states ):
                    unprocessed_states.add( x ) 

        # nfa["alphabet"].add(lit)                 epsilon ?
        for x in current.epsilon :
            nfa["transitions"][ current.name ][ "ε" ].add( x.name )
            if( x.name not in processed_states ):
                unprocessed_states.add( x ) 

    return nfa



# print(postfix_to_nfa( "ab." ) )

