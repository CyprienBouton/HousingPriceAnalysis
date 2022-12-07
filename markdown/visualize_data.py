import pickle
import matplotlib.pyplot as plt
import numpy as np

file = open("dset/data.pkl","rb")
data =pickle.load(file)

def cost_per_m2(nb_points=50000):
    assert type(nb_points)==int
    df = data[:nb_points]
    fig, ax = plt.subplots(figsize=(3.,2.3))
    points = ax.scatter(df['Longitude'], df['Latitude'], c=df['Cost per m2'], s=5, cmap="plasma")
    ax.title.set_text("Paris real estate maps")
    plt.box(None)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    fig.colorbar(points, label="Cost/m2")
    return fig

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
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    if round(p(0))>0:
        formula = f"{y_name} = {round(p(1)-p(0))} * {x_name} + {round(p(0))}"
    else:
        formula = f"{y_name} = {round(p(1)-p(0))} * {x_name} - {round(-p(0))}"
    return p(x), formula
    