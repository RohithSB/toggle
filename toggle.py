import requests
import base64
import json

usertoken='ab2e05851aad100a29085e8939a349eb'
string=usertoken+':api_token'
headers={
    'Authorization': 'Basic ' + base64.b64encode(string.encode('ascii')).decode("utf-8")}
# headers={'Authorization':'Basic '+newstring.decode("utf-8")}
print (headers)
url='https://www.toggl.com/api/v8/time_entries'
response=requests.get(url,headers=headers)
if response.status_code!=200:
    print("Login failed. Check your API key")
    quit()

response=response.json()
resp = json.dumps(response)
print (resp)
