import streamlit as st
import pickle
def page2():
    st.markdown("<h1>Dataset</h1>",
     unsafe_allow_html=True)
    st.markdown("""
    All the transactions on the housing market in France are available 
    here https://files.data.gouv.fr/geo-dvf/latest/csv/
    
    For more information on the dataset consult the following link 
    https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/#description

    This project use all the housing transactions from 2017 to 2022. This dataset 
    includes the localization of the accomodation and information about the transaction.

    This project use only the most relevent features of the government dataset:
    - Transaction cost
    - Transaction date
    - Built surface
    - Number of rooms
    - Longitude
    - Latitude

    And other additional features:
    - District 
    - Delta days The number of days since the first transaction of the dataset
    
    
    We obtain the following dataset:
    """)
    data = pickle.load(open("dset/data.pkl","rb"))
    st.write(data)