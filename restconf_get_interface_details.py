import requests

import urllib3

from requests.auth import HTTPBasicAuth

from getpass import getpass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = getpass("Please enter the username: ")

password = getpass("Please enter the password: ")

ios_cred = HTTPBasicAuth(username=username,password=password)

ios_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"

ios_headers = {"Accept": "application/yang-data+json"}

try:


   interface_query = requests.get(url=ios_url,auth=ios_cred,headers=ios_headers,verify=False,timeout=10)
 
   if interface_query.status_code == 200:

      print("The status code is: ",interface_query.status_code)

      print("The actual response is: ",interface_query.text)
   
   else:
   
      print("The query has failed and the status code is: ",interface-query.status_code)
   
      print("The response is: ",interface_query.text)   

except Exception as e:

   print("The request could not be completed and the error is: ",e)




