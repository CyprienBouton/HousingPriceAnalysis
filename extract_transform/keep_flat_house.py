def keep_flat_house(data):
  #function to delete dependance, commercial local, industrial local,...
  data=data[(data['Type of property']=='Maison')^(data['Type of property']=='Appartement')] #we keep only flats and houses.
  data['Type of property']=data['Type of property'].replace(to_replace = 'Maison',value = 'House')
  data['Type of property']=data['Type of property'].replace(to_replace = 'Appartement',value = 'Flat')#rename the values
  return data