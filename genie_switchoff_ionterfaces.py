
from genie.testbed import load

from genie.utils.diff import Diff

testbed = load("testbed.yml")

routers = ["router1"]

def connect():

   try:

      device = testbed.devices[router]
  
      device.connect(log_stdout=False)

      print(f"The remote SSH connection is EST with {router}************************\n")
    
      return device  

   except Exception as e:

      print("The remote SSH connection is failed and the error is: ",e)


def parsed_output(device):

   return device.parse("show ip int brief")

   

def interface_eva(final_output,device):

   interfaces = final_output["interface"]

   for interface, details in interfaces.items():

      if interface == "GigabitEthernet1":

         continue

      if details["ip_address"] == "unassigned" or details["protocol"] == "down":

         device.configure([f'interface {interface}', 'shutdown'])

         print(f"The interface {interface} is turned to admin down")
  
      else:

         print(f"The interface {interface} is up")


   






for router in routers:

   device = connect()

   if device:

     final_output =  parsed_output(device)
  
     

     interface_eva(final_output,device)

   



   
