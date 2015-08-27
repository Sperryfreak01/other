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
url = "https://api.arenasolutions.com/v1/"

# Login first
endpoint = 'login'
headers = {"content-type": "application/json"}
body = {"email": "pfriedhoff@nextracker.com", "password": "", "workspaceId": "896561705"}
r = requests.post(url + endpoint, headers = headers, data = json.dumps(body))
login_data = r.json()

# Search for item object. Returns 'Compact Item' object
endpoint = 'items'
headers["arena_session_id"] = login_data["arenaSessionId"]
params  = {'number': '5113'}
r = requests.get(url + endpoint, headers = headers, params = params)
item = r.json()

# Get item revisions. Returns 'revision' object
item_guid = item['results'][0]['guid']

# Logout
# r = requests.get('https://api.arenasolutions.com/v1/logout', headers = headers)
# print ('Logout code is: %s' % r.status_code)