import pandas as pd
import streamlit as st
import numpy as np

##importing ORIGINAL dataset
original = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/competition/data/output_noshow1_balanced_2022-11-16.csv')
original

#Viewing data 

original.columns
original.shape
original.dtypes 


print("Given Dataframe :\n", original) 

age = original(original['patient_gender'], 'female')
print('\nResult dataframe :\n', age)



###importing 

external = pd.read_csv("data/external_data.csv")
external 

##Viewing data
external.columns
external.shape
external.dtypes 

##important factors to note: alcholism, diabtetes, hypertension, age, gender

##cleaning external columns

external.columns = external.columns.str.replace('[^A-Za-z0-9]+', '_')
external.columns = external.columns.str.lower()

##renaming external columns 
renamed_external = external.rename(columns={'alcoolism': 'alcoholism', 'hipertension': 'hypertension'})

#exporting cleaned csv
renamed_external.to_csv("data/cleaned_external.csv")