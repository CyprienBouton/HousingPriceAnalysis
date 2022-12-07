import pickle
import matplotlib.pyplot as plt
import numpy as np

file = open("dset/data.pkl","rb")
data =pickle.load(file)

def price_per_surface(nb_points=50000):
    df = data[:nb_points]
    fig, ax = plt.subplots(figsize=(3.,2.3))
    ax.scatter(df['Built surface'], df['Transaction cost']*1e-6)
    ax.title.set_text("Paris real estate maps")
    ax.set_xlabel("Surface (m2)")
    ax.set_ylabel("Price (M€)")
    z, formula = trend_line(df['Built surface'], df['Transaction cost'], "Surface", "Price")
    plt.plot(df['Built surface'], z*1e-6,'--r')
    plt.title(formula)
    return fig

def trend_line(x,y,x_name: str, y_name: str):
    """
    function to compute the linear trend line of a scatter. Return:
        1. The trend line
        2. A string re^resenting the trend line's equation
    """
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    a = round(p(1)-p(0))
    b = round(-p(0))
    if round(p(0))>0:
        formula = f"{y_name} = {'{:,}'.format(a)} * {x_name} + {'{:,}'.format(b)}"
    else:
        formula = f"{y_name} = {'{:,}'.format(a)} * {x_name} - {'{:,}'.format(b)}"
    return p(x), formula
    