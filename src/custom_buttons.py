import streamlit as st

def button_dropdown_list(button_name):
    """ Button that modify st.session_state[button_name] state when it's clicked
    
    :param button_name: Name of the button.
    :type button_name: str
    """
    if button_name not in st.session_state:
        st.session_state[button_name] = False
    def change_show():
        st.session_state[button_name] = not st.session_state[button_name]
    st.button(button_name, on_click=change_show)