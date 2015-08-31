"""
Script to pull data from the API for processing

refer to: https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/
and: http://stackoverflow.com/questions/30259452/proper-way-to-consume-data-from-restful-api-in-django
"""
import requests, json

"""
Google Directions API example
"""
# Refer to: https://developers.google.com/maps/documentation/directions/intro#DirectionsRequests
# url = 'https://maps.googleapis.com/maps/api/directions/json' 

# params = {
# 'origin': 'Toronto',
# 'destination': 'Montreal',
# 'key':'AIzaSyAfY4klBTbZf16oY_hcRcH2Cr4XjEFhJHI'
# }

# r = requests.get(url, params = params)
# data = r.json()
# print (r.status_code)

"""
Arena PLM API
"""
# Find all values of a given key for nested dict or list. Use with: list(find('guid', results_data))
def find(key, dictionary):
	for k, v in dictionary.items():
		if k == key:
			yield v
		elif isinstance(v, dict):
			for result in find(key, v):
				yield result
		elif isinstance(v, list):
			for d in v:
				for result in find(key, d):
					yield result

url = "https://api.arenasolutions.com/v1/"

# Login to get Arena session Id
headers = {"content-type": "application/json"}
body = {"email": "pfriedhoff@nextracker.com", "password": "", "workspaceId": "896561705"}
r = requests.post(url + 'login', headers = headers, data = json.dumps(body))
print ('Login code is: %s' % r.status_code)

# Search for Item based on number to get its GUID
headers["arena_session_id"] = r.json().get('arenaSessionId')
params  = {'number': 'PDM-000002'}
r = requests.get(url + 'items', headers = headers, params = params)
results_data = r.json()

print (list(find('guid', results_data)))

# Logout
r = requests.get('https://api.arenasolutions.com/v1/logout', headers = headers)
print ('Logout code is: %s' % r.status_code)