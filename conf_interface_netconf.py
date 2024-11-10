from ncclient import manager

from cred import xe as device

netconf_connect = manager.connect(**device)

print("The SSH netconf connection is established successfully")

interface_config = """ 
 <config xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">  
   <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
         <name>GigabitEthernet2</name>
         <description>Interface concigured by YV using netconf</description>
         <type xmlns:ianaift = "urn:ietf:params:xml:ns:yang:iana-if-type">
            ianaift:ethernetCsmacd
         </type>
         <enabled>true</enabled>
         <ipv4 xmlns = "urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
               <ip>1.1.1.1</ip>
               <netmask>255.0.0.0</netmask>
            </address>
         </ipv4>
      </interface>
   </interfaces>
 </config>

"""


interface_config = netconf_connect.edit_config(interface_config, target = "running")


print(interface_config)




