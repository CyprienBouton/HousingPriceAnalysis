from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split
import pickle
import numpy as np

if __name__=="__main__":
    file = open("dset/data.pkl","rb")
    data = pickle.load(file)

    def MAPE(true, pred):
        return (100*np.abs(true-pred)/true).mean()

    x_train, x_test, y_train, y_test = train_test_split(data[[
    "Built surface", "Number of rooms", "Longitude", "Latitude", "District", "Delta days"]], 
    data["Transaction cost"].values, test_size=.2, random_state=1) # split train_set and test_set

    model = RandomForestRegressor(n_estimators=200, min_samples_split=30)
    model.fit(x_train, y_train)
    pickle.dump(model, open('src/model.pkl', 'wb'))