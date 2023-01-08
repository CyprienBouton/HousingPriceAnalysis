import streamlit as st
from markdown import main_page, page2, page3, page4

page_names_to_funcs = {
    "General Description": main_page.main_page,
    "Dataset": page2.page2,
    "Data vizualisation": page3.page3,
    "Flat Price prediction": page4.page4
}

selected_page = st.sidebar.selectbox("Go to page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]() 