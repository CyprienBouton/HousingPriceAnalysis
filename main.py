import pandas as pd
import re

data = pd.read_csv('dset/valeursfoncieres-2022-s1.txt', on_bad_lines='skip')

def split_values(x):
    return re.split("\|",str(x.values[0]))

data = data.apply(split_values,axis=1)

if __name__ == "__main__":
    print(data.iloc[0])

