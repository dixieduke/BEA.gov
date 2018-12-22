# Get per capita personal income from CA1 table for SC counties for all years
import requests
import json

key = "F414B54D-68CF-452A-BFD9-7B7BDA23AE7C"
dataset_name = "RegionalIncome"
parameter_name = "LineCode"
table_name = "CA1"
line_code = "3"
year = "ALL"
geo_fips = "45000"
result_format = "json"
url = "https://apps.bea.gov/api/data?&UserID=" + key + \
"&method=GetData&datasetname=" + dataset_name + \
"&TableName=" + table_name + "&LineCode=" + line_code + \
"&Year=" + year + "&GeoFips=" + geo_fips + \
"&ResultFormat=" + result_format

response = requests.get(url)  # Get response from site
data = response.json() # put response in object

with open("ca1_per_capita_personal_income_sc.json", "w") as jsondata:  # Write json response to file
    jsondata.write(json.dumps(data, sort_keys=True, indent=2))

#for item in data["BEAAPI"]["Results"]["Data"]:  # Printing the info
#    number_meaning = item["CL_UNIT"]
#    population = item["DataValue"]
#    table_code = item["Code"]
#    location_code = item["GeoFips"]
#    location_name = item["GeoName"]
#    year = item["TimePeriod"]
#    dollar_exponent = item["UNIT_MULT"]
#    print(year + ": " + location_name + "| " + population)