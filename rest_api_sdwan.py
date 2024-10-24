import requests

from getpass import getpass

from requests.auth import HTTPBasicAuth

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = getpass("Please enter the username: ")

password = getpass("Please enter the password: ")

ios_cred = HTTPBasicAuth(username=username,password=password)

ios_url = "https://10.10.20.90"

ios_headers = {"Accept": "application/json"}

main_url = requests.get(url=ios_url,auth=ios_cred,headers=ios_headers,verify=False)

if main_url.status_code == 200:

   print("The request is successful and the response status code is: " + str(main_url.status_code))
   print()
   print("The response is: " + str(main_url.text))

else:

   print("The request is not successful and the status code is: " + str(main_url.status_code))




