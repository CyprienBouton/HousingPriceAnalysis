from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split
from sklearn.metrics import  mean_squared_error
import pickle

file = open("../dset/data.pkl","rb")
data = pickle.load(file)

x_train, x_test, y_train, y_test = train_test_split(
    data.drop(['Transaction cost','Transaction date', 'Transaction type'], axis=1),
 data['Transaction cost'], test_size=.2)

model = RandomForestRegressor()
model.fit(x_train, y_train)
preds = model.train(x_test)

print( mean_squared_error(preds, y_test))