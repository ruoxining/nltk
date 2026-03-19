"""Unofficial test with grammars."""
import argparse

from nltk.grammar import CFG, PCFG


def main():
    """Main procedure to test the grammars."""
    # init a grammar
    # TODO: no need to deal with no unary rules
    grammar = PCFG.fromstring("""
        S -> A B [0.4] | B A [0.6]
        B -> A B [0.2] | b [0.8]
        A -> a [1.0]
    """)
    # grammar = PCFG.fromstring("""
    #     S -> A B [0.4] | B A [0.6]
    #     B -> A [0.2] | b [0.8]
    #     A -> a [1.0]
    # """)

    # to cnf
    cnf = grammar.chomsky_normal_form()

    # cnf
    print(cnf.productions())


if __name__ == '__main__':
    main()
