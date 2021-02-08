import requests
import json


url = 'http://192.168.0.100:8080/api/v1.0/set_name_mask'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# Name array containing strings of which LEDs to turn on
# If two or more LEDs have the same name each matching LED will be turned on
name_array = []
name_array.append('B2.1.4')
'''
name_array.append('B2.1.2')
name_array.append('B2.1.3')
'''

# Object to contain the JSON request data
# auto_off can be left out of set to 0 for the RAM LED to hold the pattern until the next SetNameMask
json_request = {}
json_request['fade'] = 0.3
json_request['auto_off'] = 20
json_request['name_mask'] = name_array

# Convert the object to a string
json_data = json.dumps(json_request)

print("Request: " + json_data)

# Make REST POST to the url with the json string as the data
response = requests.post(url, data=json_data, headers=headers)

print(response)
