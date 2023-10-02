import os
import requests
import csv
import datetime



current_date = datetime.date(2022,2,2)

while(current_date != datetime.date(2022,4,20)):
    URL = "https://www.cbr-xml-daily.ru/archive/"+str(current_date).replace("-","/")+"/daily_json.js"
    html_page = requests.get(URL)
    json_page = html_page.json()
    if("error" in json_page):
        current_date += datetime.timedelta(days=1)
        continue
    else:
        usd_value = json_page["Valute"]["USD"]["Value"]
        data = [str(current_date)], [str(usd_value)]
        with open("data.csv", "a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
        current_date += datetime.timedelta(days=1)