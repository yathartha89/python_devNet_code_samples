from netmiko import ConnectHandler

from getpass  import getpass

from cred import iosxe1 as devices

def connection(device):
   try:

      conn = ConnectHandler(**device)

      print("The SSH connection is EST successfully")

      return conn

   except Exception as e:

      print("The SSH connection is failed and the error is: ",e)


def show(conn):

   return  conn.send_command("show ip int brief")

def parsed_output(conn):

   return conn.send_command("show ip int brief",use_textfsm=True) 





for device in devices:

   conn = connection(device)

   if conn:

      try:

         interface_details = show(conn)

         print("\n")

         parsed_interface_details = parsed_output(conn)
  
         print("***** The file is been created *****")
   
         for int_details in parsed_interface_details:

            interface_name = int_details["interface"]

            interface_ip = int_details["ip_address"]

            interface_status = int_details["status"]

            interface_proto = int_details["proto"]

            with open(f"{device['ip']}.txt", "a") as file:
 
               file.write("\n")
               file.write(f"Name: {interface_name}\n")
               file.write("\n")
               file.write(f"IP: {interface_ip}\n")
               file.write("\n")
               file.write(f"Status: {interface_status}\n")
               file.write("\n")
               file.write("**********\n")
               file.write("\n")
      except Exception as e:

         print("There is some error while executing the commands and the error is: ",e)
print("The automation has been finished")
  

   


