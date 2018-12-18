# Initial attempt at retrieving info from the .gov site
import requests

key = "F414B54D-68CF-452A-BFD9-7B7BDA23AE7C"
url = "https://apps.bea.gov/api/data?&UserID=" + key + "&method=GETDATASETLIST&"

response = requests.get(url)
print(response.status_code)
print(response._content)