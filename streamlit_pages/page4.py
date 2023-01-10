import streamlit as st
from src.flat import Flat
import pickle

def price_estimation(flat, file):
    if file!=None: # first load the model
        model = pickle.load(file)
        preds = flat.predict_price(model)
        return st.write("We estimate that your flat worth "+str(preds)+" €")
    else:
        return st.warning('You have to upload the model to estimate the price!', icon="⚠️")    

def page4():
    st.markdown("<h1>Flat price prediction</h1>",
     unsafe_allow_html=True)
    surface = st.slider("Surface", min_value=9, max_value=300, value=50, step=None)
    nb_rooms = st.number_input("Number of rooms", min_value=1, max_value=50)
    adress = st.text_input("Address")
    district = st.selectbox("District:",[i for i in range(1,21)])
    date = st.date_input("Date of the transaction")
    yourFlat = Flat(surface, nb_rooms, adress, district, date)
    file = st.file_uploader("Import your model",type='pkl')
    st.button("Price estimation",on_click=price_estimation(yourFlat,file))