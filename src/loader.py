import pandas as pd

def load_data():
    # Загрузка patients.csv из датасета Synthetic Medical Dataset (локально)
    data = pd.read_csv('../data/patients.csv')  # Путь относительно src/
    print("Patients data loaded successfully. Columns include FIRST and LAST for names.")
    return data

if __name__ == "__main__":
    load_data()
