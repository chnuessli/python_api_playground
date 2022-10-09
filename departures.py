import requests
import json

url = "http://transport.opendata.ch/v1/stationboard?station=Chur"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print (response.text)

json_string = response.text

with open('departure.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_string, outfile, ensure_ascii=False, indent=4)