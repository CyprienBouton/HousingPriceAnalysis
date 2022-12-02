def clean_data(data):
    """
    Clean the pandas dataframe as follow:
        2.1. Replace by type 'Vente' (sell) all the naming involving vente (sell) activity.
        2.2. Remove all transactions not 'Vente' (sell)  (eg 'echange', 'expropriation',...)
        2.3. Drop nan values
    """
    data['Transaction type'] = data['Transaction type'].replace(to_replace="^Vente", value="Vente", regex = True)
    data = data[data['Transaction type'] == 'Vente']
    data = data.dropna()
    return data
    