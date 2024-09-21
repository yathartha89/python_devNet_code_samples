from netmiko import ConnectHandler

from cred import iosxe1 as device
import logging

logging.basicConfig(filename='netmiko.txt',level=logging.DEBUG)

hosts = [{"hostname": "R1", "ip": "10.10.20.48"}, {"hostname": "R2", "ip": "10.10.20.35", "device_type": "cisco_xr"}]
number_of_tries = 1
max_retries = 3

for host in hosts:

   while number_of_tries < max_retries:
      try:
         ch = ConnectHandler(
                 ip=host["ip"],
                 username=device["username"],
                 password=device["password"],
                 port=device["port"],
                 device_type=device["type"],
                 global_delay_factor=5
                 
  
)
         
         print(f"The connection to {host['hostname']} is established successfully")
         ch.set_base_prompt()
         commands = ["interface l1", "ip address 1.1.1.1 255.0.0.0", "description loopback created using netmiko automation"]
         
         output = ch.send_config_set(commands)
    
         print(output)

         break

   
      except Exception as e:
         print("The connection is not successful and the error is: ", e)
         number_of_tries+=1
         
 
         


