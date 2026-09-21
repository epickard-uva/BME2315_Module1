#Main code file for Patient Practice Module 1.
from patient_elle import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 


# #Sort and Print Patients based on age at death from youngest to oldest
Patient.all_patients.sort(key=lambda patient: patient.age_at_death)

for patient in Patient.all_patients:
    print(patient) 


#Testing class method for sorting patients with two attributes 
#Testing for subset of patients with APOE Genotype 3_4 and cognitive status Dementia
subset = Patient.create_subset(
    "apoe_genotype", "3_4",
    "cognitive_status", "Dementia"
)

print("\n SUBSET: Number of patients in subset:", len(subset))

for patient in subset:
    print(patient)


# Make a bar graph that compares the mean (+/- standard deviation) of an attribute 
# that you are interested in between female and male patients (e.g. Amyloid-Beta42 levels in female vs. male patients with dementia)

#Creating lists to hold subset
age_dementia_female = []
age_dementia_male = []

#Filtering and getting mean/stdev of subset data
for patient in Patient.all_patients:
    if patient.sex == "Female" and patient.age_of_dementia_diagnosis != "":
        age_dementia_female.append(int(patient.age_of_dementia_diagnosis))
    elif patient.sex == "Male" and patient.age_of_dementia_diagnosis != "":
        age_dementia_male.append(int(patient.age_of_dementia_diagnosis))

x_age_dementia_female = (statistics.mean(age_dementia_female))
x_age_dementia_male = (statistics.mean(age_dementia_male))
age_dementia_female_stdev = (statistics.stdev(age_dementia_female))
age_dementia_male_stdev = (statistics.stdev(age_dementia_male))

print(f'x_age_dementia_female = {x_age_dementia_female}, age_dementia_female_stdev = {age_dementia_female_stdev}')
print(f'x_age_dementia_male = {x_age_dementia_male}, age_dementia_male_stdev = {age_dementia_male_stdev}')

patient_groups_cols = ['Female', 'Male']
mean_sex = [x_age_dementia_female, x_age_dementia_male]
stdev_sex = [age_dementia_female_stdev, age_dementia_male_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]


#Creating bar graph for mean age of dementia diagnosis by gender
plt.bar(patient_groups_cols, mean_sex, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Age of Dementia Diagnosis by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Age (years)")
plt.text(
    0,
    x_age_dementia_female + 11,
    f"{x_age_dementia_female:.2f}",
    ha='center'
)
plt.text(
    1,
    x_age_dementia_male + 12,
    f"{x_age_dementia_male:.2f}",
    ha='center'
)
plt.show()



#Creating a scatter plot to visualize relationship between fresh brain weight and amyloid-beta 42 levels in patients
patient_brain_weight = []
patient_amyloid_beta_42 = []

for patient in Patient.all_patients:
    if (patient.fresh_brain_weight != "" 
        and patient.fresh_brain_weight != "Unavailable"
        and patient.abeta42 != ""
        and patient.abeta42 != "Unavailable" 
        and float(patient.abeta42) < 600): #Exlcuded outliers to see graph and relationship better 

        patient_brain_weight.append(float(patient.fresh_brain_weight))
        patient_amyloid_beta_42.append(float(patient.abeta42))


X = [patient_brain_weight]
Y = [patient_amyloid_beta_42]


plt.scatter(X, Y, color='blue')
plt.xlabel('Fresh Brain Weight')
plt.ylabel('Amyloid-Beta42 Levels')
plt.title('Scatter Plot of Fresh Brain Weight vs Amyloid-Beta42 Levels')
plt.show()

