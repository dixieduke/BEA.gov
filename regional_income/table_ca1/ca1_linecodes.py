# This should provide a list of line codes for the CA1 table
import requests
import json

key = "F414B54D-68CF-452A-BFD9-7B7BDA23AE7C"
dataset_name = "RegionalIncome"
parameter_name = "LineCode"
table_name = "CA1"
result_format = "json"
url = "https://apps.bea.gov/api/data?&UserID=" + key + \
"&method=GetParameterValuesFiltered&datasetname=" + dataset_name \
+ "&TargetParameter=" + parameter_name + "&TableName=" + table_name + \
"&ResultFormat=" + result_format

response = requests.get(url)  # Get response from site
data = response.json() # put response in object

with open("regional_income_ca1_lc.json", "w") as jsondata:  # Write json response to file
    jsondata.write(json.dumps(data, sort_keys=True, indent=2))

for item in data["BEAAPI"]["Results"]["ParamValue"]:  # Printing the info
    description = item["Desc"]
    key = item["Key"]
    print(key + ": " + description)