import streamlit as st
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.gaussian_process import GaussianProcessRegressor

def choose_model():
    model_names = {
        "Linear": LinearRegression(),
        "Ridge": Ridge(),
        "Lasso": Lasso(),
        "DecisionTreeRegressor": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "KNN": KNeighborsRegressor(),
        "Gaussian": GaussianProcessRegressor()
    }
    model_name = st.selectbox("Model", model_names.keys())
    model = model_names[model_name]
    return model