import paramiko
import time

from cred import iosxe as device

l = {"R1": "10.10.20.48", "R2": "10.10.20.35"}

for host in l:
   try:
      client = paramiko.SSHClient()
      client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      client.connect(hostname=l[host],username=device["username"],password=device["password"],timeout=5)

   except Exception as e:
      print(f"The connection to {host} is failed and the error is: ", e)
   
   if client.get_transport() is not None and client.get_transport().is_active():
      print(f"The connection to {host} is successful")
      session = client.invoke_shell()
      commands = ["ter len 0", "show run"]
      for command in commands:
         session.send(command + "\n")
         time.sleep(10)
         output = session.recv(1024).decode()
         f = open(f"{host}.txt",'w')
         f.write(output)
         time.sleep(5)
         f.close()
         
         

      client.close()
      
