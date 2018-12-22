import requests
import json

key = "F414B54D-68CF-452A-BFD9-7B7BDA23AE7C"
datasetname = "RegionalIncome"
parametername = "GeoFips"
url = "https://apps.bea.gov/api/data?&UserID=" + key + "&method=GetParameterValues&datasetname=" + datasetname + "&ParameterName=" + parametername

response = requests.get(url)  # Get response from site
data = response.json() # put response in object

with open("regional_income_param_gfvalues.json", "w") as jsondata:  # Write json response to file
    jsondata.write(json.dumps(data, sort_keys=True, indent=2))


for item in data["BEAAPI"]["Results"]["ParamValue"]:
    description = item["Desc"]
    key = item["Key"]
    print(description + ": " + key)


