import pickle
import streamlit as st

file = open("dset/data.pkl","rb")
data =pickle.load(file)
data['latitude']=data['latitude'].astype(int)
data['longitude']=data['longitude'].astype(int) 
# fig =  px.choropleth(data, lat="Latitude", lon="Longitude")
st.map(data, zoom=None)