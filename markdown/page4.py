import streamlit as st
from src.flat import Flat
import pickle

model = pickle.load(open('src/model.pkl','rb'))

def page4():
    st.markdown("<h1>Flat price prediction</h1>",
     unsafe_allow_html=True)
    surface = st.slider("Surface", min_value=9, max_value=300, value=50, step=None)
    nb_rooms = st.number_input("Number of rooms", min_value=1, max_value=50)
    adress = st.text_input("adress")
    district = st.selectbox("District:",[i for i in range(1,21)])
    yourFlat = Flat(surface, nb_rooms, adress, district)
    st.markdown("We estimate that your flat worth "+str(yourFlat.predict_price(model))+" €")
    
