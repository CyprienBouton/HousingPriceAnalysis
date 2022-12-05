import pickle
import streamlit as st
import matplotlib.pyplot as plt

file = open("dset/data.pkl","rb")
data =pickle.load(file)

fig, ax = plt.subplots()
points = ax.scatter(data['Longitude'], data['Latitude'], c=data['Cost per m2'], s=5, cmap="plasma")
fig.colorbar(points)
st.pyplot(fig)