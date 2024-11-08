
from ncclient import manager

from cred import xe as device

def net_conf_conn():

   try:

      conn = manager.connect(**device)

      print("The netconf connection has been EST successfully")

      return conn
     
   except Exception as e:
   
      print("The connection could not be established successfully and the error is: ",e)




commands =  """ 

         <config xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">

            <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

               <interface>
                             
                  <name>GigabitEthernet2</name>

                  <description>interface configured by YV using netconf</description>

                  <enabled>true</enabled>

                  <type xmlns:ianaift = "urn:ietf:params:xml:ns:yang:iana-if-type">

                     ianaift:ethernetCsmacd

                  </type>

                  <ipv4 xmlns = "urn:ietf:params:xml:ns:yang:ietf-ip">
                     
                     <address operation='delete'>

                        <ip>1.1.1.1</ip>
 
                        <netmask>255.0.0.0</netmask>

                     </address>

                  </ipv4>

             </interface>

           </interfaces>

       </config>

"""



def pushing_config(conn,commands):

   interface_config = conn.edit_config(commands,target="running")

   print(interface_config)

   
   
conn = net_conf_conn()

if conn:

   pushing_config(conn,commands)
   conn.close_session()
else:

   print("The connection has failed")



   


      


