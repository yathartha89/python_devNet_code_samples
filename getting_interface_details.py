from netmiko import ConnectHandler

import re

from cred import iosxe1 as device

hosts = {"hostname": "R1", "ip": "10.10.20.48"} 

num_tries = 1

max_tries = 3

while num_tries < max_tries:

   try:
      
      ch = ConnectHandler(

               ip=hosts["ip"],
               username=device["username"],
               password=device["password"],
               port=device["port"],
               device_type=device["type"]   
 

)


      print(f"The connection to {hosts['hostname']} has been established successfully")
     

      interface = ch.send_command("sh run int GigabitEthernet1")
      print(interface)
      break
        
   except Exception as e:
      print("The SSH connection failed and the error is: ", e)

      num_tries+=1


try:
 
   name = re.search(r'interface (\S+)',interface).group(1)

   description = re.search(r'description (.*)',interface).group(1)

   ip_info = re.search(r'ip address (\S+) (\S+)',interface)

   ip = ip_info.group(1)

   mask = ip_info.group(2)

   print(f"The interface {name} has an IP address of {ip} and the mask is {mask}")


except Exception as e:
   print("The interface does not exist and the error is: ",e)






