import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/competition/data/output_noshow1_balanced_2022-11-16.csv')
df

#Viewing data 

df.columns
df.shape
df.dtypes 


print("Given Dataframe :\n", df) 

age = df(df['patient_gender'], 'female')
print('\nResult dataframe :\n', age)
