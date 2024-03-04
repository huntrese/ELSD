# Generated from Hello.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,3,0,
        14,8,0,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,3,1,23,8,1,1,2,1,2,1,2,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,31,0,10,1,0,0,0,2,15,
        1,0,0,0,4,24,1,0,0,0,6,27,1,0,0,0,8,30,1,0,0,0,10,11,3,2,1,0,11,
        13,3,6,3,0,12,14,3,8,4,0,13,12,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,
        0,15,16,5,1,0,0,16,17,5,5,0,0,17,19,5,5,0,0,18,20,5,5,0,0,19,18,
        1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,23,3,4,2,0,22,21,1,0,0,0,
        22,23,1,0,0,0,23,3,1,0,0,0,24,25,5,2,0,0,25,26,5,6,0,0,26,5,1,0,
        0,0,27,28,5,3,0,0,28,29,5,7,0,0,29,7,1,0,0,0,30,31,5,4,0,0,31,32,
        5,7,0,0,32,9,1,0,0,0,3,13,19,22
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Patient:'", "'Age:'", "'Diagnosis:'", 
                     "'Treatment:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "TEXT", "WS" ]

    RULE_r = 0
    RULE_patientInfo = 1
    RULE_age = 2
    RULE_diagnosis = 3
    RULE_treatment = 4

    ruleNames =  [ "r", "patientInfo", "age", "diagnosis", "treatment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    INT=6
    TEXT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def patientInfo(self):
            return self.getTypedRuleContext(HelloParser.PatientInfoContext,0)


        def diagnosis(self):
            return self.getTypedRuleContext(HelloParser.DiagnosisContext,0)


        def treatment(self):
            return self.getTypedRuleContext(HelloParser.TreatmentContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)




    def r(self):

        localctx = HelloParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.patientInfo()
            self.state = 11
            self.diagnosis()
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 12
                self.treatment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatientInfoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.ID)
            else:
                return self.getToken(HelloParser.ID, i)

        def age(self):
            return self.getTypedRuleContext(HelloParser.AgeContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_patientInfo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatientInfo" ):
                listener.enterPatientInfo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatientInfo" ):
                listener.exitPatientInfo(self)




    def patientInfo(self):

        localctx = HelloParser.PatientInfoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_patientInfo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(HelloParser.T__0)
            self.state = 16
            self.match(HelloParser.ID)
            self.state = 17
            self.match(HelloParser.ID)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 18
                self.match(HelloParser.ID)


            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 21
                self.age()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_age

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAge" ):
                listener.enterAge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAge" ):
                listener.exitAge(self)




    def age(self):

        localctx = HelloParser.AgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_age)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(HelloParser.T__1)
            self.state = 25
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiagnosisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(HelloParser.TEXT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_diagnosis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagnosis" ):
                listener.enterDiagnosis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagnosis" ):
                listener.exitDiagnosis(self)




    def diagnosis(self):

        localctx = HelloParser.DiagnosisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_diagnosis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(HelloParser.T__2)
            self.state = 28
            self.match(HelloParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TreatmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(HelloParser.TEXT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_treatment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTreatment" ):
                listener.enterTreatment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTreatment" ):
                listener.exitTreatment(self)




    def treatment(self):

        localctx = HelloParser.TreatmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_treatment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(HelloParser.T__3)
            self.state = 31
            self.match(HelloParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





