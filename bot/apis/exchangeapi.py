import requests
import json

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()
if response:
    exchangedata = json.loads(response.text)
    file = open("exchangecache.json", "w+")
    file.write(response.text)
    file.close()
else:
    file = open("exchangecache.json", "r")
    cachedata = file.read()
    file.close()
    exchangedata = json.loads(cachedata)
print(data)
