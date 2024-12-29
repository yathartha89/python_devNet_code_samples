from netmiko import ConnectHandler

from cred import iosxe1 as devices

import threading

def connection(device):
   try:

      conn = ConnectHandler(**device)

      print("********** The SSH connection is EST successfully **********\n")
      print("\n")
      return conn

   except Exception as e:

      print("The SSH connection is failed and the error is: ",e)

def command(conn):

   int_details = conn.send_command("show ip int brief")

   print(int_details)
   print("\n")

   conn.disconnect()

threads = []

for device in devices:

   conn = connection(device)

   if conn:

      thread = threading.Thread(target=command,args=(conn,))

      threads.append(thread)

      thread.start()


for thread in threads:

   thread.join()

print("********** The automation is completed **********\n")
      

