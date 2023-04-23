from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

url = "https://companiesmarketcap.com/banks/largest-banks-by-market-cap/"
path = "~/Music/chromedriver_linux64" #enter your own path

option = Options()
option.add_argument('--headless')

driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service= driver_service , options=option)
driver.get(url)

def banks_detail():
  #web-page contents
  data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
  container_name = driver.find_elements(by='xpath',value="//tr/td/div/a/div[@class='company-name']")
  container_val = driver.find_elements(by='xpath',value="//tr/td[@class='td-right' and contains(text(),'B')]")
   
  for i in range(100):
        Bank = container_name[i].text
        marketCap = float(container_val[i].text[1:-2])
        data.loc[len(data)] = [Bank,marketCap]

  with open('bank_market_cap.json', 'w') as f:
          f.write(data.to_json(orient='records', lines=True))
           
banks_detail() 