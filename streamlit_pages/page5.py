import streamlit as st
import pickle
import numpy as np
from sklearn.model_selection import cross_val_score
from src.choose_model import choose_model

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
    if st.button('Compute cross validation score'):
        with st.spinner("Wait, your model is training"):
            scores = cross_val_score(model, X, y, cv=5)
        st.markdown("The average coefficient of determination is R<sup>2</sup>="
                    + str(round(scores.mean(), 3)),
                    unsafe_allow_html=True)