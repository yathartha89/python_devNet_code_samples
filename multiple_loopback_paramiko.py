import paramiko
import time

from cred import iosxe as device


try:
 
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

   ssh.connect(
      username=device["username"],
      password=device["password"],
      hostname=device["host"],
      timeout=10



)

except Exception as e:
   print(f"Connection failed: {e}")


if ssh.get_transport() is not None and ssh.get_transport().is_active():

   print("********The connection has been established successfully********")

   client = ssh.invoke_shell()
   client.send("config t" + "\n")
   time.sleep(.5)
   for interface in range(80,91):
      
      time.sleep(.5)
      client.send("no interface loopback" + str(interface) + "\n")
      time.sleep(.5)
      output = client.recv(1024).decode()
      print(output)


ssh.close()



