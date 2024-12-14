from getpass import getpass

from ncclient import manager

from xml.dom.minidom import parseString

from xmltodict import parse

from cred import netconf as device

username = getpass("Enter your username: ")

password = getpass("Enter your password: ")


filter_conf = """ 

      <filter xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">
         
         <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

            <interface>


            </interface>

         </interfaces>

      </filter>  
        
"""

interface_conf = """ 

           <config xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">
           
              <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

                 <interface>

                    <name>{name}</name>
 
                    <description>Interface put admin down by YV using netconf</description>

                    <enabled>false</enabled>

                    <type xmlns:ianaift = "urn:ietf:params:xml:ns:yang:iana-if-type">

                       ianaift:{type}

                    </type>

                 </interface>

              </interfaces>

           </config>
"""

def net_conn():
   try:

      conn = manager.connect(**device)
  
      print("The netconf connection is EST successfully")

      return conn

   except Exception as e:

      print("The netconf connection is failed and the error is: ",e)



def get_int_conf(conn):

   return conn.get_config(filter=filter_conf,source="running")

def xml_to_pretty_xml(int_conf):

   return parseString(int_conf.xml).toprettyxml()

def xml_to_dict(pretty_xml):

   return parse(pretty_xml)

def shutdown_phy_int(conn,interface_name):

   physical_int = interface_conf.format(name=interface_name,type='ethernetCsmacd')

   int_shut = conn.edit_config(physical_int,target="running")

   print(f"The interface {interface_name} has been  shut down successfully")
   
def shutdown_loopback_int(conn,interface_name):

   loopback_int = interface_conf.format(name=interface_name,type='softwareLoopback')

   loopback_shut = conn.edit_config(loopback_int,target='running')

   print(f"The loopback interface {interface_name} has been shut down successfully")





if username == 'test' and password == 'cisco':

   conn = net_conn()

   if conn:

      int_conf = get_int_conf(conn)

      pretty_xml = xml_to_pretty_xml(int_conf)

      interface = xml_to_dict(pretty_xml)

      interface_info = interface['rpc-reply']['data']['interfaces']['interface']
   
      for interface in interface_info:
 

         ip = interface.get('ipv4', {}).get('address', {}).get('ip', 'none')

         if interface['type']['#text'] == 'ianaift:ethernetCsmacd':

            if ip == 'none' and interface['enabled'] == 'true':

               shutdown_phy_int(conn,interface['name'])

         elif interface['type']['#text'] == 'ianaift:softwareLoopback':

            if ip == 'none' and interface['enabled'] == 'true':

               shutdown_loopback_int(conn,interface['name'])

                
else:

   print("The credentials are wrong ,please try again")
                   

         

   

   

   
