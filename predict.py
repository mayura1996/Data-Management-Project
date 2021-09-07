# Import DecisionTreeClassifier from sklearn.tree
from sklearn.tree import DecisionTreeClassifier

# Import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

# Import LogisticRegression
from sklearn.linear_model import LogisticRegression

#Import Others
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, auc
from sklearn.linear_model import LogisticRegression
import time
import numpy as np
import pickle
from datetime import datetime

import requests,json
import test

# api_key = "Your_API_Key"
# base_url = "http://api.openweathermap.org/data/2.5/weather?"
# complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# a=4
# b=3
def algo(latitude,longitude,Pickled_LR_Model):
    # Pkl_Filename = "RF_limit.pickle"  
    # with open(Pkl_Filename, 'rb') as file:  
    #     Pickled_LR_Model = pickle.load(file)
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
# Start_Lat
# Start_Lng
# Temperature(F)
# Humidity(%)
# Pressure(in)
# Wind_Speed(mph)
    lat,lon,temperature,pressure,humidity,windSpeed = test.getData(latitude,longitude)
    print(lat)
    # instance = [[ 3.03697120e+01, -32.08479140e+01,  10.11000000e+01,  18.40000000e+01,
    # 1.51094556e+08,  1.77802993e+00]]
    instance = [[lat,lon,temperature,pressure,humidity,windSpeed ]]
    print(type(instance))


    print(np.array([instance[0]]))


    return str(Pickled_LR_Model.predict(np.array([instance[0]]))[0])

# Pkl_Filename = "RF_limit.pickle"  
# with open(Pkl_Filename, 'rb') as file:  
#         Pickled_LR_Model = pickle.load(file)

# if __name__ == "__main__":
#     # Pkl_Filename = "RF_limit.pickle"  
#     # with open(Pkl_Filename, 'rb') as file:  
#     #     Pickled_LR_Model = pickle.load(file)
#     # algo(Pickled_LR_Model)

#     print("mayura")
