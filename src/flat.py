from geopy.geocoders import Nominatim

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
