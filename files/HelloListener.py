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


    # Enter a parse tree produced by HelloParser#age.
    def enterAge(self, ctx:HelloParser.AgeContext):
        pass

    # Exit a parse tree produced by HelloParser#age.
    def exitAge(self, ctx:HelloParser.AgeContext):
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



del HelloParser