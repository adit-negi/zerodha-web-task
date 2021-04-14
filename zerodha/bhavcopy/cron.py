from .models import *
from django.core.cache import cache
from io import BytesIO
import io
from zipfile import ZipFile
import csv
import requests
import datetime
def cron_job():

    day = str(datetime.datetime.now().day -1)
    if int(day)<10:
        day = "0"+str(day)
    month = str(datetime.datetime.now().month)
    if int(month)<10:
        month = "0"+str(month)
    url ='https://www.bseindia.com/download/BhavCopy/Equity/EQ' +day+month+'21_CSV.ZIP'
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    zip_file = ZipFile(BytesIO(response.content))
    for zip_info in zip_file.infolist():
        with zip_file.open(zip_info) as file:
            with io.TextIOWrapper(file) as text:
                csvreader = csv.reader(text)
                for i in csvreader:
                    
                    cache.set(i[1].strip(), {'code':i[0], 'name':i[1], 'open': i[4], 'high':i[5] , 'low':i[6] , 'close':i[7]})
                    print(i)

#'955TMFPERP  '