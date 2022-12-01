def add_delta_days(data):
    #Divide by oneday to get ride of type timedelta
    oneday = pd.Timedelta(days=1)
    data['Delta days'] = (data['Transaction date'] - data['Transaction date'].min())/oneday
    return data
