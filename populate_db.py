from app import db
from app.models import Disease, Symptom

# Create instances of Disease and Symptom
disease1 = Disease(disease='Common Cold')
symptom1 = Symptom(description='Runny nose', encoded_description='encoded_data_here')
symptom1.disease = disease1

# Add instances to the session and commit changes
db.session.add(disease1)
db.session.add(symptom1)
db.session.commit()

disease2 = Disease(disease='Common Cold')
symptom2 = Symptom(description='Runny nose', encoded_description='encoded_data_here')
symptom2.disease = disease2

# Add instances to the session and commit changes
db.session.add(disease2)
db.session.add(symptom2)
db.session.commit()

disease3 = Disease(disease='Common Cold')
symptom3 = Symptom(description='Runny nose', encoded_description='encoded_data_here')
symptom3.disease = disease3

# Add instances to the session and commit changes
db.session.add(disease3)
db.session.add(symptom3)
db.session.commit()

disease4 = Disease(disease='Common Cold')
symptom4 = Symptom(description='Runny nose', encoded_description='encoded_data_here')
symptom4.disease = disease4

# Add instances to the session and commit changes
db.session.add(disease4)
db.session.add(symptom4)
db.session.commit()

disease5 = Disease(disease='Common Cold')
symptom5 = Symptom(description='Runny nose', encoded_description='encoded_data_here')
symptom5.disease = disease5

# Add instances to the session and commit changes
db.session.add(disease5)
db.session.add(symptom5)
db.session.commit()

print('Database populated with initial data')