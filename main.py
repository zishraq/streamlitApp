import streamlit as st
import pandas as pd

st.title('Patient data')

df = pd.read_csv('patients_detailed_data.csv')

st.dataframe(df)
