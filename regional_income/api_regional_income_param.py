import requests
import json

key = "F414B54D-68CF-452A-BFD9-7B7BDA23AE7C"
datasetname = "RegionalIncome"
url = "https://apps.bea.gov/api/data?&UserID=" + key + "&method=getparameterlist&datasetname=" + datasetname

response = requests.get(url)  # Get response from site
data = response.json() # put response in object

with open("regional_income_param.json", "w") as jsondata:  # Write json response to file
    jsondata.write(json.dumps(data, sort_keys=True, indent=2))


for item in data["BEAAPI"]["Results"]["Parameter"]:
    name = item["ParameterName"]
    description = item["ParameterDescription"]
    required = item["ParameterIsRequiredFlag"]
    print(name + ": " + description + " | " + required + "\n")


