from netmiko import ConnectHandler
from cred import iosxe1 as device

ch = ConnectHandler(
      ip=device["ip"],
      port=device["port"],
      username=device["username"],
      password=device["password"],
      device_type=device["device_type"]


)

for num in range(1,101):

   loopback = ["no interface loopback" + str(num)]
   output = ch.send_config_set(loopback)
   print(output)

ch.disconnect()

   








 
