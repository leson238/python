
# Below are the list of Packages used in this Script.We have used a Python Library called 'Requests' which is not bundled by default with Python installation.
# More information on this Package and the instructions on installing it on the Application Server are available in the following link.
# http://docs.python-requests.org/en/latest/user/install/#install

import sys
import requests
import json
import datetime

# Create a Session Object that will be used to pass different parameters across the HTTP requests.
# All the parameters like the ServerName , protocol , portnumber and Technician API key that are used in the Script are Input here.Please update this based on your Environment.

# Update this link with the protocol and servername:portnumber values of the ServiceDesk Plus application.
appUrl = "seocd5-hcm.supercloud.vn:3046"
# Replace 374C0176-A6BF-4CDC-8E05-9731F66FAE71 with a Technician's API key.
TechnicianKey = '09DC84A8-37ED-4496-8F4F-25CE9B9214EC'
resultjson = {}
url = ""
# File containing request details will be stored as json object and the file path will be passed as argument to the script replacing the $COMPLETE_JSON_FILE argument
file_Path = sys.argv[1]


def submitToApp(requestid, opsName, data):
    if(opsName == "DELETE_REQUEST"):
        url = appUrl + "/sdpapi/request/" + workorderid
    if(opsName == "ADD_REQUEST"):
        url = appUrl + "/sdpapi/request/"
    with requests.Session() as s:
        data = {'INPUT_DATA': jsonData, 'TECHNICIAN_KEY': TechnicianKey,
                'format': 'json', 'OPERATION_NAME': opsName}
    r = s.post(url, data, verify=False)
    return(r)


# Load the json content which contains request details
with open(file_Path) as data_file:
    data = json.load(data_file)
requestObj = data['request']


# Assigning value got from the Request JSON Object to variables which can be used in constructing the JSON for creating the New Request
workorderid = requestObj['WORKORDERID']
#technician = requestObj['TECHNICIAN']
# Reqlevel =  requestObj['LEVEL'] # This is the Level Value got from the Request details.
#status =  requestObj['STATUS']
requester = requestObj['REQUESTER']
#createdby = requestObj['CREATEDBY']
subject = requestObj['SUBJECT']
#requesttemplate = requestObj['REQUESTTEMPLATE']
description = requestObj['DESCRIPTION']
#priority = requestObj['PRIORITY']
#site = requestObj['SITE']
#category = requestObj['CATEGORY']
#subcategory = requestObj['SUBCATEGORY']
#item = requestObj['ITEM']
#impact = requestObj['IMPACT']
#urgency = requestObj['URGENCY']
subject = subject.lower()
template = ""

if ("request for laptop" in subject):
    template = "Request a Laptop"
elif ("new employee request" in subject):
    template = "New Employee Onboarding"
elif ("request for a mail list" in subject):
    template = "Request a new mailing list creation"


if(template != ""):
    operationJson = {}
    requestJson = {}
    requestinside = {}
    requestinside['requester'] = requester
    requestinside['subject'] = template + " by "+requester
    requestinside['requesttemplate'] = template
    requestinside['description'] = description
    requestJson['details'] = requestinside
    operationJson['operation'] = requestJson
    jsonData = json.dumps(operationJson)

    r = submitToApp(workorderid, "ADD_REQUEST", jsonData)
    result = submitToApp(workorderid, "DELETE_REQUEST", jsonData)

    if(r.status_code == 200):
        responseobj = r.json()
        status = responseobj['operation']['result']['status']
        message = responseobj['operation']['result']['message']

        # Checking if the status value in the return json is set as "Success".
        if status == 'Success':
            resultjson["result"] = "success"
            resultjson["message"] = "Template set Successfully"
            # This message will be shown if the Level was updated Successfully.
            print(resultjson)

        else:
            resultjson["result"] = "Failed"
            resultjson["message"] = "status " + status + " Message " + message
            print(resultjson)
    else:
        resultjson["result"] = "Failed"
        resultjson["message"] = r.text
        print(resultjson)
else:
    resultjson["result"] = "Success"
    resultjson["message"] = "No Changes Done"
    print(resultjson)
