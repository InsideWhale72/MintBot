import requests
import json

response = requests.get('https://ll.thespacedevs.com/2.1.0/launch/upcoming/?mode=list&limit=5')
if response:
    rocketapidata = json.loads(response.text)
    file = open("rocketcache.json", "w+")
    file.write(response.text)
    file.close()
else:
    file = open("rocketcache.json", "r")
    cachedata = file.read()
    file.close()
    rocketapidata = json.loads(cachedata)

for i in rocketapidata["results"]:
  print(i["name"])