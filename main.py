
from postfix_to_nfa import *
from lambdanfa_nfa import *
from regex_to_postfix import *
from nfa_to_dfa import *
from dfa_cheker import *

import json


# Citire
with open("LFA-Assignment2_Regex_DFA_v2.json", "r") as file:
    regex_data = json.load(file)



miss = 0

for regex_entry in regex_data :
    print(regex_entry['regex'])

    postfix_regex_text = to_postfix( regex_entry['regex'] )

    lambdanfa = postfix_to_nfa( postfix_regex_text )
    nfa = lambdanfa_to_nfa( lambdanfa )
    dfa = convert_nfa_to_dfa( nfa )

    for test in regex_entry[ "test_strings" ] :
        if Cuvant_Valid( test["input"],dfa["start"],dfa["transitions"],dfa["accept"] ) != test["expected"]:
            miss = miss+1
        
        print( test["input"] , end="    -> " )

        if Cuvant_Valid( test["input"],dfa["start"],dfa["transitions"],dfa["accept"] ) :
            print( "valid" )
        else :
            print( "invalid" )
        # print( "rasp este : ",test["expected"],"\n" )
    print()



print("\n\nThe program has", miss ,"mistakes")
