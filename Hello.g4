grammar Hello;

r : patientInfo diagnosis treatment?;

patientInfo : 'Patient:' ID ID ID? age?;

age : 'Age:' INT;

diagnosis : 'Diagnosis:' TEXT;

treatment : 'Treatment:' TEXT;

ID : [a-zA-Z]+ ;
INT : [0-9]+ ;
TEXT : '"' (~["\r\n])* '"' ; 
WS : [ \t\r\n]+ -> skip ;
