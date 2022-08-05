import requests
import json

facts = set()
jsonDict = dict()

index = 1
url = "https://catfact.ninja/facts"

while url != "":
    link = requests.get(url=url)
    kafa = json.loads(link.text)

    for x in kafa['data']:
        facts.add(x['fact'])
        jsonDict[index] = x['fact']
        index += 1

    if kafa['next_page_url'] is None:
        url = ""
    else:
        url = kafa['next_page_url']

file = open('facts.txt', 'a')
fileJSON = open('facts.json', 'a')
fileJSON.write(json.dumps(jsonDict, indent = 4))
for x in facts:
    file.write(x+ '\n')

file.close()
fileJSON.close()