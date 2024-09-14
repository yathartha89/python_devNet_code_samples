import paramiko
import time

from getpass import getpass

host = "10.10.20.47"

username = "developer"

password = getpass("Enter the password")

session = paramiko.SSHClient()

session.set_missing_host_key_policy(paramiko.AutoAddPolicy())


session.connect(
       hostname=host,
       username=username,
       password=password,
       timeout=10
       

        )

if session.get_transport() is not None and session.get_transport().is_active():
   print("The connection has been established successfullly")
   shell = session.invoke_shell()
   commands = ["config t", "no interface loopback90"]
   for command in commands:
   

      shell.send(command + '\n')
      time.sleep(1)

      print(shell.recv(1024).decode())
else:
   print("session is not active")

session.close()
