grammar Hello;

r : (diabetesData | heartDiseaseData)  ;
diabetesData : 'Patient:' pregnancies? glucose? bloodPressure? skinThickness? insulin? bmi? diabetesPedigreeFunction? age? outcome?;

heartDiseaseData : 'Patient:' age? sex? chestPainType? restingBP? cholesterol? fastingBS? restingECG? maxHR? exerciseAngina? oldpeak? stSlope? heartDisease?;

sex : 'Sex:' INT;
chestPainType : 'ChestPainType:' INT;
restingBP : 'RestingBP:' INT;
cholesterol : 'Cholesterol:' INT;
fastingBS : 'FastingBS:' INT;
restingECG : 'RestingECG:' INT;
maxHR : 'MaxHR:' INT;
exerciseAngina : 'ExerciseAngina:' INT;
oldpeak : 'Oldpeak:' FLOAT;
stSlope : 'ST_Slope:' INT;
heartDisease : 'HeartDisease:' INT;
diagnosis : 'Diagnosis:' TEXT;
treatment : 'Treatment:' TEXT;

pregnancies : 'Pregnancies:' INT;
glucose : 'Glucose:' FLOAT;
bloodPressure : 'BloodPressure:' FLOAT;
skinThickness : 'SkinThickness:' FLOAT;
insulin : 'Insulin:' FLOAT;
bmi : 'BMI:' FLOAT;
diabetesPedigreeFunction : 'DiabetesPedigreeFunction:' FLOAT;
age : 'Age:' INT;
outcome : 'Outcome:' INT;



INT : [0-9]+ ;
FLOAT : [0-9]+('.'[0-9]+)?;
WS : [ \t\r\n]+ -> skip ;
ID : [a-zA-Z]+ ;
TEXT : '"' (~["\r\n])* '"' ; 
