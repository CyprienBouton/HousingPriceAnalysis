import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.gaussian_process import GaussianProcessRegressor

def MAPE(true, pred):
    return (100*np.abs(true-pred)/true).mean()
    
def page5():
    st.markdown("<h1>Create your own model</h1>", unsafe_allow_html=True)
    model_names = {
        "Linear": LinearRegression,
        "Ridge": Ridge,
        "Lasso": Lasso,
        "DecisionTreeRegressor": DecisionTreeRegressor,
        "Random Forest": RandomForestRegressor,
        "KNN": KNeighborsRegressor,
        "SVM": SVR,
        "Gaussian": GaussianProcessRegressor
    }
    model_name = st.selectbox("Model", model_names.keys())
    model = model_names[model_name]
    x_train = pickle.load(open('src/x_train.pkl','rb'))
    y_train = pickle.load(open('src/y_train.pkl','rb'))
    x_test = pickle.load(open('src/x_test.pkl','rb'))
    y_test = pickle.load(open('src/y_test.pkl','rb'))
    model.fit(x_train, y_train)
    error = MAPE(y_test, model.predicts(x_test))
    st.write(f"Your model has an error of {error}%")