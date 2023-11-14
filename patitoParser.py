# Generated from patito.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO



from varfunctable import *
global funclist, quads
funclist = FuncTable()
quads = Cuadruplos()

global current_content, current_func, current_scope, current_type, current_var, various_vars, temporal_operator

current_var = ''
current_func = ''
current_type = ''
current_scope = 0
current_content = ''
various_vars = []
temporal_operator = ''


def serializedATN():
    return [
        4,1,34,292,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,44,8,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,67,8,2,10,2,12,2,70,
        9,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,78,8,2,11,2,12,2,79,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,
        100,8,4,10,4,12,4,103,9,4,5,4,105,8,4,10,4,12,4,108,9,4,1,4,1,4,
        1,4,3,4,113,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,5,5,123,8,5,10,5,
        12,5,126,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,135,8,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,153,8,8,
        1,8,1,8,1,8,5,8,158,8,8,10,8,12,8,161,9,8,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,169,8,9,1,9,1,9,1,9,5,9,174,8,9,10,9,12,9,177,9,9,1,10,1,10,
        1,10,1,10,1,10,1,10,3,10,185,8,10,1,10,1,10,1,10,5,10,190,8,10,10,
        10,12,10,193,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,206,8,11,1,11,1,11,1,11,3,11,211,8,11,1,11,1,11,1,11,
        3,11,216,8,11,3,11,218,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,
        12,227,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,238,
        8,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,5,15,259,8,15,10,15,12,15,262,
        9,15,3,15,264,8,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        3,16,275,8,16,1,16,1,16,1,16,1,16,3,16,281,8,16,5,16,283,8,16,10,
        16,12,16,286,9,16,1,16,1,16,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,0,1,1,0,8,9,306,0,34,1,0,0,0,2,37,
        1,0,0,0,4,59,1,0,0,0,6,81,1,0,0,0,8,83,1,0,0,0,10,120,1,0,0,0,12,
        134,1,0,0,0,14,136,1,0,0,0,16,144,1,0,0,0,18,162,1,0,0,0,20,178,
        1,0,0,0,22,217,1,0,0,0,24,226,1,0,0,0,26,228,1,0,0,0,28,242,1,0,
        0,0,30,253,1,0,0,0,32,268,1,0,0,0,34,35,3,2,1,0,35,36,5,0,0,1,36,
        1,1,0,0,0,37,38,5,1,0,0,38,39,6,1,-1,0,39,40,5,30,0,0,40,41,6,1,
        -1,0,41,43,5,2,0,0,42,44,3,4,2,0,43,42,1,0,0,0,43,44,1,0,0,0,44,
        48,1,0,0,0,45,47,3,8,4,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,
        0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,3,0,0,52,53,
        6,1,-1,0,53,54,6,1,-1,0,54,55,3,10,5,0,55,56,6,1,-1,0,56,57,5,4,
        0,0,57,58,6,1,-1,0,58,3,1,0,0,0,59,60,6,2,-1,0,60,77,5,5,0,0,61,
        62,5,30,0,0,62,68,6,2,-1,0,63,64,5,6,0,0,64,65,5,30,0,0,65,67,6,
        2,-1,0,66,63,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,
        71,1,0,0,0,70,68,1,0,0,0,71,72,5,7,0,0,72,73,3,6,3,0,73,74,6,2,-1,
        0,74,75,5,2,0,0,75,76,6,2,-1,0,76,78,1,0,0,0,77,61,1,0,0,0,78,79,
        1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,5,1,0,0,0,81,82,7,0,0,0,82,
        7,1,0,0,0,83,84,6,4,-1,0,84,85,5,10,0,0,85,86,6,4,-1,0,86,87,5,30,
        0,0,87,88,6,4,-1,0,88,106,5,11,0,0,89,90,5,30,0,0,90,91,5,7,0,0,
        91,92,3,6,3,0,92,101,6,4,-1,0,93,94,5,6,0,0,94,95,5,30,0,0,95,96,
        5,7,0,0,96,97,3,6,3,0,97,98,6,4,-1,0,98,100,1,0,0,0,99,93,1,0,0,
        0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,105,1,0,0,0,
        103,101,1,0,0,0,104,89,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,
        107,1,0,0,0,107,109,1,0,0,0,108,106,1,0,0,0,109,110,5,12,0,0,110,
        112,5,13,0,0,111,113,3,4,2,0,112,111,1,0,0,0,112,113,1,0,0,0,113,
        114,1,0,0,0,114,115,3,10,5,0,115,116,5,14,0,0,116,117,5,2,0,0,117,
        118,6,4,-1,0,118,119,6,4,-1,0,119,9,1,0,0,0,120,124,5,15,0,0,121,
        123,3,12,6,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,
        125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,16,0,0,128,
        11,1,0,0,0,129,135,3,14,7,0,130,135,3,26,13,0,131,135,3,28,14,0,
        132,135,3,30,15,0,133,135,3,32,16,0,134,129,1,0,0,0,134,130,1,0,
        0,0,134,131,1,0,0,0,134,132,1,0,0,0,134,133,1,0,0,0,135,13,1,0,0,
        0,136,137,5,30,0,0,137,138,6,7,-1,0,138,139,5,17,0,0,139,140,6,7,
        -1,0,140,141,3,16,8,0,141,142,6,7,-1,0,142,143,5,2,0,0,143,15,1,
        0,0,0,144,145,3,18,9,0,145,159,6,8,-1,0,146,147,5,18,0,0,147,153,
        6,8,-1,0,148,149,5,19,0,0,149,153,6,8,-1,0,150,151,5,20,0,0,151,
        153,6,8,-1,0,152,146,1,0,0,0,152,148,1,0,0,0,152,150,1,0,0,0,153,
        154,1,0,0,0,154,155,3,18,9,0,155,156,6,8,-1,0,156,158,1,0,0,0,157,
        152,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,
        17,1,0,0,0,161,159,1,0,0,0,162,163,3,20,10,0,163,175,6,9,-1,0,164,
        165,5,21,0,0,165,169,6,9,-1,0,166,167,5,22,0,0,167,169,6,9,-1,0,
        168,164,1,0,0,0,168,166,1,0,0,0,169,170,1,0,0,0,170,171,3,20,10,
        0,171,172,6,9,-1,0,172,174,1,0,0,0,173,168,1,0,0,0,174,177,1,0,0,
        0,175,173,1,0,0,0,175,176,1,0,0,0,176,19,1,0,0,0,177,175,1,0,0,0,
        178,179,3,22,11,0,179,191,6,10,-1,0,180,181,5,23,0,0,181,185,6,10,
        -1,0,182,183,5,24,0,0,183,185,6,10,-1,0,184,180,1,0,0,0,184,182,
        1,0,0,0,185,186,1,0,0,0,186,187,3,22,11,0,187,188,6,10,-1,0,188,
        190,1,0,0,0,189,184,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,
        192,1,0,0,0,192,21,1,0,0,0,193,191,1,0,0,0,194,195,5,11,0,0,195,
        196,6,11,-1,0,196,197,3,16,8,0,197,198,5,12,0,0,198,199,6,11,-1,
        0,199,218,1,0,0,0,200,205,6,11,-1,0,201,202,5,21,0,0,202,206,6,11,
        -1,0,203,204,5,22,0,0,204,206,6,11,-1,0,205,201,1,0,0,0,205,203,
        1,0,0,0,206,210,1,0,0,0,207,208,5,30,0,0,208,211,6,11,-1,0,209,211,
        3,24,12,0,210,207,1,0,0,0,210,209,1,0,0,0,211,218,1,0,0,0,212,213,
        5,30,0,0,213,216,6,11,-1,0,214,216,3,24,12,0,215,212,1,0,0,0,215,
        214,1,0,0,0,216,218,1,0,0,0,217,194,1,0,0,0,217,200,1,0,0,0,217,
        215,1,0,0,0,218,23,1,0,0,0,219,220,5,31,0,0,220,221,6,12,-1,0,221,
        227,6,12,-1,0,222,223,5,32,0,0,223,227,6,12,-1,0,224,225,5,33,0,
        0,225,227,6,12,-1,0,226,219,1,0,0,0,226,222,1,0,0,0,226,224,1,0,
        0,0,227,25,1,0,0,0,228,229,5,25,0,0,229,230,5,11,0,0,230,231,3,16,
        8,0,231,232,5,12,0,0,232,233,6,13,-1,0,233,237,3,10,5,0,234,235,
        5,26,0,0,235,236,6,13,-1,0,236,238,3,10,5,0,237,234,1,0,0,0,237,
        238,1,0,0,0,238,239,1,0,0,0,239,240,5,2,0,0,240,241,6,13,-1,0,241,
        27,1,0,0,0,242,243,5,27,0,0,243,244,6,14,-1,0,244,245,3,10,5,0,245,
        246,5,28,0,0,246,247,5,11,0,0,247,248,3,16,8,0,248,249,5,12,0,0,
        249,250,6,14,-1,0,250,251,5,2,0,0,251,252,6,14,-1,0,252,29,1,0,0,
        0,253,254,5,30,0,0,254,263,5,11,0,0,255,260,3,16,8,0,256,257,5,6,
        0,0,257,259,3,16,8,0,258,256,1,0,0,0,259,262,1,0,0,0,260,258,1,0,
        0,0,260,261,1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,263,255,1,0,
        0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,266,5,12,0,0,266,267,5,2,
        0,0,267,31,1,0,0,0,268,269,5,29,0,0,269,270,6,16,-1,0,270,274,5,
        11,0,0,271,272,5,33,0,0,272,275,6,16,-1,0,273,275,3,16,8,0,274,271,
        1,0,0,0,274,273,1,0,0,0,275,284,1,0,0,0,276,280,5,6,0,0,277,278,
        5,33,0,0,278,281,6,16,-1,0,279,281,3,16,8,0,280,277,1,0,0,0,280,
        279,1,0,0,0,281,283,1,0,0,0,282,276,1,0,0,0,283,286,1,0,0,0,284,
        282,1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,284,1,0,0,0,287,
        288,5,12,0,0,288,289,6,16,-1,0,289,290,5,2,0,0,290,33,1,0,0,0,26,
        43,48,68,79,101,106,112,124,134,152,159,168,175,184,191,205,210,
        215,217,226,237,260,263,274,280,284
    ]

