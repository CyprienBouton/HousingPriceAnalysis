import streamlit as st
import pickle

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

from src.custom_buttons import get_model_params


def choose_model():
    """"
    Function allowing to choose a sklearn ml model and its attribute.
    """
    model_names = {
        "Linear": LinearRegression,
        "Ridge": Ridge,
        "Lasso": Lasso,
        "DecisionTreeRegressor": DecisionTreeRegressor,
        "Random Forest": RandomForestRegressor,
        "ExtraTreesRegressor":ExtraTreesRegressor, 
        "KNN": KNeighborsRegressor
    }
    model_name = st.selectbox("Model", model_names.keys())
    class_model = model_names[model_name]
    model_params = get_model_params(class_model)
    return class_model, model_params