from matplotlib.ticker import StrMethodFormatter
import matplotlib.pyplot as plt
import pickle
import numpy as np

file = open("dset/data.pkl","rb")
data =pickle.load(file)

def price_per_room():
    fig, ax = plt.subplots(figsize=(3.,2.3))
    avg_price = data.groupby('Number of rooms')['Cost per m2'].agg(np.mean)
    district_ordered = list(set(data['Number of rooms']))
    ax.set_xlabel("Number of rooms")
    ax.set_ylabel("Cost per m2 (€)")
    ax.bar(district_ordered,avg_price)
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    return fig