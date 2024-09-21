from netmiko import ConnectHandler

import re

from cred import iosxe1 as device

hosts = {"host": "R1", "ip": "10.10.20.48"}

def check_connection(num_tries,max_tries):
  
   while num_tries < max_tries:
      
      try:
         
         ch = ConnectHandler(

             ip=hosts["ip"],
             username=device["username"],
             password=device["password"],
             port=device["port"],
             device_type=device["type"]

   
)

         print(f"The connection to {hosts['host']} is established successfully")


         return ch
        
         break

      except Exception as e:
         print("The connection cannot be established and the error is: ",e)
         num_tries +=1

def config_commands(ch,commands):
 
   interface = ch.send_command(commands)

   return interface



def pattern_matching(interface):
   try:

      name = re.search(r'interface (\S+)',interface)

      if name:
         name1 = name.group(1)
        
      description = re.search(r'description (.*)',interface)
      if description:
         description1 = description.group(1)
      
      ip_info = re.search(r'ip address (\S+) (\S+)',interface)
      if ip_info:

         ip = ip_info.group(1)

         mask = ip_info.group(2)


      print(f"The interface {name1} has an ip address of {ip} and a mask of {mask}")

   except Exception as e:
      print("The info could not be found and the error is: ",e)

ch = check_connection(1,3)


if ch:

   commands = input("Enter the command: ")

   interface =  config_commands(ch,commands)

   pattern_matching(interface)





