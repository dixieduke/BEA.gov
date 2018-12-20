# Initial attempt at retrieving info from the .gov site
import requests
import json

key = "F414B54D-68CF-452A-BFD9-7B7BDA23AE7C"
url = "https://apps.bea.gov/api/data?&UserID=" + key + "&method=GETDATASETLIST&"

response = requests.get(url)

#print(response.status_code)  # Print response status code
#print(response._content)  # Print response content
#print(response.json())  # Prints JSON response

with open("datasets.json", "w") as jsondata:
    jsondata.write(json.dumps(response.json(), sort_keys=True, indent=2))