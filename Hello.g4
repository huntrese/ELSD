grammar Hello;

r : patientInfo  ;
patientInfo : 'Patient:' pregnancies? glucose? bloodPressure? skinThickness? insulin? bmi? diabetesPedigreeFunction? age? outcome?;
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

ID : [a-zA-Z]+ ;
INT : [0-9]+ ;
FLOAT : [0-9]+('.'[0-9]+)?;
TEXT : '"' (~["\r\n])* '"' ; 
WS : [ \t\r\n]+ -> skip ;
