import requests
import json


url='https://api.agify.io?name='



isimler=open('isimler.txt', 'r')

for x in isimler:
    y = url + x
    y = y.strip()
    age_request = requests.get(url=y)
    jsonload = json.loads(age_request.text)
    print(jsonload)

isimler.close()