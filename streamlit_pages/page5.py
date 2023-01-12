import streamlit as st
import pickle
import numpy as np
from src.choose_model import choose_model

def MAPE(true, pred):
    # return the mean average pourcentage error
    return (100*np.abs(true-pred)/true).mean()
    
def page5():
    #Page allowing to create a model.
    st.markdown("<h1>Create your own model</h1>", unsafe_allow_html=True)
    model = choose_model()
    x_train = pickle.load(open('dset/x_train.pkl','rb'))
    y_train = pickle.load(open('dset/y_train.pkl','rb'))
    x_test = pickle.load(open('dset/x_test.pkl','rb'))
    y_test = pickle.load(open('dset/y_test.pkl','rb'))
    if st.button("Fit"):
        with st.spinner("Wait, your model is training"):
            model.fit(x_train, y_train)
        error = MAPE(y_test, model.predict(x_test))
        st.write("""Your model has a mean error of {:.2f} %""".format(error))
        st.download_button("Download model", data=pickle.dumps(model), file_name="model.pkl")