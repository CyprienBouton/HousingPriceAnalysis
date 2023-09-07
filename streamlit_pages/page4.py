import streamlit as st
from src.flat import Flat
import pickle

def price_estimation(flat, file):
    #compute the price if the model is loaded otherwise return a warning
    if file!=None: # first load the model
        models_dict = pickle.load(file)
        preds = flat.predict_price(models_dict)
        return st.write("We estimate that your flat worth "+str(preds)+" €")
    else:
        return st.warning('You have to upload a model to estimate the price!', icon="⚠️")    

def page4():
    st.markdown("<h1>Flat price prediction</h1>",
     unsafe_allow_html=True)
    surface = st.slider("Surface", min_value=9, max_value=300, value=50, step=None)
    nb_rooms = st.number_input("Number of rooms", min_value=1, max_value=50)
    address = st.text_input("Address")
    district = st.selectbox("District:",[i for i in range(1,21)])
    date = st.date_input("Date of the transaction")
    yourFlat = Flat(surface, nb_rooms, address, district, date)
    file = st.file_uploader("Import your model (.pkl format)",type='pkl')
    prediction = st.button("Price estimation")
    if prediction:
        price_estimation(yourFlat, file)
