#Main code file for Patient Practice Module 1.
from patient_elle import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 
import pandas as pd 
from sklearn.linear_model import LinearRegression 

#Using class method to sorting for patients in a subset
#Creating lists to hold subset APOE genotypes for grouping 
subset_2 = Patient.create_subset(
    "apoe_genotype", "2_3",
    "apoe_genotype", "2_3"
)
subset_3 = Patient.create_subset(
    "apoe_genotype", "2_2",
    "apoe_genotype", "2_2"
)
subset_4 = Patient.create_subset(
    "apoe_genotype", "2_4",
    "apoe_genotype", "2_4"
)
apoe_2 = subset_2 + subset_3 + subset_4

apoe_3_3 = Patient.create_subset(
    "apoe_genotype", "3_3",
    "apoe_genotype", "3_3"
)

apoe_3_4 = Patient.create_subset(
    "apoe_genotype", "3_4",
    "apoe_genotype", "3_4"
)

apoe_4_4 = Patient.create_subset(
    "apoe_genotype", "4_4",
    "apoe_genotype", "4_4"
)

# Make a bar graph that compares the mean (+/- standard deviation) of an attribute 


#Filtering and getting mean/stdev of subset data
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

#Statistical Significance
#Run a one-way ANOVA for the bar graphs 
f_stat, p_value = stats.f_oneway(age_dementia_female, age_dementia_male)
print("f-statistic:", f_stat)
print("p_value:", p_value)

# Creating bar graph for mean age of dementia diagnosis by gender
plt.bar(patient_groups_cols, mean_sex, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Age of Dementia Diagnosis by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Age (years)")
plt.text(0.5, max(mean_sex) + 5, f"One-way_ANOVA: p = {p_value:.3f}", ha='center', fontsize=9)
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
        and patient.abeta42 != "Unavailable"):

        patient_brain_weight.append(float(patient.fresh_brain_weight))
        patient_amyloid_beta_42.append(float(patient.abeta42))


X = [patient_brain_weight]
Y = [patient_amyloid_beta_42]


#Statistical Significance
#Linear Regression

X = np.array(patient_brain_weight, dtype=float).reshape(-1, 1)
Y = np.array(patient_amyloid_beta_42, dtype=float)

model = LinearRegression()
model.fit(X, Y)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, Y)

#Annotate the equation 
equation = f"y = {slope:.2f}x + {intercept:.2f}\nR^2 = {r2:.2f}"

plt.text(
    0.95, 0.95,
    equation,
    transform=plt.gca().transAxes,
    ha='right',
    va='top',
    color="red",
    fontsize=12
)

plt.scatter(X, Y, color='blue')
plt.plot(X, model.predict(X), color="red")
plt.xlabel('Fresh Brain Weight')
plt.ylabel('Amyloid-Beta42 Levels')
plt.title('Scatter Plot of Fresh Brain Weight vs Amyloid-Beta42 Levels')
plt.show()
#BEGINNING OF MY CODE 
# calculating the number of people with dementia for each genotype 
df = pd.read_csv("Metadata and Protein Data for Module 1.csv")
apoe_genotypes = ['3_3', '3_4', '4_4']
observed_prevalence = []
for genotype in apoe_genotypes:
    genotype_data = df[df['APOE Genotype'] == genotype]
    dementia_count = (genotype_data['Cognitive Status'] == 'Dementia').sum()
    total_count = len(genotype_data)
    prevalence = dementia_count/total_count * 100
    observed_prevalence.append(prevalence)

print(observed_prevalence)
#chi square test for statistical analysis 
apoe_data = df[df['APOE Genotype'].isin(['3_3', '3_4', '4_4'])]
contingency_table = pd.crosstab(
    apoe_data['APOE Genotype'],
    apoe_data['Cognitive Status'] == 'Dementia'
)
print("Contingency Table: ")
print(contingency_table)
chi2, p_value, degrees_of_freedom, expected = stats.chi2_contingency(
    contingency_table
)
print("\nChi-square test results:")
print("Chi-square statistic:", chi2)
print("Degrees of freedom:", degrees_of_freedom)
print("p-value:", p_value)
#creating bar graph that shows apoe genotype vs lifetime dementia risk %
#lifetime risk ranges from internet source 
apoe_genotypes = ['3_3', '3_4', '4_4']
risk_lower = np.array([10, 20, 30])
risk_upper = np.array([15, 25, 55])
risk_mean = (risk_lower + risk_upper)/2 #calculating midpoint for each risk range 
error_lower = risk_mean - risk_lower
error_upper = risk_upper - risk_mean
#creating error bars
yerr = [error_lower, error_upper]

# Create grouped bar graph
x = np.arange(len(apoe_genotypes))
width = 0.35

plt.bar(
    x - width/2,
    observed_prevalence,
    width,
    label="Observed dementia prevalence"
)

plt.bar(
    x + width/2,
    risk_mean,
    width,
    yerr=yerr,
    capsize=8,
    label="Reported lifetime risk"
)

plt.xticks(x, apoe_genotypes)
plt.xlabel("APOE Genotype")
plt.ylabel("Dementia Risk/Prevalence (%)")
plt.title("Observed Dementia Prevalence vs. Reported Lifetime Risk by APOE Genotype")
plt.legend()
plt.text(
    0.5, 0.95, 
    f"Chi-square p-value = {p_value:.4f}",
    transform =plt.gca().transAxes,
    ha='center'
)

plt.show()
#Used chat for code above to help plot 
##