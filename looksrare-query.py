import requests
import urllib.request, json
import time

count = 0
coll = 2
while (count == 0):
	time.sleep(5)
	url = "https://api.looksrare.org/api/v1/collections/listing-rewards"

	headers = {
		"Accept": "application/json",
	}

	response = requests.get(url, headers=headers)
	data22 = response.json()
	i=0
	while(i<=10):
		address = data22['data'][i]['collection']['address']
		if(address == "0x34d85c9CDeB23FA97cb08333b511ac86E1C4E258"):
			name = data22['data'][i]['collection']['name']
			floorGlobal = (float(data22['data'][i]['floorGlobal'])/(10**18))
			x = name
			y = str(round(floorGlobal,3))
			z = str(round(floorGlobal*(1.1),3))
			z2 = str(round(floorGlobal*(1.2),3))
			z3 = str(round(floorGlobal*(1.3),3))
			z4 = str(round(floorGlobal*(1.4),3))

			print(x + ' -- F: '+y + ' -- 1.1x: '+ z + ' -- 1.2x: '+ z2 + ' -- 1.3x: '+ z3 + ' -- 1.4x: '+ z4)
			
			
		else:
			name = data22['data'][i]['collection']['name']
		i=i+1
