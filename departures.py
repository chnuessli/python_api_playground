import requests
import json

url = "http://transport.opendata.ch/v1/stationboard?station=Chur"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

pretty_json = json.loads(response.text)
print (json.dumps(pretty_json, indent=2))

with open('departure.json', 'w', encoding='utf-8') as outfile:
    json.dump(pretty_json, outfile, ensure_ascii=False, indent=4)