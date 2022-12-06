import streamlit as st
from .visualize_data import cost_per_m2
def page3():
    st.markdown("<h1>Data visualization</h1>",
     unsafe_allow_html=True)
    st.pyplot(cost_per_m2())
    