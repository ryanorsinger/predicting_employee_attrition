import pandas as pd
from sklearn.model_selection import train_test_split


def train_validate_test_split(df, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, random_state=seed)
    train, validate = train_test_split(train_validate, test_size=0.3, random_state=seed)
    return train, validate, test



def encode_categoricals(df):
    # Convert boolean strings to 0/1 boolean
    df.OverTime = df.OverTime == "Yes"
    df["is_female"] = df.Gender == "Female"
    df.Attrition = df.Attrition == "Yes"
    
    # columns to encode


    # returns the df and the encoded_df



def drop_unnecessary_columns(df):
    zero_entropy_columns = []
    for column in df.columns:
        if len(df[column].value_counts()) == 1:
            zero_entropy_columns.append(column)
    zero_entropy_columns

    df = df.drop(columns=["Gender"] + zero_entropy_columns)
    return df





# Encode_categoricals
# Drop unnecessary columns
# Split into train, validate, and test
# Produce scaled dataframes for X and ys
# def prep_and_preprocess(df):



# train, validate, test, scaled_encoded_train, scaled_encoded_validate, scaled_encoded_test