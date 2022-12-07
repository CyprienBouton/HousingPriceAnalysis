import streamlit as st
from visualize import cost_per_m2, price_per_surface
def page3():
    st.markdown("<h1>Data visualization</h1>",
     unsafe_allow_html=True)
    st.markdown("See how the following paramters effect on the price:")
    st.pyplot(price_per_surface.price_per_surface())
    st.pyplot(cost_per_m2.cost_per_m2())