import pickle
import pandas as pd
import streamlit as st
from src.extract_transform import (load_data, clean_data, remove_outlier,
 keep_flat, add_delta_days, keep_paris)

if __name__=="__main__":
    data = pd.DataFrame()
    for year in range(2017,2023):
        data_year = load_data.load_data(year)
        data = pd.concat([data,data_year])
    data = clean_data.clean_data(data)
    data = keep_paris.keep_paris(data) # create a column District
    data = keep_flat.keep_flat(data)
    Bounds = {
        "Built surface min": 9,
        "Built surface max": 1000,
        "Transaction cost min": 1000,
        "Transaction cost max": 10000000,
        "Cost per m2 min": 2500,
        "Cost per m2 max": 30000} #Bounds for flat in paris
    Nsigma = 1.5 # any data superior to 1.5 times its standard deviation will be removed
    data = remove_outlier.remove_outlier(data, Nsigma, Bounds) # create a column cost per m2
    data = add_delta_days.add_delta_days(data)
    data = data.dropna()
    # we save the data in a pickle file
    file = open('dset/data.pkl', 'wb')
    pickle.dump(data, file)

