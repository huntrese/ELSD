# Generated from Hello.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#r.
    def visitR(self, ctx:HelloParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#diabetesData.
    def visitDiabetesData(self, ctx:HelloParser.DiabetesDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#heartDiseaseData.
    def visitHeartDiseaseData(self, ctx:HelloParser.HeartDiseaseDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#sex.
    def visitSex(self, ctx:HelloParser.SexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#chestPainType.
    def visitChestPainType(self, ctx:HelloParser.ChestPainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#restingBP.
    def visitRestingBP(self, ctx:HelloParser.RestingBPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#cholesterol.
    def visitCholesterol(self, ctx:HelloParser.CholesterolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#fastingBS.
    def visitFastingBS(self, ctx:HelloParser.FastingBSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#restingECG.
    def visitRestingECG(self, ctx:HelloParser.RestingECGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#maxHR.
    def visitMaxHR(self, ctx:HelloParser.MaxHRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#exerciseAngina.
    def visitExerciseAngina(self, ctx:HelloParser.ExerciseAnginaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#oldpeak.
    def visitOldpeak(self, ctx:HelloParser.OldpeakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#stSlope.
    def visitStSlope(self, ctx:HelloParser.StSlopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#heartDisease.
    def visitHeartDisease(self, ctx:HelloParser.HeartDiseaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#diagnosis.
    def visitDiagnosis(self, ctx:HelloParser.DiagnosisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#treatment.
    def visitTreatment(self, ctx:HelloParser.TreatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#pregnancies.
    def visitPregnancies(self, ctx:HelloParser.PregnanciesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#glucose.
    def visitGlucose(self, ctx:HelloParser.GlucoseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#bloodPressure.
    def visitBloodPressure(self, ctx:HelloParser.BloodPressureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#skinThickness.
    def visitSkinThickness(self, ctx:HelloParser.SkinThicknessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#insulin.
    def visitInsulin(self, ctx:HelloParser.InsulinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#bmi.
    def visitBmi(self, ctx:HelloParser.BmiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#diabetesPedigreeFunction.
    def visitDiabetesPedigreeFunction(self, ctx:HelloParser.DiabetesPedigreeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#age.
    def visitAge(self, ctx:HelloParser.AgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HelloParser#outcome.
    def visitOutcome(self, ctx:HelloParser.OutcomeContext):
        return self.visitChildren(ctx)



del HelloParser