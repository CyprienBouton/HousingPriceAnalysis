import streamlit as st
import pickle
import numpy as np
from sklearn.model_selection import cross_val_score

from src.choose_model import choose_model
from src.custom_buttons import button_dropdown_list
from src.model import cross_validate

def MAPE(true, pred):
    # return the mean average pourcentage error
    return (100*np.abs(true-pred)/true).mean()
    
def page5():
    #Page allowing to create a model.
    st.markdown("<h1>Create your own model</h1>", unsafe_allow_html=True)
    model = choose_model()
    X = pickle.load(open('dset/X.pkl','rb'))
    y = pickle.load(open('dset/y.pkl','rb'))
    if st.button("Fit"):
        with st.spinner("Wait, your model is training"):
            model.fit(X, y)
        st.download_button("Download model", data=pickle.dumps(model), file_name="model.pkl")
    button_dropdown_list("Cross validation")
    if st.session_state["Cross validation"]:
        n_splits = st.number_input("Number of splits", min_value=2)
        if st.button('Compute cross validation score'):
            scores = cross_validate(model, n_splits=5)
            st.markdown("The average coefficient of determination is R<sup>2</sup>="
                        + str(round(scores, 3)),
                        unsafe_allow_html=True)