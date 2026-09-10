import pandas as pd 

df = pd.read_csv('/Users/ellepickard/Documents/Computational BME/Module 1/Module1_CompBME/Metadata and Protein Data for Module 1.csv')

for header in df.columns: 
        print(header)
       