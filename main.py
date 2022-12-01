import pandas as pd
import re
import streamlit as st
from extract_transform.load_data import load_data
import pickle

data = pd.DataFrame()
for year in range(2017,2023):
    data_year = load_data(year)
    data = pd.concat([data,data_year])
    print(data.shape, data_year.shape)

# we save the data in a pickle file
file = open('data.pkl', 'wb')
pickle.dump(data, file)
