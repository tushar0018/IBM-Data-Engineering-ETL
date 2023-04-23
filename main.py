from log_details import logging as log
from market_cap import banks_detail
from exchange_rates import exchange_rate_data
from ETL import *

log(" ETL Job Started")

log("Extract Phase Started")

# Banks detail
banks_detail()
filename = 'bank_market_cap.json'
extracted_data = extract_from_json(filename)

#exchange rates
exchange_rate_data()
rates_file ='exchange_rates.csv' 
exchange_rate = extract_from_csv(rates_file)
extracted_data.head(5)
log('Extract phase Ended')

log("Transform phase Started")
transformed_data =transform(extracted_data,exchange_rate)
transformed_data.head(5)
log("Transform phase Ended")

log("Load phase Started")
targetfile = 'bank_market_cap_gbp.csv'
load(targetfile,transformed_data)
log("Load phase Ended")


log("ETL Job Ended")