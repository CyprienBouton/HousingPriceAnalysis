import pandas as pd
def add_delta_days(data):
    #Divide by oneday to get ride of type timedelta
    oneday = pd.Timedelta(days=1)
    data["Transaction date"]= pd.to_datetime(data["Transaction date"]) #convert str to pd.datetime
    data['Delta days'] = (data['Transaction date'] - data['Transaction date'].min())/oneday
    return data