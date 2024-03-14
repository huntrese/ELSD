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
        4,1,28,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,3,0,53,8,0,
        1,1,1,1,3,1,57,8,1,1,1,3,1,60,8,1,1,1,3,1,63,8,1,1,1,3,1,66,8,1,
        1,1,3,1,69,8,1,1,1,3,1,72,8,1,1,1,3,1,75,8,1,1,1,3,1,78,8,1,1,1,
        3,1,81,8,1,1,2,1,2,3,2,85,8,2,1,2,3,2,88,8,2,1,2,3,2,91,8,2,1,2,
        3,2,94,8,2,1,2,3,2,97,8,2,1,2,3,2,100,8,2,1,2,3,2,103,8,2,1,2,3,
        2,106,8,2,1,2,3,2,109,8,2,1,2,3,2,112,8,2,1,2,3,2,115,8,2,1,2,3,
        2,118,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,
        7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,
        1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,
        1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,
        1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,
        0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,0,0,182,0,52,1,0,0,0,2,54,1,0,0,0,4,82,1,0,0,0,6,119,
        1,0,0,0,8,122,1,0,0,0,10,125,1,0,0,0,12,128,1,0,0,0,14,131,1,0,0,
        0,16,134,1,0,0,0,18,137,1,0,0,0,20,140,1,0,0,0,22,143,1,0,0,0,24,
        146,1,0,0,0,26,149,1,0,0,0,28,152,1,0,0,0,30,155,1,0,0,0,32,158,
        1,0,0,0,34,161,1,0,0,0,36,164,1,0,0,0,38,167,1,0,0,0,40,170,1,0,
        0,0,42,173,1,0,0,0,44,176,1,0,0,0,46,179,1,0,0,0,48,182,1,0,0,0,
        50,53,3,2,1,0,51,53,3,4,2,0,52,50,1,0,0,0,52,51,1,0,0,0,53,1,1,0,
        0,0,54,56,5,1,0,0,55,57,3,32,16,0,56,55,1,0,0,0,56,57,1,0,0,0,57,
        59,1,0,0,0,58,60,3,34,17,0,59,58,1,0,0,0,59,60,1,0,0,0,60,62,1,0,
        0,0,61,63,3,36,18,0,62,61,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,
        66,3,38,19,0,65,64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,69,3,40,
        20,0,68,67,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,72,3,42,21,0,71,
        70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,75,3,44,22,0,74,73,1,0,
        0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,78,3,46,23,0,77,76,1,0,0,0,77,
        78,1,0,0,0,78,80,1,0,0,0,79,81,3,48,24,0,80,79,1,0,0,0,80,81,1,0,
        0,0,81,3,1,0,0,0,82,84,5,1,0,0,83,85,3,46,23,0,84,83,1,0,0,0,84,
        85,1,0,0,0,85,87,1,0,0,0,86,88,3,6,3,0,87,86,1,0,0,0,87,88,1,0,0,
        0,88,90,1,0,0,0,89,91,3,8,4,0,90,89,1,0,0,0,90,91,1,0,0,0,91,93,
        1,0,0,0,92,94,3,10,5,0,93,92,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,
        95,97,3,12,6,0,96,95,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,100,
        3,14,7,0,99,98,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,103,3,
        16,8,0,102,101,1,0,0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,106,3,
        18,9,0,105,104,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,109,3,
        20,10,0,108,107,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,112,
        3,22,11,0,111,110,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,115,
        3,24,12,0,114,113,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,118,
        3,26,13,0,117,116,1,0,0,0,117,118,1,0,0,0,118,5,1,0,0,0,119,120,
        5,2,0,0,120,121,5,24,0,0,121,7,1,0,0,0,122,123,5,3,0,0,123,124,5,
        24,0,0,124,9,1,0,0,0,125,126,5,4,0,0,126,127,5,24,0,0,127,11,1,0,
        0,0,128,129,5,5,0,0,129,130,5,24,0,0,130,13,1,0,0,0,131,132,5,6,
        0,0,132,133,5,24,0,0,133,15,1,0,0,0,134,135,5,7,0,0,135,136,5,24,
        0,0,136,17,1,0,0,0,137,138,5,8,0,0,138,139,5,24,0,0,139,19,1,0,0,
        0,140,141,5,9,0,0,141,142,5,24,0,0,142,21,1,0,0,0,143,144,5,10,0,
        0,144,145,5,25,0,0,145,23,1,0,0,0,146,147,5,11,0,0,147,148,5,24,
        0,0,148,25,1,0,0,0,149,150,5,12,0,0,150,151,5,24,0,0,151,27,1,0,
        0,0,152,153,5,13,0,0,153,154,5,28,0,0,154,29,1,0,0,0,155,156,5,14,
        0,0,156,157,5,28,0,0,157,31,1,0,0,0,158,159,5,15,0,0,159,160,5,24,
        0,0,160,33,1,0,0,0,161,162,5,16,0,0,162,163,5,25,0,0,163,35,1,0,
        0,0,164,165,5,17,0,0,165,166,5,25,0,0,166,37,1,0,0,0,167,168,5,18,
        0,0,168,169,5,25,0,0,169,39,1,0,0,0,170,171,5,19,0,0,171,172,5,25,
        0,0,172,41,1,0,0,0,173,174,5,20,0,0,174,175,5,25,0,0,175,43,1,0,
        0,0,176,177,5,21,0,0,177,178,5,25,0,0,178,45,1,0,0,0,179,180,5,22,
        0,0,180,181,5,24,0,0,181,47,1,0,0,0,182,183,5,23,0,0,183,184,5,24,
        0,0,184,49,1,0,0,0,22,52,56,59,62,65,68,71,74,77,80,84,87,90,93,
        96,99,102,105,108,111,114,117
    ]

