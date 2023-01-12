import numpy as np
from scipy import stats

def remove_outlier(data, Nsigma, Bounds):
    """
    1. Create a column 'Cost per m2'
    2. Remove the unlikely transaction based on human judgment: Bounds records
    2. Remove the outlier transactions (to avoid misleading analysis results)
    Bounds is a dictonary with the following keys:
          Built surface min
          Built surface max
          Transaction cost min
          Transaction cost max
          Cost per m2 min
          Cost per m2 max
   """    
    data['Cost per m2']=data['Transaction cost']/data['Built surface']
    data = data[ (data['Built surface'] > Bounds['Built surface min']) &
         (data['Built surface'] < Bounds['Built surface max']) &
         (data['Transaction cost'] > Bounds['Transaction cost min']) &
         (data['Transaction cost'] < Bounds['Transaction cost max']) &
         (data['Cost per m2'] > Bounds['Cost per m2 min']) &
         (data['Cost per m2'] < Bounds['Cost per m2 max'])]
    
    datared = data[['Built surface', 'Transaction cost', 'Cost per m2']]
    data = data[(np.abs(stats.zscore(datared)) < Nsigma).all(axis=1)]
    return data