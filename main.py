import pandas as pd
import re

data = pd.read_csv('dset/valeursfoncieres-2022-s1.csv', on_bad_lines='skip')

def split_values(x):
    return re.split("\|",str(x))

columns = split_values(data.columns[0])

def transform_row(df):
    df.iloc[:,0] = df.iloc[:,0].apply(split_values)
    return df

data = transform_row(data)
for idx,column in enumerate(columns):
    data[column] = data.apply(lambda x:x)#[idx])

if __name__ == "__main__":
    print(data)