class patitoParser ( Parser ):

    grammarFileName = "patito.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'var'", "','", "':'", "'int'", "'float'", "'void'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'='", "'>'", 
                     "'<'", "'!='", "'+'", "'-'", "'*'", "'/'", "'if'", 
                     "'else'", "'while'", "'do'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Id", "Cte_int", "Cte_float", 
                      "Cte_string", "WS" ]

    RULE_startRule = 0
    RULE_programa = 1
    RULE_vars = 2
    RULE_type = 3
    RULE_funcs = 4
    RULE_body = 5
    RULE_statement = 6
    RULE_assign = 7
    RULE_expression = 8
    RULE_exp = 9
    RULE_termino = 10
    RULE_factor = 11
    RULE_cte = 12
    RULE_condition = 13
    RULE_cycle = 14
    RULE_f_call = 15
    RULE_print = 16

    ruleNames =  [ "startRule", "programa", "vars", "type", "funcs", "body", 
                   "statement", "assign", "expression", "exp", "termino", 
                   "factor", "cte", "condition", "cycle", "f_call", "print" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    Id=30
    Cte_int=31
    Cte_float=32
    Cte_string=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programa(self):
            return self.getTypedRuleContext(patitoParser.ProgramaContext,0)


        def EOF(self):
            return self.getToken(patitoParser.EOF, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)




    def startRule(self):

        localctx = patitoParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.programa()
            self.state = 35
            self.match(patitoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token

        def Id(self):
            return self.getToken(patitoParser.Id, 0)

        def body(self):
            return self.getTypedRuleContext(patitoParser.BodyContext,0)


        def vars_(self):
            return self.getTypedRuleContext(patitoParser.VarsContext,0)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.FuncsContext)
            else:
                return self.getTypedRuleContext(patitoParser.FuncsContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = patitoParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(patitoParser.T__0)
            quads.quad_main_init()
            self.state = 39
            localctx._Id = self.match(patitoParser.Id)
            global current_func, current_scope; current_func = (None if localctx._Id is None else localctx._Id.text); funclist; funclist.add_function((None if localctx._Id is None else localctx._Id.text))
            self.state = 41
            self.match(patitoParser.T__1)

            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 42
                self.vars_()


            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 45
                self.funcs()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(patitoParser.T__2)
            quads.quad_main_set()
            current_scope+=1; 
            current_func = "main";
            funclist.add_function(current_func)
            self.state = 54
            self.body()
            current_scope-=1
            self.state = 56
            self.match(patitoParser.T__3)
            funclist.print_all_functions(); quads.printQuads()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._type = None # TypeContext

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.Id)
            else:
                return self.getToken(patitoParser.Id, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.TypeContext)
            else:
                return self.getTypedRuleContext(patitoParser.TypeContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = patitoParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            global current_content, current_func, current_scope, current_type, current_var, various_vars
            self.state = 60
            self.match(patitoParser.T__4)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                localctx._Id = self.match(patitoParser.Id)
                various_vars.append((None if localctx._Id is None else localctx._Id.text))
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 63
                    self.match(patitoParser.T__5)
                    self.state = 64
                    localctx._Id = self.match(patitoParser.Id)
                    various_vars.append((None if localctx._Id is None else localctx._Id.text))
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self.match(patitoParser.T__6)
                self.state = 72
                localctx._type = self.type_()
                current_type = (None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop))
                self.state = 74
                self.match(patitoParser.T__1)

                for myvar in various_vars: funclist.add_variable_to_function(current_func, myvar, current_type, current_scope, current_content);
                various_vars = [];

                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==30):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return patitoParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = patitoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._type = None # TypeContext

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.Id)
            else:
                return self.getToken(patitoParser.Id, i)

        def body(self):
            return self.getTypedRuleContext(patitoParser.BodyContext,0)


        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.TypeContext)
            else:
                return self.getTypedRuleContext(patitoParser.TypeContext,i)


        def vars_(self):
            return self.getTypedRuleContext(patitoParser.VarsContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = patitoParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            global current_content, current_func, current_scope, current_type, current_var
            self.state = 84
            self.match(patitoParser.T__9)
            current_scope+=1
            self.state = 86
            localctx._Id = self.match(patitoParser.Id)
            current_func = (None if localctx._Id is None else localctx._Id.text); funclist.add_function(current_func)
            self.state = 88
            self.match(patitoParser.T__10)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 89
                localctx._Id = self.match(patitoParser.Id)
                self.state = 90
                self.match(patitoParser.T__6)
                self.state = 91
                localctx._type = self.type_()
                current_var = (None if localctx._Id is None else localctx._Id.text); 
                current_type = (None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)); 
                funclist.add_variable_to_function(current_func, current_var, current_type, current_scope, current_content)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 93
                    self.match(patitoParser.T__5)
                    self.state = 94
                    localctx._Id = self.match(patitoParser.Id)
                    self.state = 95
                    self.match(patitoParser.T__6)
                    self.state = 96
                    localctx._type = self.type_()
                    current_var = (None if localctx._Id is None else localctx._Id.text); current_type = (None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)); 
                    funclist.add_variable_to_function(current_func, current_var, current_type, current_scope, current_content)
                    self.state = 103
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(patitoParser.T__11)
            self.state = 110
            self.match(patitoParser.T__12)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 111
                self.vars_()


            self.state = 114
            self.body()
            self.state = 115
            self.match(patitoParser.T__13)
            self.state = 116
            self.match(patitoParser.T__1)
            current_scope-=1;
            funclist.delete_all_variables(current_func)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.StatementContext)
            else:
                return self.getTypedRuleContext(patitoParser.StatementContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = patitoParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(patitoParser.T__14)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1778384896) != 0):
                self.state = 121
                self.statement()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(patitoParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(patitoParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(patitoParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(patitoParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(patitoParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(patitoParser.PrintContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = patitoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token

        def Id(self):
            return self.getToken(patitoParser.Id, 0)

        def expression(self):
            return self.getTypedRuleContext(patitoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = patitoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            localctx._Id = self.match(patitoParser.Id)

            quads.push_operate(funclist.get_variable_memory((None if localctx._Id is None else localctx._Id.text), current_scope), funclist.get_variable_type((None if localctx._Id is None else localctx._Id.text), current_scope), False, False, 0, '')

            self.state = 138
            self.match(patitoParser.T__16)

            quads.push_operator('=')

            self.state = 140
            self.expression()

            quads.quads_Assign()

            self.state = 142
            self.match(patitoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ExpContext)
            else:
                return self.getTypedRuleContext(patitoParser.ExpContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = patitoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.exp()

            quads.quads_Compare()

            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0):
                self.state = 152
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 146
                    self.match(patitoParser.T__17)

                    quads.push_operator('>')

                    pass
                elif token in [19]:
                    self.state = 148
                    self.match(patitoParser.T__18)

                    quads.push_operator('<')

                    pass
                elif token in [20]:
                    self.state = 150
                    self.match(patitoParser.T__19)

                    quads.push_operator('!=')

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 154
                self.exp()

                quads.quads_Compare()

                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.TerminoContext)
            else:
                return self.getTypedRuleContext(patitoParser.TerminoContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = patitoParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.termino()

            quads.quads_PlusMin()

            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 168
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [21]:
                    self.state = 164
                    self.match(patitoParser.T__20)

                    quads.push_operator('+')

                    pass
                elif token in [22]:
                    self.state = 166
                    self.match(patitoParser.T__21)

                    quads.push_operator('-')

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 170
                self.termino()

                quads.quads_PlusMin()

                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.FactorContext)
            else:
                return self.getTypedRuleContext(patitoParser.FactorContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = patitoParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.factor()

            quads.quads_MultDiv()

            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 184
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23]:
                    self.state = 180
                    self.match(patitoParser.T__22)

                    quads.push_operator('*')

                    pass
                elif token in [24]:
                    self.state = 182
                    self.match(patitoParser.T__23)

                    quads.push_operator('/')

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 186
                self.factor()

                quads.quads_MultDiv()

                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token

        def expression(self):
            return self.getTypedRuleContext(patitoParser.ExpressionContext,0)


        def Id(self):
            return self.getToken(patitoParser.Id, 0)

        def cte(self):
            return self.getTypedRuleContext(patitoParser.CteContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = patitoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(patitoParser.T__10)

                quads.push_FF()

                self.state = 196
                self.expression()
                self.state = 197
                self.match(patitoParser.T__11)

                quads.pop_FF()

                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 2)
                global temporal_operator
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [21]:
                    self.state = 201
                    self.match(patitoParser.T__20)
                    temporal_operator = '+'
                    pass
                elif token in [22]:
                    self.state = 203
                    self.match(patitoParser.T__21)
                    temporal_operator = '-'
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 210
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30]:
                    self.state = 207
                    localctx._Id = self.match(patitoParser.Id)

                    quads.push_operate(funclist.get_variable_memory((None if localctx._Id is None else localctx._Id.text), current_scope), funclist.get_variable_type((None if localctx._Id is None else localctx._Id.text), current_scope), False, False, (None if localctx._Id is None else localctx._Id.text), temporal_operator); temporal_operator = ''

                    pass
                elif token in [31, 32, 33]:
                    self.state = 209
                    self.cte()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [30, 31, 32, 33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [30]:
                    self.state = 212
                    localctx._Id = self.match(patitoParser.Id)

                    quads.push_operate(funclist.get_variable_memory((None if localctx._Id is None else localctx._Id.text), current_scope), funclist.get_variable_type((None if localctx._Id is None else localctx._Id.text), current_scope), False, False, (None if localctx._Id is None else localctx._Id.text), '')

                    pass
                elif token in [31, 32, 33]:
                    self.state = 214
                    self.cte()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Cte_int = None # Token
            self._Cte_float = None # Token
            self._Cte_string = None # Token

        def Cte_int(self):
            return self.getToken(patitoParser.Cte_int, 0)

        def Cte_float(self):
            return self.getToken(patitoParser.Cte_float, 0)

        def Cte_string(self):
            return self.getToken(patitoParser.Cte_string, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = patitoParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cte)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                localctx._Cte_int = self.match(patitoParser.Cte_int)
                global temporal_operator

                quads.push_operate((None if localctx._Cte_int is None else localctx._Cte_int.text), "int", True, False, 0, temporal_operator); temporal_operator = ''

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                localctx._Cte_float = self.match(patitoParser.Cte_float)

                quads.push_operate((None if localctx._Cte_float is None else localctx._Cte_float.text), "float", True, False, 0, temporal_operator); temporal_operator = ''

                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                localctx._Cte_string = self.match(patitoParser.Cte_string)

                quads.push_operate((None if localctx._Cte_string is None else localctx._Cte_string.text), "string", True, False, 0, temporal_operator); temporal_operator = ''

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(patitoParser.ExpressionContext,0)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.BodyContext)
            else:
                return self.getTypedRuleContext(patitoParser.BodyContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = patitoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(patitoParser.T__24)
            self.state = 229
            self.match(patitoParser.T__10)
            self.state = 230
            self.expression()
            self.state = 231
            self.match(patitoParser.T__11)

            quads.quad_if_1()

            self.state = 233
            self.body()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 234
                self.match(patitoParser.T__25)

                quads.quad_if_3()

                self.state = 236
                self.body()


            self.state = 239
            self.match(patitoParser.T__1)

            quads.quad_if_2()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(patitoParser.BodyContext,0)


        def expression(self):
            return self.getTypedRuleContext(patitoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = patitoParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(patitoParser.T__26)

            quads.quad_while_1()

            self.state = 244
            self.body()
            self.state = 245
            self.match(patitoParser.T__27)
            self.state = 246
            self.match(patitoParser.T__10)
            self.state = 247
            self.expression()
            self.state = 248
            self.match(patitoParser.T__11)

            quads.quad_while_return()

            self.state = 250
            self.match(patitoParser.T__1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(patitoParser.Id, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(patitoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)




    def f_call(self):

        localctx = patitoParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_f_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(patitoParser.Id)
            self.state = 254
            self.match(patitoParser.T__10)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16112420864) != 0):
                self.state = 255
                self.expression()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 256
                    self.match(patitoParser.T__5)
                    self.state = 257
                    self.expression()
                    self.state = 262
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 265
            self.match(patitoParser.T__11)
            self.state = 266
            self.match(patitoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Cte_string = None # Token

        def Cte_string(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.Cte_string)
            else:
                return self.getToken(patitoParser.Cte_string, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(patitoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = patitoParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(patitoParser.T__28)

            quads.push_operator('print')

            self.state = 270
            self.match(patitoParser.T__10)
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 271
                localctx._Cte_string = self.match(patitoParser.Cte_string)

                quads.push_operate((None if localctx._Cte_string is None else localctx._Cte_string.text), "string", True, False, 0, '')

                pass

            elif la_ == 2:
                self.state = 273
                self.expression()
                pass


            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 276
                self.match(patitoParser.T__5)
                self.state = 280
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 277
                    localctx._Cte_string = self.match(patitoParser.Cte_string)

                    quads.push_operate((None if localctx._Cte_string is None else localctx._Cte_string.text), "string", True, False, 0, '')

                    pass

                elif la_ == 2:
                    self.state = 279
                    self.expression()
                    pass


                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
            self.match(patitoParser.T__11)

            quads.quads_Print()

            self.state = 289
            self.match(patitoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





