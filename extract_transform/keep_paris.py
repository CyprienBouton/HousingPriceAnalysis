import re

def get_district(Town):
    """
    The purpose of this function is to get the district number from the Town
    In Paris Town is like "Paris 10e arrondissement"
    """
    assert type(Town)==str
    return re.search(r'[0-9]+',Town).group()

def keep_paris(data):
    """we only focus on flat in PAris
        1. Remove all accomodation that are not in Paris
        2. Add a column District
        3. Remove Town column
    """
    data = data[data['Town'].apply(lambda x: x[:6])=="Paris "]
    data["District"] = data['Town'].apply(get_district)
    data = data.drop('Town', axis=1)
    return data