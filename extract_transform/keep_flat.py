def keep_flat(data):
  #function to delete house, dependance, commercial local, industrial local,...
  data=data[(data['Type of property']=='Appartement')] #we keep only flats.
  data['Type of property']=data['Type of property'].replace(to_replace='Appartement',
  value = 'Flat') #rename the values
  return data