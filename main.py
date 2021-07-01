from LexerParser import Lexer
from stackMachina import StackMachine
from LexerParser import Parser

if __name__ == '__main__':
    L = Lexer()
    L.get_term('test.txt')
    print('Tokens:', L.list_tokens)
    try:
        P = Parser(L.list_tokens)
        Tree = P.S()
        print('Tree:\n', Tree)
        StackMachine = StackMachine(Tree.children)
        StackMachine.start()
    except BaseException:
        print('Syntax error')
