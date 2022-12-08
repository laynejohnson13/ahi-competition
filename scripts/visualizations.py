import pandas as pd 
import numpy as np 
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

##creating title/header
st.title('Predictors of Patient No-Shows')
st.header('Welcome! This dashboard was created to display visualizations regarding patient no-show data.')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/competition/data/output_noshow1_balanced_2022-11-16.csv')
df


###visualizations 

st.subheader('Comparing Appointment Type and Show Status')
type = px.bar(df, x= 'appointment_type', y=['appointment_yosi_noshow1'], color= 'appointment_type', barmode='group', height=400)
st.plotly_chart(type)

st.subheader('Comparing Patient Age and Show Status')
age = px.bar(df, x= 'patient_age', y=['appointment_yosi_noshow1'], color= 'appointment_yosi_noshow1', barmode='group', height=400)
st.plotly_chart(age)

st.subheader('Comparing Show Status and Location')
location = px.bar(df, x='appointment_yosi_noshow1', y=['geocode_city','geocode_county'], barmode='group', height=400)
st.plotly_chart(location) 

st.subheader("Overall Show Status")
show = df[['appointment_yosi_noshow1']]
st.line_chart(show)