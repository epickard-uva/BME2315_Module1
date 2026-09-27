import csv
from patient import *

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 
import pandas as pd
from sklearn.linear_model import LinearRegression

#lists female and male beta levels 

female_beta = []
male_beta  = []

#lists for patient ages and beta levels 
patient_age =[]
patient_beta = []

#creates object from csv file 
Patient.instantiate_from_csv(r"C:\Users\norac\OneDrive\Documents\CompBME\module 1\Module1_CompBME\Metadata and Protein Data for Module 1.csv")

#sorting by braak stage and prints 
Patient.all_patients.sort(key=Patient.get_braak, reverse=False)

for patient in Patient.all_patients:
    print(patient)

#filter for females with dementia 
dementia_females = Patient.filter(Patient.all_patients, sex = "Female", cognitive_status = "Dementia")

for patient in dementia_females: 
    print(patient)

#adds the the lists the values of patients' beta levels by sex
for patient in Patient.filter(Patient.all_patients, sex = "Female"):
    female_beta.append(patient.abeta42)
for patient in Patient.filter(Patient.all_patients, sex = "Male"):
    male_beta.append(patient.abeta42)

#calculating mean beta levels for each sex 
x_female_bar = statistics.mean(female_beta)
x_male_bar = statistics.mean(male_beta)

#calculates the standard deviation by sex 
beta_female_stdev = statistics.stdev(female_beta)
beta_male_stdev = statistics.stdev(male_beta)
 
print(f'Female mean = {x_female_bar}, Female stdev = {beta_female_stdev}')
print(f'Male mean = {x_male_bar}, Male stdev = {beta_male_stdev}')

#creating the data and bar graph details
Patient_sex_cols = ['Female', 'Male']

mean_sex = [x_female_bar, x_male_bar]

stdev_sex = [beta_female_stdev, beta_male_stdev]

yerr = [np.zeros(len(mean_sex)), stdev_sex]

#Run one-way ANOVA 
f_stat, p_value = stats.f_oneway(beta_female_stdev,beta_male_stdev )

# calculates p-value using independent t-test
t_stat, p_val = stats.ttest_ind(female_beta, male_beta)
print(f't_stat = {t_stat}, p_val = {p_val}')

plt.bar(Patient_sex_cols, mean_sex, yerr=yerr, capsize=10)

plt.title("Mean Amyloid-Beta42 Levels by Sex")
plt.xlabel("Sex")
plt.ylabel("Amyloid-Beta42 (pg/ug)")

y_max = max(mean_sex) + max(stdev_sex) * 0.4

plt.text(0.5, y_max,
         f"t = {t_stat:.2f}\np = {p_val:.3e}",
         ha='center',
         va='bottom')

plt.show()

#adds the ages of patients to list 
for patient in Patient.all_patients:
    patient_age.append(patient.age)

#adds the beta levels of patients to the list
for patient in Patient.all_patients:
    patient_beta.append(patient.abeta42)

#creating details for scatter plot like labels, etc 
X = [patient_age]
y = [patient_beta]

X = np.array(patient_age).reshape(-1, 1) 
y = np.array(patient_beta)

#for the linear regression 
model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)

#annotate equation 
equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"
plt.text(X.max() * 0.75, y.max() * 0.90, equation, color="red", fontsize=12, verticalalignment='top')

plt.xlabel('Age at Death')
plt.ylabel('Amyloid-Beta42 (pg/ug)')
plt.title('Scatter Plot of Amyloid-Beta42 vs Age at Death')
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color="red")
plt.show()

#Citation: I used AI to help clarify Python concepts, troubleshoot errors, and improve code documentation. 
#I wrote and adapted the code myself and reviewed the final code to ensure I understood it.



#trying to make changes to push to git  