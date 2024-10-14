from ncclient import manager

from cred import xe as device

from xml.dom.minidom import parseString

from xmltodict import parse 

import time

def net_conf_conn(num,max_num):
 while num < max_num:
   try:

      net_conf = manager.connect(**device)
   
      print("The net_conf connection has been EST successfully")
   
      return net_conf
   except Exception as e:
      print("The connection could not be EST and the error is: ",e)
      num+=1



interface_filter =  """
    
     <filter xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
           <interface>



           </interface>
        </interfaces>
     </filter>

   

"""

def get_run_interface(net_conf):


   output = net_conf.get_config(filter=interface_filter,source="running")

   return output


def pretty_output(output):

   return  parseString(output.xml).toprettyxml()

def xmltodict(out):

   return parse(out)

   

         

num = 3
max_num = 4
conn = net_conf_conn(num,max_num)

time.sleep(5)

print()

if conn:

   out = get_run_interface(conn)

   final_output = pretty_output(out)
  
   interfaces_dict =  xmltodict(final_output)
    
   interfaces = interfaces_dict["rpc-reply"]["data"]["interfaces"]["interface"]
   
   file = open("interfaces.txt",'a')   

   for interface in interfaces:
      ipv4_info = interface.get('ipv4', {}).get('address', {})
      
      data = f"The name is {interface['name']}, state is {interface['enabled']}, IP is {ipv4_info.get('ip', 'none')}, netmask is {ipv4_info.get('netmask', 'none')}\n"
   

     

      file.write(data)

   file.close()
  
   print("The file hs been prepared with interface details")

      





   

   





 
