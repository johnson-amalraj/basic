# Requirements for web scrape
# pip install maya
# pip install beautifulsoup4
# pip install requests
# pip install pandas

# its used to scrape details from other website and we will host into our own app/website
# Basically scrape meaning was get/search content from selected page(webpage/pages in book)

import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=32.66958000000005&lon=-85.39299999999997')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup) # it will print content as html
# print(soup.find_all('a')) # it will grab the selected details
week = soup.find(id = 'seven-day-forecast-body') # it will get the container data under 'seven-day-forecast-body'
# print(week)

items = week.find_all(class_ = 'tombstone-container')
# print(items[0])

# print(items[0].find(class_ = 'period-name').get_text())
# print(items[0].find(class_ = 'short-desc').get_text())
# print(items[0].find(class_ = 'temp').get_text())

period_names       = [item.find(class_ = 'period-name').get_text() for item in items]
short_descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
temperatures       = [item.find(class_ = 'temp').get_text() for item in items]
# print(period_names)
# print(short_descriptions)
# print(temperatures)


# below will print in table format by using 'pandas'
weather_details = pd.DataFrame(
    {
       'Period'      : period_names,
       'Description': short_descriptions,
       'Temperature' : temperatures, # Always add coma if you need to add more details in future
    }
)
print(weather_details)
weather_details.to_csv('weather_report.csv')
