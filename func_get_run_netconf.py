from ncclient import manager

from cred import xe as device

from xml.dom.minidom import parseString

import time

def netconf_connect():
   try:

      netconf_conn = manager.connect(**device,timeout=10)
     
      print("The SSH netconf connection is successfully established")

      return netconf_conn

   except Exception as e:
      print("The SSH netconf connection failed and the error is: ",e) 


def get_running_config(netconf_conn):

   running_config = netconf_conn.get_config(source = "running")

   return running_config


def convertXML_to_prettyXML(running_config):

   pretty_output = parseString(running_config.xml).toprettyxml()

   return pretty_output



netconf = netconf_connect()


if netconf:

   output = get_running_config(netconf)

   final_output = convertXML_to_prettyXML(output)


   print("The final output is:")
   print()

   time.sleep(2)

   print(final_output)


   

   

   
