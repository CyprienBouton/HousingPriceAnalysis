import streamlit as st
import pickle
import numpy as np
from src.choose_model import choose_model

def MAPE(true, pred):
    return (100*np.abs(true-pred)/true).mean()
    
def page5():
    st.markdown("<h1>Create your own model</h1>", unsafe_allow_html=True)
    model = choose_model()
    x_train = pickle.load(open('dset/x_train.pkl','rb'))
    y_train = pickle.load(open('dset/y_train.pkl','rb'))
    x_test = pickle.load(open('dset/x_test.pkl','rb'))
    y_test = pickle.load(open('dset/y_test.pkl','rb'))
    model.fit(x_train, y_train)
    error = MAPE(y_test, model.predict(x_test))
    st.write("""Your model has an error of {:.2f} %""".format(error))
    st.download_button("Download Model", data=pickle.dumps(model), file_name="model.pkl")