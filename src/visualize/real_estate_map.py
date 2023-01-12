import pickle
import matplotlib.pyplot as plt

file = open("dset/data.pkl","rb")
data =pickle.load(file)

def real_estate_map(nb_points=50000):
    """
    Figure showing a the cost per m2 in a maps of Paris.
    """
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