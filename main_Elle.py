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
# Analysis #2 (Calculating mean ab-42 and mean pTau per genotype)

# AB42 subsets
ab_2 = [float(patient.abeta42) for patient in apoe_2 
        if patient.abeta42 != "Unavailable" and patient.abeta42 != ""]
ab_3_3 = [float(patient.abeta42) for patient in apoe_3_3 
          if patient.abeta42 != "Unavailable" and patient.abeta42 != ""]
ab_3_4 = [float(patient.abeta42) for patient in apoe_3_4 
          if patient.abeta42 != "Unavailable" and patient.abeta42 != ""]
ab_4_4 = [float(patient.abeta42) for patient in apoe_4_4 
          if patient.abeta42 != "Unavailable" and patient.abeta42 != ""]

# Mean AB42
mean_ab_2 = statistics.mean(ab_2)
mean_ab_3_3 = statistics.mean(ab_3_3)
mean_ab_3_4 = statistics.mean(ab_3_4)
mean_ab_4_4 = statistics.mean(ab_4_4)

# Stdev AB42
stdev_ab_2 = statistics.stdev(ab_2)
stdev_ab_3_3 = statistics.stdev(ab_3_3)
stdev_ab_3_4 = statistics.stdev(ab_3_4)
stdev_ab_4_4 = statistics.stdev(ab_4_4)

# pTau subsets
ptau_2 = [float(patient.ptau) for patient in apoe_2 
          if patient.ptau != "Unavailable" and patient.ptau != ""]
ptau_3_3 = [float(patient.ptau) for patient in apoe_3_3 
            if patient.ptau != "Unavailable" and patient.ptau != ""]
ptau_3_4 = [float(patient.ptau) for patient in apoe_3_4 
            if patient.ptau != "Unavailable" and patient.ptau != ""]
ptau_4_4 = [float(patient.ptau) for patient in apoe_4_4 
            if patient.ptau != "Unavailable" and patient.ptau != ""]

# Mean pTau
mean_ptau_2 = statistics.mean(ptau_2)
mean_ptau_3_3 = statistics.mean(ptau_3_3)
mean_ptau_3_4 = statistics.mean(ptau_3_4)
mean_ptau_4_4 = statistics.mean(ptau_4_4)

# Stdev pTau
stdev_ptau_2 = statistics.stdev(ptau_2)
stdev_ptau_3_3 = statistics.stdev(ptau_3_3)
stdev_ptau_3_4 = statistics.stdev(ptau_3_4)
stdev_ptau_4_4 = statistics.stdev(ptau_4_4)

# ---------------------------------------------------------
# Mean AB42 Bar graph
# ---------------------------------------------------------

#One-way ANOVA
f_stat_ab, p_value_ab = stats.f_oneway(
    ab_2,
    ab_3_3,
    ab_3_4,
    ab_4_4
)
print("AB42 f-statistic:", f_stat_ab)
print("AB42 p_value:", p_value_ab)

# AB42 bar graph
mean_ab = [mean_ab_2, mean_ab_3_3, mean_ab_3_4, mean_ab_4_4]
stdev_ab = [stdev_ab_2, stdev_ab_3_3, stdev_ab_3_4, stdev_ab_4_4]
plt.bar(
    genotypes,
    mean_ab,
    yerr=stdev_ab,
    capsize=10,
    color=["blue", "green", "orange", "red"]
)
plt.title("Average Aβ42 by APOE Genotype")
plt.xlabel("APOE Genotype")
plt.ylabel("Average Aβ42 (pg/ug)")
plt.text(
    1.5,
    max(mean_ab) + max(stdev_ab) * 0.2,
    f"One-way ANOVA: p = {p_value_ab:.3f}",
    ha="right",
    fontsize=9
)
plt.show()

# ---------------------------------------------------------
# Mean pTau Bar graph
# ---------------------------------------------------------

#One-way ANOVA
f_stat_ptau, p_value_ptau = stats.f_oneway(
    ptau_2,
    ptau_3_3,
    ptau_3_4,
    ptau_4_4
)
print("pTau f-statistic:", f_stat_ptau)
print("pTau p_value:", p_value_ptau)

# tTau bar graph
mean_ptau = [mean_ptau_2, mean_ptau_3_3, mean_ptau_3_4, mean_ptau_4_4]
stdev_ptau = [stdev_ptau_2, stdev_ptau_3_3, stdev_ptau_3_4, stdev_ptau_4_4]
plt.bar(
    genotypes,
    mean_ptau,
    yerr=stdev_ptau,
    capsize=10,
    color=["blue", "green", "orange", "red"]
)
plt.title("Average tTau by APOE Genotype")
plt.xlabel("APOE Genotype")
plt.ylabel("Average pTau (pg/ug)")
plt.text(
    1.5,
    max(mean_ptau) + max(stdev_ptau) * 0.5,
    f"One-way ANOVA: p = {p_value_ptau:.3f}",
    ha="right",
    fontsize=9
)
plt.show()

#Used ChatGPT above to help with generating code for four-way bar graphs; gave it my variable names and what I wanted on each axis. 


# ---------------------------------------------------------
# Scatter plot for AB-42 and pTau
# ---------------------------------------------------------

# Scatter plot for AB-42 and pTau to see if they are correlated 
patient_ab_42 = []
patient_ptau = []

for patient in Patient.all_patients:

    if (patient.abeta42 != ""
        and patient.abeta42 != "Unavailable"
        and patient.ptau != ""
        and patient.ptau != "Unavailable"):

        patient_ab_42.append(float(patient.abeta42))
        patient_ptau.append(float(patient.ptau))

X = patient_ab_42
Y = patient_ptau

model = LinearRegression()
model.fit(np.array(X).reshape(-1, 1), Y)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(np.array(X).reshape(-1, 1), Y)

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
plt.plot(X, model.predict(np.array(X).reshape(-1, 1)), color="red")
plt.xlabel('Amyloid-Beta42 (pg/ug)')
plt.ylabel('Phosphorylated Tau (pTau) (pg/ug)')
plt.title('Scatter Plot of pTau vs AB42 Levels')
plt.show()