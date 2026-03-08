import streamlit as st
import psycopg2
import pandas as pd
import os

conn = psycopg2.connect(
    host="db",
    user="admin",
    password="admin",
    database="medical"
)

df = pd.read_sql("SELECT * FROM patients", conn)

st.title("Medical Records Dashboard")

st.write(df.head())