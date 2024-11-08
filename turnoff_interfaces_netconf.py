from ncclient import manager

from cred import xe as device

from xml.dom.minidom import parseString

from xmltodict import parse

import time

def netconf_conn(num,max_num):

   while num < max_num:

      try:

         conn = manager.connect(**device)

         print("The netconf connection has been EST successfully")

         return conn

      except Exception as e:

         print("The netconf connection has not been EST successfully and the error is: ",e)
        
         num = num + 1

def get_interface_config(commands,conn):

   return conn.get_config(filter=commands,source='running')
 

def xml_to_pretty_xml(interface_xml):

   return parseString(interface_xml.xml).toprettyxml()


def conversion_to_dict(dict):

   return parse(dict)


interface_config = """ 

        <config xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">

           <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

              <interface>

                 <name>{int_name}</name>
  
                 <enabled>false</enabled>

                 <type xmlns:ianaift = "urn:ietf:params:xml:ns:yang:iana-if-type">

                    ianaift:ethernetCsmacd

                 </type>

              </interface>

           </interfaces>

        </config>

"""

loopback_config = """ 
 
       <config xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">

          <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

             <interface>

                <name>{int_name}</name>

                <enabled>false</enabled>

                <type xmlns:ianaift = "urn:ietf:params:xml:ns:yang:iana-if-type">

                   ianaift:softwareLoopback
                </type>

             </interface>

          </interfaces>

       </config> 
"""

def disable_interface(conn):

   int_disable = interface_config.format(int_name=interface['name'])

   ouptut = conn.edit_config(int_disable,target='running')
  
   print(f"The interface {interface['name']} has been disabled")
   
def disable_loopback_interface(conn):

   loopback_disable = loopback_config.format(int_name=interface['name'])

   output = conn.edit_config(loopback_disable,target='running')
   
   print(f"The interface {interface['name']} has been disabled")

while True:

   conn = netconf_conn(2,3)

   commands = """ 

      <filter xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">

         <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

            <interface>


            </interface>

         </interfaces>


      </filter>

"""



   if conn:

      interface_xml =  get_interface_config(commands,conn)

      dict = xml_to_pretty_xml(interface_xml)
   
      final_output = conversion_to_dict(dict)
      
     
      int_output = final_output['rpc-reply']['data']['interfaces']['interface']

      for interface in int_output:

         ipv4_info = interface.get('ipv4', {}).get('address', {})

         ip = ipv4_info.get('ip', 'none')

         int = interface['enabled']

         if int == 'true' and ip == 'none' and interface['type']['#text'] == 'ianaift:ethernetCsmacd':

            disable_interface(conn)
        
         elif int == 'true' and ip == 'none' and interface['type']['#text'] == 'ianaift:softwareLoopback':

            disable_loopback_interface(conn)
   
         time.sleep(2)   
           

        

   
   

   
   
