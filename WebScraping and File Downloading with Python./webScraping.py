import requests
from bs4 import BeautifulSoup
import pandas as pd

# 2022-12-01 08:06

# taking input
pat = input("enter date and time: ")
pattern = pat+"  "

x = str(pat.split("-"))
y = x[2:6]

url = f"https://www.ncei.noaa.gov/data/local-climatological-data/access/{y}/"
file = requests.get(url)

# extracting csv
soup = BeautifulSoup(file.content, "html.parser")
table = soup.find('table')
rows = table.find_all('tr')
td_list = table.find_all('td')
i = 0
for elem in td_list:
    if elem.text == pattern:
        ind = i
    i += 1
file_id = td_list[ind-1].text

# building url for csv
url1 = f"https://www.ncei.noaa.gov/data/local-climatological-data/access/{y}/{file_id}"

# downloading csv
req = requests.get(url1)
open(file_id, 'wb').write(req.content)
print("file downloaded")


# reading csv using python
data = pd.read_csv(file_id)

data['HourlyDryBulbTemperature'] = pd.to_numeric(data['HourlyDryBulbTemperature'],errors = 'coerce')

# printing data on command line
print(data[data.HourlyDryBulbTemperature == data.HourlyDryBulbTemperature.max()])
