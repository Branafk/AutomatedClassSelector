from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

import bs4
import requests
import json
import math
import lxml.html as lh
import pandas as pd

my_url = 'https://www.scu.edu/apps/courseavail/?p=schedule'

#Opening up connection, grabbing the page 
page = requests.get(my_url)

#Store the contents of the website under doc 
doc = lh.fromstring(page.content)


# HTML parsing 
tr_elements = doc.xpath('//tr')

#Check the length of the first 12 rows 
[len(T) for T in tr_elements[:12]]

#Create empty list 
col = []
i = 0 

#For each row, store each first elemtn (header) and an empty list 
for t in tr_elements[0]:
	i += 1 
	name = t.text_content()
	print('%d:"%s"'%(i,name))
	col.append((name, []))

#Print check 
print(tr_elements)

#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T = tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=10:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1


