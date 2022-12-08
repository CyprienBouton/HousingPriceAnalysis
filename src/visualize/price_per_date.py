from matplotlib.ticker import StrMethodFormatter
import matplotlib.pyplot as plt
import pickle
import datetime
import numpy as np

file = open("dset/data.pkl","rb")
data =pickle.load(file)

def price_per_date():
    fig, ax = plt.subplots(figsize=(3.,2.3))
    data['Month'] = data['Transaction date'].apply(lambda x: datetime.date(x.year, x.month, 1))
    avg_price = data.groupby('Month')['Cost per m2'].agg(np.mean)
    # district_ordered = list(set(data['Delta days']))
    ax.plot(avg_price)
    ax.set_xlabel("Date (year)")
    ax.set_ylabel("Cost per m2 (€)")
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    return fig