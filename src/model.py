from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split
from sklearn.metrics import  mean_squared_error
import pickle
import matplotlib.pyplot as plt
import numpy as np


def MAPE(true, pred):
    return (100*np.abs(true-pred)/true).mean()

file = open("dset/data.pkl","rb")
data = pickle.load(file)

x_train, x_test, y_train, y_test = train_test_split(data.iloc[:,1:], 
data.iloc[:,:1].values.ravel(), test_size=.2) # split train_set and test_set


model = RandomForestRegressor(n_estimators=5)
model.fit(x_train, y_train)
for i in range(50):
    preds = model.predict([x_test.iloc[i]])
    print(MAPE([y_test[i]],preds), y_test[i], preds)