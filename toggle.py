import requests
import base64
import datetime
import json

yest = datetime.date.today()-datetime.timedelta(1)
count = 0
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
resps = json.loads(json.dumps(response))

for resp in resps:
    if resp['at'].split("T")[0] == str(datetime.date.today()-datetime.timedelta(1)):
        count = count + 1

if count > 1:
    print ("Timeheet Updated")
else:
    print("Timesheet Not Updated")
