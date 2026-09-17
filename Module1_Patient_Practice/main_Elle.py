#Main code file for Patient Practice Module 1.
from patient import *



# #Sort and Print Patients based on age at death from youngest to oldest
Patient.all_patients.sort(key=lambda patient: patient.age_at_death)

for patient in Patient.all_patients:
    print(patient) 


#Testing class method for sorting patients with two attributes 
#Testing for subset of females with dementia 
subset = Patient.create_subset(
    "sex", "Female",ccx
    "cognitive_status", "Dementia"
)

print("SUBSET: Number of patients in subset:", len(subset))

for patient in subset:
    print(patient)

