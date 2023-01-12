import re

def get_district(Town):
    """
    The purpose of this function is to get the district number from the Town
    """
    assert type(Town)==str
    return float(re.search(r'[0-9]+',Town).group())#In Paris Town is like "Paris 10e arrondissement

def keep_paris(data):
    """we only focus on flat in PAris
        1. Remove all accomodation that are not in Paris
        2. Replace the column Town by the column District
    """
    data = data[data['Town'].apply(lambda x: x[:6])=="Paris "]
    data['District'] = data.apply(lambda x: get_district(x.Town), axis=1)
    data = data.drop('Town', axis=1)
    return data