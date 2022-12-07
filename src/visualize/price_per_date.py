import matplotlib.pyplot as plt
import pickle
import numpy as np

file = open("dset/data.pkl","rb")
data =pickle.load(file)

def price_per_date():
    fig, ax = plt.subplots(figsize=(3.,2.3))
    avg_price = data.groupby('Delta days')['Cost per m2'].agg(np.mean)
    district_ordered = list(set(data['Delta days']))
    ax.plot(district_ordered,avg_price)
    return fig