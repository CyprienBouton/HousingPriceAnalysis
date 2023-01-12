from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
import datetime

class Flat:
    """
    this class contain the following attributes:
        Built in Surface
        Number of rooms
        Address
        District
        Date of the transaction 
    """
    def __init__(self, surface, nb_rooms: int, address: str, district: int, date):
        self.surface = surface
        self.nb_rooms = nb_rooms
        self.address = address
        self.district = district
        self.date = date
        self.postcode = str(75000+self.district)
        oneday = pd.Timedelta(days=1)
        # substract the 1st transaction of the dset. See extract_transform/add_delta.py for more details
        self.relative_date = (self.date - datetime.date(2017, 1, 7))/oneday

    def geocode_location(self):
        """
        Create a geolocator object from the adress and the postcode.
        This allow to get the latitude and the longitude
        """
        geolocator = Nominatim(user_agent="my_request")
        location = geolocator.geocode(f"{self.address}, Paris {self.postcode}")
        return location

    def lat(self):
        return self.geocode_location().latitude
    
    def long(self):
        return self.geocode_location().longitude
    
    def predict_price(self, model):
        #give a price estimation for a given model
        input = pd.DataFrame([[
            self.surface, self.nb_rooms, self.district, self.lat(), self.long(), self.relative_date]],
        columns = ['Built surface', 'Number of rooms', 'Longitude', 'Latitude', 'District', 'Delta days'])
        input=input.astype(float)
        preds = model.predict(input)[0]
        return '{:,}'.format(round(preds))