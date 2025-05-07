Regex to DFA Converter


Course: Formal Languages and Automata
Name: Turcu Andrei Cristian
Group: 152


Construct a deterministic finite automaton (DFA) equivalent to a given regular expression



Project Structure

├── regex_to_postfix.py       # Converts infix regex to postfix (Shunting Yard)
├── postfix_to_nfa.py         # Builds a λ-NFA from postfix expression (Thompson's algorithm)
├── lambdanfa_nfa.py          # Removes epsilon transitions (λ-NFA to NFA)
├── nfa_to_dfa.py             # Converts NFA to DFA (subset construction)
├── dfa_checker.py            # DFA simulator: checks if a string is accepted
├── main.py                   # Main script: processes regex, builds automata, runs tests
└── LFA-Assignment2_Regex_DFA_v2.json  # JSON file containing test cases



How to Run the Code

    Make sure you have Python 3.7 or later installed.

    Clone or download this repository.

    Run main : python3 main.py


The program will go through each regular expression, convert it to a DFA, and test all the specified strings using the DFA simulator, if the program made any mistakes this will be outputed in the end.


Design Decisions

    Shunting Yard Algorithm is used to convert infix expressions to postfix, simplifying parsing and operator precedence.

    Thompson’s Construction was chosen for building the NFA, due to its simplicity and direct mapping from postfix.

    Epsilon-closure + Subset Construction are applied to convert λ-NFA → NFA → DFA, following the classical theory.

    DFA simulation is implemented via a recursive function that checks the current state and transitions based on input.

    Test cases are stored in a JSON file, each containing the regex and input strings with expected outputs.