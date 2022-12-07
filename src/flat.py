from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np

class Flat:
    def __init__(self, surface, nb_rooms: int, adress: str, district: int):
        self.surface = surface
        self.nb_rooms = nb_rooms
        self.adress = adress
        self.district = district
        self.postcode = str(75000+self.district)

    def geocode_location(self):
        #making an instance of Nominatim class
        geolocator = Nominatim(user_agent="my_request")
        location = geolocator.geocode(f"{self.adress}, Paris {self.postcode}")
        return location

    def lat(self):
        return self.geocode_location().latitude
    
    def long(self):
        return self.geocode_location().longitude
    
    def predict_price(self, model):
        #give a price estimation for a given model
        input = pd.DataFrame([[self.surface, self.nb_rooms, self.district, self.lat(), self.long()]],
        columns = ['Built surface', 'Number of rooms', 'Longitude', 'Latitude', 'District'])
        input=input.astype(float)
        preds = model.predict(input)[0]
        return '{:,}'.format(round(preds))

if __name__=="__main__":
    myHome = Flat(16, 1, "270 rue saint Jacques", 5)
    import pickle
    model = pickle.load(open("src/model.pkl","rb"))
    print(myHome.predict_price(model))