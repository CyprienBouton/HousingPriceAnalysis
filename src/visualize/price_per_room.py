import matplotlib.pyplot as plt
import pickle
import numpy as np

file = open("dset/data.pkl","rb")
data =pickle.load(file)

def price_per_room():
    fig, ax = plt.subplots(figsize=(3.,2.3))
    avg_price = data.groupby('Number of rooms')['Cost per m2'].agg(np.mean)
    district_ordered = list(set(data['Number of rooms']))
    ax.bar(district_ordered,avg_price)
    return fig