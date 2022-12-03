def keep_flat(data):
  #function to delete house, dependance, commercial local, industrial local,...
  data=data[(data['Type of property']=='Appartement')] #we keep only flats.
  data.loc[data['Type of property']=="Appartement", 'Type of property'] = "Flat" #rename the values
  data = data.drop('Type of property', axis=1) #don't need this column anymore
  return data