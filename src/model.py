from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import pickle
import numpy as np

file = open("dset/data.pkl","rb")
data = pickle.load(file)

def MAPE(true, pred):
    return (100*np.abs(true-pred)/true).mean()

x_train, x_test, y_train, y_test = train_test_split(data[[
    "Built surface","Number of rooms", "Longitude","Latitude", "District", "Delta days"]], 
data.iloc[:,0].values.ravel(), test_size=.2, random_state=1) # split train_set and test_set

model = RandomForestRegressor(n_estimators=100, min_samples_split=4)
model.fit(x_train, y_train)
pickle.dump(model, open('src/model.pkl', 'wb'))
# preds = model.predict(x_test)
# print(MAPE(y_test, preds), mean_squared_error(y_test, preds), r2_score(y_test, preds))