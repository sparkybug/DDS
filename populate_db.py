from app import db
from app.models import Disease, Symptom

# Create instances of Disease and Symptom
disease1 = Disease(disease='Common Cold')
symptom1 = Symptom(
    description='The Symtoms for Common Cold are  continuous_sneezing,  chills,  fatigue,  cough,  high_fever,  headache,  swelled_lymph_nodes,  malaise,  phlegm,  throat_irritation,  redness_of_eyes,  sinus_pressure,  runny_nose,  congestion,  chest_pain,  loss_of_smell,  muscle_pain',
    embedded_description='embedded_data_here')

symptom1.disease = disease1

# Add instances to the session and commit changes
db.session.add(disease1)
db.session.add(symptom1)
db.session.commit()

# Create instances of Disease and Symptom
disease2 = Disease(disease='Hypoglycemia')
symptom2 = Symptom(
    description='The Symtoms for Hypoglycemia are  vomiting,  fatigue,  anxiety,  sweating,  headache,  nausea,  blurred_and_distorted_vision,  excessive_hunger,  slurred_speech,  irritability,  palpitations,  drying_and_tingling_lips', embedded_description='embedded_data_here')
symptom2.disease = disease2

# Add instances to the session and commit changes
db.session.add(disease2)
db.session.add(symptom2)
db.session.commit()

# Create instances of Disease and Symptom
disease3 = Disease(disease='Malaria')
symptom3 = Symptom(
    description='The Symtoms for Malaria are  chills,  vomiting,  high_fever,  sweating,  headache,  nausea,  muscle_pain,  diarrhoea', embedded_description='embedded_data_here')
symptom3.disease = disease3

# Add instances to the session and commit changes
db.session.add(disease3)
db.session.add(symptom3)
db.session.commit()

# Create instances of Disease and Symptom
disease4 = Disease(disease='Peptic ulcer diseae')
symptom4 = Symptom(
    description='The Symtoms for Peptic ulcer diseae are  vomiting,  loss_of_appetite,  abdominal_pain,  passage_of_gases,  internal_itching,  indigestion', embedded_description='embedded_data_here')
symptom4.disease = disease4

# Add instances to the session and commit changes
db.session.add(disease4)
db.session.add(symptom4)
db.session.commit()

# Create instances of Disease and Symptom
disease5 = Disease(disease='Typhoid')
symptom5 = Symptom(
    description='The Symtoms for Typhoid are  chills,  vomiting,  fatigue,  high_fever,  nausea,  constipation,  abdominal_pain,  diarrhoea,  toxic_look_(typhos),  belly_pain,  headache', embedded_description='embedded_data_here')
symptom5.disease = disease5

# Add instances to the session and commit changes
db.session.add(disease5)
db.session.add(symptom5)
db.session.commit()

# Create instances of Disease and Symptom
disease6 = Disease(disease='Urinary tract infection')
symptom6 = Symptom(
    description='The Symtoms for Urinary tract infection are  burning_micturition,  bladder_discomfort,  foul_smell_of urine,  continuous_feel_of_urine',
    embedded_description='embedded_data_here')

symptom6.disease = disease6

# Add instances to the session and commit changes
db.session.add(disease6)
db.session.add(symptom6)
db.session.commit()

print('Database populated with initial data')