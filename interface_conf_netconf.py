from ncclient import manager

from cred import xe as device

from getpass import getpass



def net_conf_conn(num,max_num):
   while num < max_num:
      try:

         net_conf = manager.connect(**device)
         print("The netconf connection has been established successfully")
         return net_conf
         
      except Exception as e:
         print("The connection could not be established and the error is: ",e)
         num+=1

template = """
     <config xmlns = "urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
           <interface>
              <name>{int_name}</name>
              <description>The interface created by YV using netconf</description>
              <type xmlns:ianaift = "urn:ietf:params:xml:ns:yang:iana-if-type">
                 ianaift:{type}
              </type>
              <enabled>true</enabled>
              <ipv4 xmlns = "urn:ietf:params:xml:ns:yang:ietf-ip">
                 <address>
                    <ip>{ip_address}</ip>
                    <netmask>{ip_mask}</netmask>
               
                 </address>
              </ipv4>
           </interface>
        </interfaces>
     </config>


              
"""


def config_interface(net_conf):

   print("welcome to the interface configuration, please input the parameters")
  
   interface_name = input("Please enter the interface name: ")

   int_type = "ethernetCsmacd"

   int_address = input("Please enter the address: ")

   int_mask = input("Please enter the ip mask: ")

   interface_config = template.format(int_name=interface_name,type=int_type,ip_address=int_address,ip_mask=int_mask)

   output = net_conf.edit_config(interface_config,target="running")

   print(output)


def loopback_config(net_conf):

   print("Welcome to the loopback interface config,please enter the parametres")
   
   interface_name = input("Please enter the interface name: ")

   int_type = "softwareLoopback"

   int_address = input("Please enter the interface address: ")

   int_mask = input("Please enter the subnet mask: ")

   loopback_config = template.format(int_name=interface_name,type=int_type,ip_address=int_address,ip_mask=int_mask)

   output = net_conf.edit_config(loopback_config,target="running")

   print(output)



username = getpass("Please enter the username: ")

password = getpass("Please enter the password: ")

num = 1
max_num = 3

if username == "admin" and password == "cisco":

   conn = net_conf_conn(num,max_num)

   if conn:

      print("Welcome to the net_conf utility , please enter your choice as 1/2\n1. Physical interface\n2. Loopback interface")


      user_choice = input("Please enter your choice: ")

      if user_choice == "1":
   
         config_interface(conn)


      elif user_choice == "2":
      
         loopback_config(conn)

      else:

         print("Please enter the correct choice")

else:

   print("Please enter the correct credentials")
   


   



   

   

   



