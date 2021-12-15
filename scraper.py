import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 

url = 'https://sbahn.berlin/en/plan-a-journey/timetable-changes/?tabs=tbc-l7'
response = requests.get(url)
text = response.text
data = BeautifulSoup (text, 'html.parser')

#print (data.prettify())


line = []
connection = []
regularity = []

train_div = data.find_all('div' , class_= 'c-construction-announcement-body')
line_25 = train_div[0]

print(line_25.a.text)

conn_25 = train_div[1]
print(conn_25.h3.text)

date_25 = train_div[2]
print (data.find_all('div' , class_='o-timespan__center o-timespan__cp'))




for info in train_div:

    line_no = info.a.text
    line.append(line_no)
    print (line_no)


    path= info.h3.text
    connection.append(path)
    print(path)

    time= info.find_all('div' , class_='o-timespan__center o-timespan__cp')
    for i in time:
        date= i.text
        regularity.append(date)
        print (date)

'''
    print (line)
    print(connection)
    print (regularity)



trains = pd.DataFrame({
'lineNumber' : line,
'lineName' = connection,
'date' = regularity,


})
'''



