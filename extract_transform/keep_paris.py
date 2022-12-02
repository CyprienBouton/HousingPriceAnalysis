import re

def get_district(Town):
    assert type(Town)==str
    return re.search(r'[0-9]+',Town).group()

def keep_paris(data):
    """we only focus on flat in PAris
        1. Remove all house and flat that are not in Paris
        2. add a column District
        3. Remove useless column: Town, Postcode, 
    """
    data = data[data['Town'].apply(lambda x: x[:6])=="Paris "]
    data["District"] = data['Town'].apply(get_district)
    data = data.drop('Town', axis=1)
    return data