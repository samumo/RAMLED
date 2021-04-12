import requests
import json

#############################
#############################
# UNTESTED!!    

url = 'http://192.168.0.100:8080/api/v1.0/set_idle_mode'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


# Object to contain the JSON request data
json_request = {"brightness": "40", "cmd": "SetIdleMode", "enabled": 'true', "start_delay": "58", "intensity": "112", "fade": 1.4}

# Convert the object to a string
json_data = json.dumps(json_request)

print("Request: " + json_data)

# Make REST POST to the url with the json string as the data
response = requests.api.post(url, data=json_data, headers=headers)

print(response)