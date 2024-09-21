from netmiko import ConnectHandler

from cred import iosxe1 as device

hosts = {"hostname": "R1", "ip": "10.10.20.48"}

def checking_connection(num_tries,max_retries):
   while num_tries < max_retries:
      try:
         ch = ConnectHandler(
   
                 ip=hosts["ip"],
                 username=device["username"],
                 password=device["password"],
                 port=device["port"],
                 device_type=device["type"]
                
       
)

         print(f"The connection to {hosts['hostname']} is established successfully")
         return ch
        

      except Exception as e:
         num_tries = num_tries + 1
         print("The connection is failed and the error is: ", e)
        


def command(commands,ch):
 
   output = ch.send_config_set(commands)
   print(output)



ch = checking_connection(1,3)

if ch:
   commands = ["interface l1", "ip address 1.1.1.1 255.0.0.0", "description interface created using netmiko automation"]

   command(commands,ch)



   ch.disconnect()


   
