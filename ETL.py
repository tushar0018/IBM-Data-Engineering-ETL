import pandas as pd

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe

def extract_from_csv(filename):
    df2 = pd.read_csv(filename,index_col = 0)
    gbp = df2.loc['GBP']['rates']
    usd = df2.loc['USD']['rates']
    exchange_rate = gbp/usd 
    return exchange_rate

def transform(df,exchange_rate):
    df['Market Cap (US$ Billion)'] = (df['Market Cap (US$ Billion)'] * exchange_rate).round(decimals= 3)
    df = df.rename(columns = {'Market Cap (US$ Billion)':'Market Cap (GBP$ Billion)'})
    return df  

def load(targetfile,transformed_data):
    transformed_data.to_csv(targetfile,index= False)  
