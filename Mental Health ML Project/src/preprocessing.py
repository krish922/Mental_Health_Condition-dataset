import pandas as pd

def prepare_feature(df):
    # Drop unnecessory columns
    X = df.drop(["User_ID", "Mental_Health_Condition"],axis=1)

    # Convert categorical columns
    X = pd.get_dummies(X)

    # Fill missing Values
    X = X.fillna(0)

    return X

def encode_target(df):
    mapping = {
        "NO": 0,
        "Yes": 1
        }

    y = df["Mental_Health_Condition"].map(mapping)
    return y