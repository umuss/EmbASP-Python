# Generated from .\DatalogGrammar.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\37\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\3")
        buf.write("\3\3\5\3\33\n\3\3\4\3\4\3\4\2\2\5\2\4\6\2\3\3\2\6\b\2")
        buf.write("\36\2\13\3\2\2\2\4\16\3\2\2\2\6\34\3\2\2\2\b\n\5\4\3\2")
        buf.write("\t\b\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3")
        buf.write("\3\2\2\2\r\13\3\2\2\2\16\32\7\6\2\2\17\20\7\3\2\2\20\25")
        buf.write("\5\6\4\2\21\22\7\4\2\2\22\24\5\6\4\2\23\21\3\2\2\2\24")
        buf.write("\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2")
        buf.write("\27\25\3\2\2\2\30\31\7\5\2\2\31\33\3\2\2\2\32\17\3\2\2")
        buf.write("\2\32\33\3\2\2\2\33\5\3\2\2\2\34\35\t\2\2\2\35\7\3\2\2")
        buf.write("\2\5\13\25\32")
        return buf.getvalue()


class DatalogGrammarParser ( Parser ):

    grammarFileName = "DatalogGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "INTEGER", "STRING", "WHITESPACE" ]

    RULE_output = 0
    RULE_predicate_atom = 1
    RULE_term = 2

    ruleNames =  [ "output", "predicate_atom", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    IDENTIFIER=4
    INTEGER=5
    STRING=6
    WHITESPACE=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OutputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatalogGrammarParser.Predicate_atomContext)
            else:
                return self.getTypedRuleContext(DatalogGrammarParser.Predicate_atomContext,i)


        def getRuleIndex(self):
            return DatalogGrammarParser.RULE_output

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = DatalogGrammarParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DatalogGrammarParser.IDENTIFIER:
                self.state = 6
                self.predicate_atom()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predicate_atomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DatalogGrammarParser.IDENTIFIER, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DatalogGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(DatalogGrammarParser.TermContext,i)


        def getRuleIndex(self):
            return DatalogGrammarParser.RULE_predicate_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate_atom" ):
                return visitor.visitPredicate_atom(self)
            else:
                return visitor.visitChildren(self)




    def predicate_atom(self):

        localctx = DatalogGrammarParser.Predicate_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_predicate_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(DatalogGrammarParser.IDENTIFIER)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DatalogGrammarParser.T__0:
                self.state = 13
                self.match(DatalogGrammarParser.T__0)
                self.state = 14
                self.term()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DatalogGrammarParser.T__1:
                    self.state = 15
                    self.match(DatalogGrammarParser.T__1)
                    self.state = 16
                    self.term()
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 22
                self.match(DatalogGrammarParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DatalogGrammarParser.IDENTIFIER, 0)

        def INTEGER(self):
            return self.getToken(DatalogGrammarParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(DatalogGrammarParser.STRING, 0)

        def getRuleIndex(self):
            return DatalogGrammarParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = DatalogGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DatalogGrammarParser.IDENTIFIER) | (1 << DatalogGrammarParser.INTEGER) | (1 << DatalogGrammarParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





