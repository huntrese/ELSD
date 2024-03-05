# Generated from Hello.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#r.
    def enterR(self, ctx:HelloParser.RContext):
        pass

    # Exit a parse tree produced by HelloParser#r.
    def exitR(self, ctx:HelloParser.RContext):
        pass


    # Enter a parse tree produced by HelloParser#patientInfo.
    def enterPatientInfo(self, ctx:HelloParser.PatientInfoContext):
        pass

    # Exit a parse tree produced by HelloParser#patientInfo.
    def exitPatientInfo(self, ctx:HelloParser.PatientInfoContext):
        pass


    # Enter a parse tree produced by HelloParser#diagnosis.
    def enterDiagnosis(self, ctx:HelloParser.DiagnosisContext):
        pass

    # Exit a parse tree produced by HelloParser#diagnosis.
    def exitDiagnosis(self, ctx:HelloParser.DiagnosisContext):
        pass


    # Enter a parse tree produced by HelloParser#treatment.
    def enterTreatment(self, ctx:HelloParser.TreatmentContext):
        pass

    # Exit a parse tree produced by HelloParser#treatment.
    def exitTreatment(self, ctx:HelloParser.TreatmentContext):
        pass


    # Enter a parse tree produced by HelloParser#pregnancies.
    def enterPregnancies(self, ctx:HelloParser.PregnanciesContext):
        pass

    # Exit a parse tree produced by HelloParser#pregnancies.
    def exitPregnancies(self, ctx:HelloParser.PregnanciesContext):
        pass


    # Enter a parse tree produced by HelloParser#glucose.
    def enterGlucose(self, ctx:HelloParser.GlucoseContext):
        pass

    # Exit a parse tree produced by HelloParser#glucose.
    def exitGlucose(self, ctx:HelloParser.GlucoseContext):
        pass


    # Enter a parse tree produced by HelloParser#bloodPressure.
    def enterBloodPressure(self, ctx:HelloParser.BloodPressureContext):
        pass

    # Exit a parse tree produced by HelloParser#bloodPressure.
    def exitBloodPressure(self, ctx:HelloParser.BloodPressureContext):
        pass


    # Enter a parse tree produced by HelloParser#skinThickness.
    def enterSkinThickness(self, ctx:HelloParser.SkinThicknessContext):
        pass

    # Exit a parse tree produced by HelloParser#skinThickness.
    def exitSkinThickness(self, ctx:HelloParser.SkinThicknessContext):
        pass


    # Enter a parse tree produced by HelloParser#insulin.
    def enterInsulin(self, ctx:HelloParser.InsulinContext):
        pass

    # Exit a parse tree produced by HelloParser#insulin.
    def exitInsulin(self, ctx:HelloParser.InsulinContext):
        pass


    # Enter a parse tree produced by HelloParser#bmi.
    def enterBmi(self, ctx:HelloParser.BmiContext):
        pass

    # Exit a parse tree produced by HelloParser#bmi.
    def exitBmi(self, ctx:HelloParser.BmiContext):
        pass


    # Enter a parse tree produced by HelloParser#diabetesPedigreeFunction.
    def enterDiabetesPedigreeFunction(self, ctx:HelloParser.DiabetesPedigreeFunctionContext):
        pass

    # Exit a parse tree produced by HelloParser#diabetesPedigreeFunction.
    def exitDiabetesPedigreeFunction(self, ctx:HelloParser.DiabetesPedigreeFunctionContext):
        pass


    # Enter a parse tree produced by HelloParser#age.
    def enterAge(self, ctx:HelloParser.AgeContext):
        pass

    # Exit a parse tree produced by HelloParser#age.
    def exitAge(self, ctx:HelloParser.AgeContext):
        pass


    # Enter a parse tree produced by HelloParser#outcome.
    def enterOutcome(self, ctx:HelloParser.OutcomeContext):
        pass

    # Exit a parse tree produced by HelloParser#outcome.
    def exitOutcome(self, ctx:HelloParser.OutcomeContext):
        pass



del HelloParser