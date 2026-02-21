import pandas as pd
import re

def depersonalize_data(df):
    df['FULL_NAME'] = df['FIRST'] + ' ' + df['LAST']
    pattern = r'\b[A-Za-z]+(?:\s[A-Za-z]+){0,2}\b'
    df['DEPERSON_FULL_NAME'] = df['FULL_NAME'].apply(
        lambda x: re.sub(pattern, '[REDACTED]', x)
    )
    print(df[['FULL_NAME', 'DEPERSON_FULL_NAME']].head())
    return df

if __name__ == "__main__":
    data = pd.read_csv('data/patients.csv')
    depersonalize_data(data)
