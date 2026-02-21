import pandas as pd

def load_data():
    data = pd.read_csv('../data/encounters.csv')
    print("Encounters data loaded successfully.")
    return data

if __name__ == "__main__":
    load_data()
