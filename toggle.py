import requests
import base64
import datetime
import json

class Timesheet():

    # Toggle tokens
    usertoken = 'ab2e05851aad100a29085e8939a349eb'
    timesheet_token = "{}:api_token".format(usertoken)
    url = 'https://www.toggl.com/api/v8/time_entries'

    def authenticate_toggle(self):
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(self.timesheet_token.encode('ascii')).decode("utf-8")
        }
        # headers={'Authorization':'Basic '+newstring.decode("utf-8")}
        print (headers)
        response = requests.get(self.url,headers=headers)
        if response.status_code != 200:
            print("Login failed. Check your API key")
           quit()

        response = response.json()
        timesheet_data = json.loads(json.dumps(response))

        return timesheet_data

    def check_timesheet(self, timesheet_data):
        count = 0
        yest = str(datetime.date.today() - datetime.timedelta(1))


        # Process Timesheet
        for data in timesheet_data:
            if data['at'].split("T")[0] == yest:
                count = count + 1

        if count > 1:
            print ("Timeheet Updated")
        else:
            print("Timesheet Not Updated")


t = Timesheet()
print "Get the details from the toggle"
timesheet_data = t.authenticate_toggle()
print len(timesheet_data)
print "Check if this guy has updated timesheet"
t.check_timesheet(timesheet_data)
