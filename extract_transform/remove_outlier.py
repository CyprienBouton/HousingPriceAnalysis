def remove_outlier(data, Nsigma, Bounds):
    """
    1. Remove the unlikely transaction based on human judgment: Bounds records
    2. Remove the outlier transactions (to avoid misleading analysis results)
    Bounds is a dictonary with the following keys: 
        Built surface min
        Built surface max
        Ground surface max
        Transaction cost min
        Transaction cost max 
    """    
    
    data = data[ (data['Built surface'] > Bounds['Built surface min']) &
         (data['Built surface'] < Bounds['Built surface max']) &
         (data['Ground surface'] < Bounds['Ground surface max']) &
         (data['Transaction cost'] > Bounds['Transaction cost min']) &
         (data['Transaction cost'] < Bounds['Transaction cost max'])]
    
    data = data[(np.abs(stats.zscore(datared)) < Nsigma).all(axis=1)]
    return data