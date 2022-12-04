from geopandas import GeoDataFrame
from shapely.geometry import Point
import pickle
import geoplot

file = open("dset/data.pkl","rb")
data =pickle.load(file)
geometry = [Point(xy) for xy in zip(data.Longitude, data.Latitude)]
data = data.drop(['Longitude', 'Latitude'], axis=1)
gdf = GeoDataFrame(data, crs="EPSG:4326", geometry=geometry)
geoplot.choropleth(gdf)