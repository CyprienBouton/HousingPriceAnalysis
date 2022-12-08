import streamlit as st
from src.visualize import (real_estate_map, price_per_surface,
 price_per_room, price_by_district, price_per_date)
def page3():
    st.markdown("<h1>Data visualization</h1>",
     unsafe_allow_html=True)
    st.markdown("Visualize how each parameter impacts the transaction value:")
    parameter_to_visualized = {
        "Surface": price_per_surface.price_per_surface,
        "Number of rooms": price_per_room.price_per_room,
        "Location": real_estate_map.real_estate_map,
        "District": price_by_district.price_by_district,
        "Date": price_per_date.price_per_date
    }

    selected_visualization = st.selectbox("Choose a parameter:", parameter_to_visualized.keys())
    st.pyplot(parameter_to_visualized[selected_visualization]())