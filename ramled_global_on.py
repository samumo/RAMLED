import pip._vendor.requests as requests
import json

#############################
#############################
# UNTESTED!!    

url = 'http://192.168.0.100:8080/api/v1.0/set_led/global'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


# Object to contain the JSON request data
json_request = {"chan": "global", "chan": "1", "on": True, "fade": 0.1, "auto_off": 0}

# Convert the object to a string
json_data = json.dumps(json_request)

print("Request: " + json_data)

# Make REST POST to the url with the json string as the data
response = requests.post(url, data=json_data, headers=headers)

print(response)


#  curl --request POST 'http://10.1.14.72:8080/api/v1.0/set_led/global' --header 'Content-Type: application/json' --data-raw '{"chan": "global", "chan": "1", "on": flase, "fade": 0.1, "auto_off": 0}'