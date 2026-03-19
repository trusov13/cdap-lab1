import pandas as pd
import psycopg2
import os

df = pd.read_csv("/data/patients.csv")

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB", "medical_db"),
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST", "db"),          # ← обязательно!
    port=int(os.getenv("POSTGRES_PORT", "5432"))
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