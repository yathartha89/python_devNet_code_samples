from ncclient import manager

from cred import xe as device

from xml.dom.minidom import parseString

netconf_conn = manager.connect(**device)

running_config = netconf_conn.get_config(source="running")

pretty_output = parseString(running_config.xml).toprettyxml()

print(pretty_output)






