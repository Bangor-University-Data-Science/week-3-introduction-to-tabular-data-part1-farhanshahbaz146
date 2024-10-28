import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df

#testing function's executions
if __name__ == "__main__":
    filepath = "data/titanic.csv"  
    titanic_data = load_titanic_data(filepath)
    print(titanic_data.head())  # Display the first few rows to confirm loading
