import streamlit as st
from . import page2, page3, page4

def main_page():
    st.markdown("<h1>Flat price prediction in Paris</h1>", unsafe_allow_html=True)
    st.markdown("""
    The purpose of this project is to predict the price of flats in Paris and to visualize
    the housing market in Paris.<br/><br/>
    There are 3 sections in this app:
    - Dataset
    - Data visualization
    - Flat price prediction
    """, unsafe_allow_html=True)
