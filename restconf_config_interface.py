import requests

from requests.auth import HTTPBasicAuth

from getpass import getpass

import json

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = getpass("Please enter the username: ")

password = getpass("Please enter the password: ")

ios_cred = HTTPBasicAuth(username=username,password=password)

ios_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"

ios_headers = {"Content-Type": "application/yang-data+json"}

interface_config = {
         "ietf-interfaces:interface": {

                 "name": "Loopback3",
                 "description": "Interface configured by YV using restconf",
                 "type": "iana-if-type:softwareLoopback",
                 "enabled": "true",
                 "ietf-ip:ipv4": {
                       "address": [
                           {
                             "ip": "2.2.2.2",
                             "netmask": "255.255.255.255",
                             
}

]

}
} 
}

def interface():
   try:

      config = requests.post(url=ios_url,auth=ios_cred,headers=ios_headers,data=json.dumps(interface_config),verify=False) 

      if config.status_code in [200, 201, 204]:
    
         print("The status code is: " + str(config.status_code))

         print("The interface config has been pushed successfully")


      else:

         print("The status code is :" + str(config.status_code))

         print("\nThe interface config has not been pushed successfully")

         print("\nThe response is :",config.text)
   except Exception as e:

      print("There is error in EST connection and the error is :",e)



interface()







