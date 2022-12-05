import pickle
import streamlit as st
import matplotlib.pyplot as plt

file = open("dset/data.pkl","rb")
data =pickle.load(file)
data['cost per m2']=data['Transaction cost']/data['Built surface']

print(data['cost per m2'].min())
# fig = plt.figure()
# fig =plt.plot(data['longitude'], data['latitude'])
# plt.show()
#  st.plotly_chart(fig)
data['cost per m2'].hist(bins = 10)
plt.show()
data = data[(data['cost per m2']<14000) & (data['cost per m2']>6000)]
data['cost per m2'].hist(bins = 10)
plt.show()