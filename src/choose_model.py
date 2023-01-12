import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.gaussian_process import GaussianProcessRegressor

def custom():
    # Upload a custom model and then train it.
    file = st.file_uploader("Import a model you'd like to train (.pkl format)",type='pkl')
    return file

def choose_model():
    """"
    Function allowing to build a model and then to train it.
    """
    model_names = {
        "Linear": LinearRegression,
        "Ridge": Ridge,
        "Lasso": Lasso,
        "DecisionTreeRegressor": DecisionTreeRegressor,
        "Random Forest": RandomForestRegressor,
        "KNN": KNeighborsRegressor,
        "Gaussian": GaussianProcessRegressor,
        "Custom": custom
    }
    model_name = st.selectbox("Model", model_names.keys())
    model = model_names[model_name]()
    return model