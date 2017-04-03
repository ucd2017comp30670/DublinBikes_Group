import requests
import json
from pprint import pprint

APIKEY = "58c66e96f312aedb78f7f726e5da74ec7ade7e33"
NAME = "Dublin"
STATIONS_URI = "https://api.jcdecaux.com/vls/v1/stations"
r = requests.get(STATIONS_URI, params={"apiKey": APIKEY,
 "contract": NAME})

a = (json.loads(r.text)[0])
print(a)
