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
        4,1,17,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,1,1,1,3,1,31,8,1,1,1,3,1,34,8,1,1,1,3,1,37,8,1,1,1,3,1,40,8,1,
        1,1,3,1,43,8,1,1,1,3,1,46,8,1,1,1,3,1,49,8,1,1,1,3,1,52,8,1,1,1,
        3,1,55,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,
        6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,
        24,0,0,85,0,26,1,0,0,0,2,28,1,0,0,0,4,56,1,0,0,0,6,59,1,0,0,0,8,
        62,1,0,0,0,10,65,1,0,0,0,12,68,1,0,0,0,14,71,1,0,0,0,16,74,1,0,0,
        0,18,77,1,0,0,0,20,80,1,0,0,0,22,83,1,0,0,0,24,86,1,0,0,0,26,27,
        3,2,1,0,27,1,1,0,0,0,28,30,5,1,0,0,29,31,3,8,4,0,30,29,1,0,0,0,30,
        31,1,0,0,0,31,33,1,0,0,0,32,34,3,10,5,0,33,32,1,0,0,0,33,34,1,0,
        0,0,34,36,1,0,0,0,35,37,3,12,6,0,36,35,1,0,0,0,36,37,1,0,0,0,37,
        39,1,0,0,0,38,40,3,14,7,0,39,38,1,0,0,0,39,40,1,0,0,0,40,42,1,0,
        0,0,41,43,3,16,8,0,42,41,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,
        46,3,18,9,0,45,44,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,49,3,20,
        10,0,48,47,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,52,3,22,11,0,51,
        50,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,55,3,24,12,0,54,53,1,0,
        0,0,54,55,1,0,0,0,55,3,1,0,0,0,56,57,5,2,0,0,57,58,5,16,0,0,58,5,
        1,0,0,0,59,60,5,3,0,0,60,61,5,16,0,0,61,7,1,0,0,0,62,63,5,4,0,0,
        63,64,5,14,0,0,64,9,1,0,0,0,65,66,5,5,0,0,66,67,5,15,0,0,67,11,1,
        0,0,0,68,69,5,6,0,0,69,70,5,15,0,0,70,13,1,0,0,0,71,72,5,7,0,0,72,
        73,5,15,0,0,73,15,1,0,0,0,74,75,5,8,0,0,75,76,5,15,0,0,76,17,1,0,
        0,0,77,78,5,9,0,0,78,79,5,15,0,0,79,19,1,0,0,0,80,81,5,10,0,0,81,
        82,5,15,0,0,82,21,1,0,0,0,83,84,5,11,0,0,84,85,5,14,0,0,85,23,1,
        0,0,0,86,87,5,12,0,0,87,88,5,14,0,0,88,25,1,0,0,0,9,30,33,36,39,
        42,45,48,51,54
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Patient:'", "'Diagnosis:'", "'Treatment:'", 
                     "'Pregnancies:'", "'Glucose:'", "'BloodPressure:'", 
                     "'SkinThickness:'", "'Insulin:'", "'BMI:'", "'DiabetesPedigreeFunction:'", 
                     "'Age:'", "'Outcome:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "TEXT", "WS" ]

    RULE_r = 0
    RULE_patientInfo = 1
    RULE_diagnosis = 2
    RULE_treatment = 3
    RULE_pregnancies = 4
    RULE_glucose = 5
    RULE_bloodPressure = 6
    RULE_skinThickness = 7
    RULE_insulin = 8
    RULE_bmi = 9
    RULE_diabetesPedigreeFunction = 10
    RULE_age = 11
    RULE_outcome = 12

    ruleNames =  [ "r", "patientInfo", "diagnosis", "treatment", "pregnancies", 
                   "glucose", "bloodPressure", "skinThickness", "insulin", 
                   "bmi", "diabetesPedigreeFunction", "age", "outcome" ]

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
    ID=13
    INT=14
    FLOAT=15
    TEXT=16
    WS=17

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.patientInfo()
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

        def pregnancies(self):
            return self.getTypedRuleContext(HelloParser.PregnanciesContext,0)


        def glucose(self):
            return self.getTypedRuleContext(HelloParser.GlucoseContext,0)


        def bloodPressure(self):
            return self.getTypedRuleContext(HelloParser.BloodPressureContext,0)


        def skinThickness(self):
            return self.getTypedRuleContext(HelloParser.SkinThicknessContext,0)


        def insulin(self):
            return self.getTypedRuleContext(HelloParser.InsulinContext,0)


        def bmi(self):
            return self.getTypedRuleContext(HelloParser.BmiContext,0)


        def diabetesPedigreeFunction(self):
            return self.getTypedRuleContext(HelloParser.DiabetesPedigreeFunctionContext,0)


        def age(self):
            return self.getTypedRuleContext(HelloParser.AgeContext,0)


        def outcome(self):
            return self.getTypedRuleContext(HelloParser.OutcomeContext,0)


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
            self.state = 28
            self.match(HelloParser.T__0)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 29
                self.pregnancies()


            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 32
                self.glucose()


            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 35
                self.bloodPressure()


            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 38
                self.skinThickness()


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 41
                self.insulin()


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 44
                self.bmi()


            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 47
                self.diabetesPedigreeFunction()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 50
                self.age()


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 53
                self.outcome()


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
        self.enterRule(localctx, 4, self.RULE_diagnosis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(HelloParser.T__1)
            self.state = 57
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
        self.enterRule(localctx, 6, self.RULE_treatment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(HelloParser.T__2)
            self.state = 60
            self.match(HelloParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PregnanciesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_pregnancies

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPregnancies" ):
                listener.enterPregnancies(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPregnancies" ):
                listener.exitPregnancies(self)




    def pregnancies(self):

        localctx = HelloParser.PregnanciesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pregnancies)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(HelloParser.T__3)
            self.state = 63
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlucoseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(HelloParser.FLOAT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_glucose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlucose" ):
                listener.enterGlucose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlucose" ):
                listener.exitGlucose(self)




    def glucose(self):

        localctx = HelloParser.GlucoseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_glucose)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(HelloParser.T__4)
            self.state = 66
            self.match(HelloParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloodPressureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(HelloParser.FLOAT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_bloodPressure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloodPressure" ):
                listener.enterBloodPressure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloodPressure" ):
                listener.exitBloodPressure(self)




    def bloodPressure(self):

        localctx = HelloParser.BloodPressureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bloodPressure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(HelloParser.T__5)
            self.state = 69
            self.match(HelloParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkinThicknessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(HelloParser.FLOAT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_skinThickness

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSkinThickness" ):
                listener.enterSkinThickness(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSkinThickness" ):
                listener.exitSkinThickness(self)




    def skinThickness(self):

        localctx = HelloParser.SkinThicknessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_skinThickness)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(HelloParser.T__6)
            self.state = 72
            self.match(HelloParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsulinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(HelloParser.FLOAT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_insulin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsulin" ):
                listener.enterInsulin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsulin" ):
                listener.exitInsulin(self)




    def insulin(self):

        localctx = HelloParser.InsulinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_insulin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(HelloParser.T__7)
            self.state = 75
            self.match(HelloParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BmiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(HelloParser.FLOAT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_bmi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBmi" ):
                listener.enterBmi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBmi" ):
                listener.exitBmi(self)




    def bmi(self):

        localctx = HelloParser.BmiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bmi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(HelloParser.T__8)
            self.state = 78
            self.match(HelloParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiabetesPedigreeFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(HelloParser.FLOAT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_diabetesPedigreeFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiabetesPedigreeFunction" ):
                listener.enterDiabetesPedigreeFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiabetesPedigreeFunction" ):
                listener.exitDiabetesPedigreeFunction(self)




    def diabetesPedigreeFunction(self):

        localctx = HelloParser.DiabetesPedigreeFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_diabetesPedigreeFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(HelloParser.T__9)
            self.state = 81
            self.match(HelloParser.FLOAT)
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
        self.enterRule(localctx, 22, self.RULE_age)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(HelloParser.T__10)
            self.state = 84
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutcomeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_outcome

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutcome" ):
                listener.enterOutcome(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutcome" ):
                listener.exitOutcome(self)




    def outcome(self):

        localctx = HelloParser.OutcomeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_outcome)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(HelloParser.T__11)
            self.state = 87
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





