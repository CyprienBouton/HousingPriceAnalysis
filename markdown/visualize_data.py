import pickle
import matplotlib.pyplot as plt

file = open("dset/data.pkl","rb")
data =pickle.load(file)

def cost_per_m2(nb_points=50000):
    assert type(nb_points)==int
    df = data[:nb_points]
    fig, ax = plt.subplots(figsize=(3.,2.3))
    points = ax.scatter(df['Longitude'], df['Latitude'], c=df['Cost per m2'], s=5, cmap="plasma")
    ax.title.set_text("Cost per square meter according to location")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    fig.colorbar(points)
    return fig

def price_Built_surface():
    fig, ax = plt.subplots(figsize=(3.,2.3))
    
