from patient_elle import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 
import pandas as pd 
from sklearn.linear_model import LinearRegression 

# loading the dataset 
df = pd.read_csv("Metadata and Protein Data for Module 1.csv")

#calculating the observed dementia prevalence for each APOE genotype
apoe_genotypes = ['3_3', '3_4', '4_4']
observed_prevalence = []
for genotype in apoe_genotypes:
    genotype_data = df[df['APOE Genotype'] == genotype]
    dementia_count = (genotype_data['Cognitive Status'] == 'Dementia').sum()
    total_count = len(genotype_data)
    prevalence = dementia_count/total_count * 100
    observed_prevalence.append(prevalence)

print(observed_prevalence)

#chi square test 
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
#calculating error bars for risk ranges
error_lower = risk_mean - risk_lower
error_upper = risk_upper - risk_mean
yerr = [error_lower, error_upper]

# Create bar graphs with groups
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