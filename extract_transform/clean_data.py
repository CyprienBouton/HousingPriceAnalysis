def clean_data(data):
    """
    Clean the pandas dataframe as follow:
        1. Replace by type 'Vente' (sell) all the naming involving vente (sell) activity.
        2. Remove all transactions not 'Vente' (sell)  (eg 'echange', 'expropriation',...)
        3. Remove the column Transaction type
        4. Drop nan values
    """
    data['Transaction type'] = data['Transaction type'].replace(to_replace="^Vente", value="Vente", regex = True)
    data = data[data['Transaction type'] == 'Vente']
    data = data.dropna()
    data = data.drop("Transaction type", axis=1)
    return data
    