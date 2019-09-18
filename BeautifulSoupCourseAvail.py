from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup 

import bs4
import requests
import json
import math
import lxml.html as lh
import pandas as pd


bs = BeautifulSoup('https://www.scu.edu/apps/courseavail/?p=schedule', "lxml")
table_body = bs.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [x.text.strip() for x in cols]
    print(cols)
