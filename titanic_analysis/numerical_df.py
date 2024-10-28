import pandas as pd

def get_numerical_df(df, numerical_features):
    #filtering the dataframe
    numerical_df = df[numerical_features].copy()
    return numerical_df

#test function's executions and outputs
if __name__ == "__main__":
    filepath = "data/titanic.csv" 
    titanic_data = pd.read_csv(filepath)
    numerical_features = ['Age', 'Fare']
    numerical_df = get_numerical_df(titanic_data, numerical_features)
    print(numerical_df)
