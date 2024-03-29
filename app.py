import streamlit as st
from streamlit_pages import main_page, page2, page3, page4, page5

if __name__=="__main__":
    page_names_to_funcs = {
    "General Description": main_page.main_page,
    "Dataset": page2.page2,
    "Data visualization": page3.page3,
    "Flat Price prediction": page4.page4,
    "Create your own model": page5.page5
    }

    selected_page = st.sidebar.selectbox("Go to page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()