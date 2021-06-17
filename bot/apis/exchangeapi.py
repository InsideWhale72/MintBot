import requests
import json

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
exchangedata = response.json()
if response:
    exchangedata = json.loads(response.text)
    file = open("exchangecache.json", "w+")
    file.write(response.text)
    file.close()
else:
    file = open("exchangecache.json", "r")
    exchangecachedata = file.read()
    file.close()
    exchangedata = json.loads(cachedata)

