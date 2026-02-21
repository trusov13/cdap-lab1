import pandas as pd

def load_patients():
    return pd.read_csv('../data/patients.csv')

def load_encounters():
    return pd.read_csv('../data/encounters.csv')

if __name__ == "__main__":
    print(load_patients().head())
    print(load_encounters().head())
