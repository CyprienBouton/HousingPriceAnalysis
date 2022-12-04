import pickle
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

file = open("dset/data.pkl","rb")
data =pickle.load(file)

data['latitude']=data['latitude'].astype(int)
data['longitude']=data['longitude'].astype(int) 
fig =  px.scatter_geo(data, lat="latitude", lon="longitude",
 scope='europe',center={'lat':48.9,'lon':2.3})
# fig.show()
st.plotly_chart(fig)
# st.map(data)