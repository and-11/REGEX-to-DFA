
from postfix_to_nfa import *
from lambdanfa_nfa import *
from regex_to_postfix import *
from nfa_to_dfa import *
from dfa_cheker import *

import json


# Citire
with open("LFA-Assignment2_Regex_DFA_v2.json", "r") as file:
    regex_data = json.load(file)







regex_entry = regex_data[0]


postfix_regex_text = to_postfix( regex_entry['regex'] )
lambdanfa = postfix_to_nfa( postfix_regex_text )
nfa = lambdanfa_to_nfa( lambdanfa )
dfa = convert_nfa_to_dfa( nfa )


print(dfa)

# stare_c = ""
# if Cuvant_Valid( regex_entry["test_strings"][0],stare_c,dfa["transitions"],dfa["accept"] ) :
#     print( "valid" )
# else :
#     print( "invalid" )
# print( "rasp este : ",regex_entry["test_strings"][0]["expected"] )




print( postfix_regex_text ) 

# print(f"Testing regex: {regex_entry['name']} => {regex_entry['regex']}")
# for test in regex_entry["test_strings"]:
#     input_str = test["input"]
#     expected = test["expected"]
#     print(f"  Input: '{input_str}', Expected: {expected}")



# for regex_entry in regex_data:

#     print(f"Testing regex: {regex_entry['name']} => {regex_entry['regex']}")
#     for test in regex_entry["test_strings"]:
#         input_str = test["input"]
#         expected = test["expected"]
#         print(f"  Input: '{input_str}', Expected: {expected}")