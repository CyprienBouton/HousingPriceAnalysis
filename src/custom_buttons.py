import streamlit as st
import json

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


def dictionary_input(dict_name):
    """ Display a dictionary input widget
    :param dict_name: Name of the dictionary.
    :type dict_name: str
    """
    raw_data = st.text_input(dict_name, value="{}")
    raw_data = raw_data.replace('\'', '"') # json requires double quotes
    try:
        return json.loads(raw_data)
    except:
        st.error(f"⚠️ {dict_name} must be a dictionary")


def get_model_params(class_model):
    """ Display a widget that retreive the parameters of the model
    :param class_model: Class of the ml model chosen.
    :type class_model: ml model
    """
    model_all_params = set(class_model._get_param_names())
    model_params = dictionary_input("Parameters of your model")
    # If parameters are provided
    if model_params:
        # Keys that are not among the parameters of the model
        absent_params = set(model_params.keys()) - model_all_params
        if absent_params:
            absent_params_str = ', '.join([str(e) for e in iter(absent_params)])
            if len(absent_params)>1:
                st.error(f"⚠️ {absent_params_str} are invalid parameters for this model.")
            else:
                st.error(f"⚠️ {absent_params_str} is an invalid parameter for this model.")
    return model_params