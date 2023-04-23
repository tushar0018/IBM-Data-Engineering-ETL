import requests
import pandas as pd
import json

def exchange_rate_data():
    url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=***********" #Make sure to change ******* to your API key.
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame.from_dict(data)
    df = df.drop(['success','timestamp','base','date'],axis=1)
    df.to_csv("exchange_rates.csv",header = True)
