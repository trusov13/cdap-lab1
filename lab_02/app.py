import streamlit as st
import psycopg2
import pandas as pd
import os

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB", "medical_db"),
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST", "db"),          # ← обязательно!
    port=int(os.getenv("POSTGRES_PORT", "5432"))
)

df = pd.read_sql("SELECT * FROM patients", conn)

st.title("Medical Records Dashboard")

st.write(df.head())