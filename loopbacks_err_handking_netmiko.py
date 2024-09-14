from netmiko import ConnectHandler

from cred import iosxe1 as device

loopbacks = [{"interface": "l91", "IP": "1.1.1.1", "mask": "255.0.0.0"}, {"interface": "l92", "IP": "2.2.2.2", "mask": "255.0.0.0"}, {"interface": "l93", "IP": "3.3.3.3", "mask": "255.0.0.0"}]

def SSH_connection_checking():

   try:
      ch = ConnectHandler(
          ip=device["ip"],
          username=device["username"],
          password=device["password"],
          port=device["port"],
          device_type=device["device_type"]

   

)

      
      return ch
   except Exception as e:
      print(f"Connection failed with error: {e}")
      return False


def creating_loopbacks(ch):
   for loopback in loopbacks:
      config_commands = [f"interface {loopback['interface']}", f"ip address {loopback['IP']} {loopback['mask']}", "description Interface created using netmiko"]
      output = ch.send_config_set(config_commands)
      print(f"The output for {loopback['interface']} is:")
      print()
      print(output)
   


ch = SSH_connection_checking()
if ch:
   print("****The connection is formed successfully****")
   creating_loopbacks(ch)





