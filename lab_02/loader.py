import pandas as pd
import psycopg2
import os

df = pd.read_csv("/data/patients.csv")

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
id SERIAL PRIMARY KEY,
first_name TEXT,
last_name TEXT
)
""")

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO patients(first_name,last_name) VALUES(%s,%s)",
        (row[0], row[1])
    )

conn.commit()
conn.close()

print("Data loaded successfully")