class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Patient:'", "'Sex:'", "'ChestPainType:'", 
                     "'RestingBP:'", "'Cholesterol:'", "'FastingBS:'", "'RestingECG:'", 
                     "'MaxHR:'", "'ExerciseAngina:'", "'Oldpeak:'", "'ST_Slope:'", 
                     "'HeartDisease:'", "'Diagnosis:'", "'Treatment:'", 
                     "'Pregnancies:'", "'Glucose:'", "'BloodPressure:'", 
                     "'SkinThickness:'", "'Insulin:'", "'BMI:'", "'DiabetesPedigreeFunction:'", 
                     "'Age:'", "'Outcome:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "WS", "ID", "TEXT" ]

    RULE_r = 0
    RULE_diabetesData = 1
    RULE_heartDiseaseData = 2
    RULE_sex = 3
    RULE_chestPainType = 4
    RULE_restingBP = 5
    RULE_cholesterol = 6
    RULE_fastingBS = 7
    RULE_restingECG = 8
    RULE_maxHR = 9
    RULE_exerciseAngina = 10
    RULE_oldpeak = 11
    RULE_stSlope = 12
    RULE_heartDisease = 13
    RULE_diagnosis = 14
    RULE_treatment = 15
    RULE_pregnancies = 16
    RULE_glucose = 17
    RULE_bloodPressure = 18
    RULE_skinThickness = 19
    RULE_insulin = 20
    RULE_bmi = 21
    RULE_diabetesPedigreeFunction = 22
    RULE_age = 23
    RULE_outcome = 24

    ruleNames =  [ "r", "diabetesData", "heartDiseaseData", "sex", "chestPainType", 
                   "restingBP", "cholesterol", "fastingBS", "restingECG", 
                   "maxHR", "exerciseAngina", "oldpeak", "stSlope", "heartDisease", 
                   "diagnosis", "treatment", "pregnancies", "glucose", "bloodPressure", 
                   "skinThickness", "insulin", "bmi", "diabetesPedigreeFunction", 
                   "age", "outcome" ]

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
    INT=24
    FLOAT=25
    WS=26
    ID=27
    TEXT=28

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

        def diabetesData(self):
            return self.getTypedRuleContext(HelloParser.DiabetesDataContext,0)


        def heartDiseaseData(self):
            return self.getTypedRuleContext(HelloParser.HeartDiseaseDataContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR" ):
                return visitor.visitR(self)
            else:
                return visitor.visitChildren(self)




    def r(self):

        localctx = HelloParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 50
                self.diabetesData()
                pass

            elif la_ == 2:
                self.state = 51
                self.heartDiseaseData()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiabetesDataContext(ParserRuleContext):
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
            return HelloParser.RULE_diabetesData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiabetesData" ):
                listener.enterDiabetesData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiabetesData" ):
                listener.exitDiabetesData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiabetesData" ):
                return visitor.visitDiabetesData(self)
            else:
                return visitor.visitChildren(self)




    def diabetesData(self):

        localctx = HelloParser.DiabetesDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_diabetesData)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(HelloParser.T__0)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 55
                self.pregnancies()


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 58
                self.glucose()


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 61
                self.bloodPressure()


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 64
                self.skinThickness()


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 67
                self.insulin()


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 70
                self.bmi()


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 73
                self.diabetesPedigreeFunction()


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 76
                self.age()


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 79
                self.outcome()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeartDiseaseDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def age(self):
            return self.getTypedRuleContext(HelloParser.AgeContext,0)


        def sex(self):
            return self.getTypedRuleContext(HelloParser.SexContext,0)


        def chestPainType(self):
            return self.getTypedRuleContext(HelloParser.ChestPainTypeContext,0)


        def restingBP(self):
            return self.getTypedRuleContext(HelloParser.RestingBPContext,0)


        def cholesterol(self):
            return self.getTypedRuleContext(HelloParser.CholesterolContext,0)


        def fastingBS(self):
            return self.getTypedRuleContext(HelloParser.FastingBSContext,0)


        def restingECG(self):
            return self.getTypedRuleContext(HelloParser.RestingECGContext,0)


        def maxHR(self):
            return self.getTypedRuleContext(HelloParser.MaxHRContext,0)


        def exerciseAngina(self):
            return self.getTypedRuleContext(HelloParser.ExerciseAnginaContext,0)


        def oldpeak(self):
            return self.getTypedRuleContext(HelloParser.OldpeakContext,0)


        def stSlope(self):
            return self.getTypedRuleContext(HelloParser.StSlopeContext,0)


        def heartDisease(self):
            return self.getTypedRuleContext(HelloParser.HeartDiseaseContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_heartDiseaseData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeartDiseaseData" ):
                listener.enterHeartDiseaseData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeartDiseaseData" ):
                listener.exitHeartDiseaseData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeartDiseaseData" ):
                return visitor.visitHeartDiseaseData(self)
            else:
                return visitor.visitChildren(self)




    def heartDiseaseData(self):

        localctx = HelloParser.HeartDiseaseDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_heartDiseaseData)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(HelloParser.T__0)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 83
                self.age()


            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 86
                self.sex()


            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 89
                self.chestPainType()


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 92
                self.restingBP()


            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 95
                self.cholesterol()


            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 98
                self.fastingBS()


            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 101
                self.restingECG()


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 104
                self.maxHR()


            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 107
                self.exerciseAngina()


            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 110
                self.oldpeak()


            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 113
                self.stSlope()


            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 116
                self.heartDisease()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_sex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSex" ):
                listener.enterSex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSex" ):
                listener.exitSex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSex" ):
                return visitor.visitSex(self)
            else:
                return visitor.visitChildren(self)




    def sex(self):

        localctx = HelloParser.SexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(HelloParser.T__1)
            self.state = 120
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChestPainTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_chestPainType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChestPainType" ):
                listener.enterChestPainType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChestPainType" ):
                listener.exitChestPainType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChestPainType" ):
                return visitor.visitChestPainType(self)
            else:
                return visitor.visitChildren(self)




    def chestPainType(self):

        localctx = HelloParser.ChestPainTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_chestPainType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(HelloParser.T__2)
            self.state = 123
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestingBPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_restingBP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestingBP" ):
                listener.enterRestingBP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestingBP" ):
                listener.exitRestingBP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestingBP" ):
                return visitor.visitRestingBP(self)
            else:
                return visitor.visitChildren(self)




    def restingBP(self):

        localctx = HelloParser.RestingBPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_restingBP)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(HelloParser.T__3)
            self.state = 126
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CholesterolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_cholesterol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCholesterol" ):
                listener.enterCholesterol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCholesterol" ):
                listener.exitCholesterol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCholesterol" ):
                return visitor.visitCholesterol(self)
            else:
                return visitor.visitChildren(self)




    def cholesterol(self):

        localctx = HelloParser.CholesterolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cholesterol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(HelloParser.T__4)
            self.state = 129
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FastingBSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_fastingBS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFastingBS" ):
                listener.enterFastingBS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFastingBS" ):
                listener.exitFastingBS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFastingBS" ):
                return visitor.visitFastingBS(self)
            else:
                return visitor.visitChildren(self)




    def fastingBS(self):

        localctx = HelloParser.FastingBSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fastingBS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(HelloParser.T__5)
            self.state = 132
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestingECGContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_restingECG

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestingECG" ):
                listener.enterRestingECG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestingECG" ):
                listener.exitRestingECG(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestingECG" ):
                return visitor.visitRestingECG(self)
            else:
                return visitor.visitChildren(self)




    def restingECG(self):

        localctx = HelloParser.RestingECGContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_restingECG)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(HelloParser.T__6)
            self.state = 135
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaxHRContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_maxHR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaxHR" ):
                listener.enterMaxHR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaxHR" ):
                listener.exitMaxHR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaxHR" ):
                return visitor.visitMaxHR(self)
            else:
                return visitor.visitChildren(self)




    def maxHR(self):

        localctx = HelloParser.MaxHRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_maxHR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(HelloParser.T__7)
            self.state = 138
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExerciseAnginaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_exerciseAngina

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExerciseAngina" ):
                listener.enterExerciseAngina(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExerciseAngina" ):
                listener.exitExerciseAngina(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExerciseAngina" ):
                return visitor.visitExerciseAngina(self)
            else:
                return visitor.visitChildren(self)




    def exerciseAngina(self):

        localctx = HelloParser.ExerciseAnginaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exerciseAngina)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(HelloParser.T__8)
            self.state = 141
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OldpeakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(HelloParser.FLOAT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_oldpeak

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOldpeak" ):
                listener.enterOldpeak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOldpeak" ):
                listener.exitOldpeak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOldpeak" ):
                return visitor.visitOldpeak(self)
            else:
                return visitor.visitChildren(self)




    def oldpeak(self):

        localctx = HelloParser.OldpeakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_oldpeak)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(HelloParser.T__9)
            self.state = 144
            self.match(HelloParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StSlopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_stSlope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStSlope" ):
                listener.enterStSlope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStSlope" ):
                listener.exitStSlope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStSlope" ):
                return visitor.visitStSlope(self)
            else:
                return visitor.visitChildren(self)




    def stSlope(self):

        localctx = HelloParser.StSlopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stSlope)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(HelloParser.T__10)
            self.state = 147
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeartDiseaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_heartDisease

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeartDisease" ):
                listener.enterHeartDisease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeartDisease" ):
                listener.exitHeartDisease(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeartDisease" ):
                return visitor.visitHeartDisease(self)
            else:
                return visitor.visitChildren(self)




    def heartDisease(self):

        localctx = HelloParser.HeartDiseaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_heartDisease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(HelloParser.T__11)
            self.state = 150
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiagnosis" ):
                return visitor.visitDiagnosis(self)
            else:
                return visitor.visitChildren(self)




    def diagnosis(self):

        localctx = HelloParser.DiagnosisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_diagnosis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(HelloParser.T__12)
            self.state = 153
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTreatment" ):
                return visitor.visitTreatment(self)
            else:
                return visitor.visitChildren(self)




    def treatment(self):

        localctx = HelloParser.TreatmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_treatment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(HelloParser.T__13)
            self.state = 156
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPregnancies" ):
                return visitor.visitPregnancies(self)
            else:
                return visitor.visitChildren(self)




    def pregnancies(self):

        localctx = HelloParser.PregnanciesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pregnancies)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(HelloParser.T__14)
            self.state = 159
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlucose" ):
                return visitor.visitGlucose(self)
            else:
                return visitor.visitChildren(self)




    def glucose(self):

        localctx = HelloParser.GlucoseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_glucose)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(HelloParser.T__15)
            self.state = 162
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloodPressure" ):
                return visitor.visitBloodPressure(self)
            else:
                return visitor.visitChildren(self)




    def bloodPressure(self):

        localctx = HelloParser.BloodPressureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_bloodPressure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(HelloParser.T__16)
            self.state = 165
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkinThickness" ):
                return visitor.visitSkinThickness(self)
            else:
                return visitor.visitChildren(self)




    def skinThickness(self):

        localctx = HelloParser.SkinThicknessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_skinThickness)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(HelloParser.T__17)
            self.state = 168
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsulin" ):
                return visitor.visitInsulin(self)
            else:
                return visitor.visitChildren(self)




    def insulin(self):

        localctx = HelloParser.InsulinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_insulin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(HelloParser.T__18)
            self.state = 171
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBmi" ):
                return visitor.visitBmi(self)
            else:
                return visitor.visitChildren(self)




    def bmi(self):

        localctx = HelloParser.BmiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_bmi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(HelloParser.T__19)
            self.state = 174
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiabetesPedigreeFunction" ):
                return visitor.visitDiabetesPedigreeFunction(self)
            else:
                return visitor.visitChildren(self)




    def diabetesPedigreeFunction(self):

        localctx = HelloParser.DiabetesPedigreeFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_diabetesPedigreeFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(HelloParser.T__20)
            self.state = 177
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAge" ):
                return visitor.visitAge(self)
            else:
                return visitor.visitChildren(self)




    def age(self):

        localctx = HelloParser.AgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_age)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(HelloParser.T__21)
            self.state = 180
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutcome" ):
                return visitor.visitOutcome(self)
            else:
                return visitor.visitChildren(self)




    def outcome(self):

        localctx = HelloParser.OutcomeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_outcome)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(HelloParser.T__22)
            self.state = 183
            self.match(HelloParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





