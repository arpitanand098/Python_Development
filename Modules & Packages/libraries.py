import random
print(random.randint(1,10))
print(random.choice(['arpit','shristy','abhi']))

### File And Directory Access

import os
print(os.getcwd())

## High level operations on files and collection of files
import shutil
shutil.copyfile('source.txt', 'Second_oct.txt')

## Data serialization

import json
data = {'name': 'Arpit','age': 20}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

###csv

import csv
with open('example.csv', mode='w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Arpit', 20])

with open('example.csv', mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

## Date_Time
from datetime import datetime,timedelta

time = datetime.now()
print(time)

yesterday = time-timedelta(days =1)

print(yesterday)

