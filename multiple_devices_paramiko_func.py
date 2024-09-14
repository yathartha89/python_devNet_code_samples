import paramiko
import time
from cred import iosxe as device

hosts = [{"host": "R1", "IP": "10.10.20.47"}, {"host": "R2", "IP": "10.10.20.35"}]

def checking_connection(host,max_retries):
   retries = 1

   while retries < max_retries:
      try:
 
         client = paramiko.SSHClient()
   
         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
         client.connect(hostname=host,password=device["password"],username=device["username"],timeout=5)
      
      

         return client
         break  
    
      except Exception as e:
         print("The connection is not successful and the error is: ", e)
         retries += 1
def config_commands(session):
   
   commands = ["config t", "interface loopback1", "ip address 1.1.1.1 255.0.0.0"]
   
   for command in commands:
      session.send(command + "\n")
      time.sleep(5)
      output = session.recv(1024).decode()
      print(output)
   session.close()



for hostname in hosts:
   conn = checking_connection(hostname["IP"],3)
   if conn:
      print(f"The connection to {hostname['host']} is successful")
      ssh = conn.invoke_shell()
      config_commands(ssh)
      
   
   
      
