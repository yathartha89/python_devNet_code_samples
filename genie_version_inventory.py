from genie.testbed import load

testbed = load("cred.yml")

iosxe = testbed.devices['router1']
nxos = testbed.devices['router2']

devices_info = [{'Hostname': 'router1', 'ip': iosxe}, {'Hostname': 'router2', 'ip': nxos}]

def connection(device):
   try:

      device.connect(log_stdout=False)

      return device

   except Exception as e:

      print("The SSH connection cannot be EST and the error is: ",e)


def parsed_output_version(device):
 
   return device.parse("show version")

def parsed_output_inventory(device):

   return device.parse("show inventory")
  

 
for dev in devices_info:
   try:

      device = connection(dev['ip'])
   
      print()
   
      print(f"**********The SSH connection to {dev['Hostname']} has been EST successfully**********\n")

      Version = parsed_output_version(device)

      Inventory = parsed_output_inventory(device)

      if 'version' in Version:

         ver = Version['version']

         inv = Inventory['main']['chassis']['C8000V']

         print(f"**********Creating a file for {dev['Hostname']}  device info**********\n")

         with open(f"{dev['Hostname']}.txt", "w") as file:
            file.write('\n')
            file.write(f'Hostname: {ver["hostname"]}\n')
            file.write('---------\n')
            file.write(f'Version: {ver["version"]}\n')
            file.write('---------\n')
            file.write(f'Uptime: {ver["uptime"]}\n')
            file.write('---------\n')
            file.write(f'Serial_num: {ver["chassis_sn"]}\n')
            file.write('---------\n')
            file.write(f'Model: {inv["descr"]}\n')
            file.write('---------\n')
            print("********** The file creation is successfull **********\n")
      
      elif 'platform' in Version:

         ver = Version['platform']
     
         inv = Inventory['name']

         print(f"**********Creating a file for {dev['Hostname']} device info**********\n")

         with open(f"{dev['Hostname']}.txt", "w") as file:

            file.write('\n')
            file.write(f'Hostname: {ver["hardware"]["device_name"]}\n')
            file.write('----------\n')
            file.write(f'Version: {ver["software"]["system_version"]}\n')
            file.write('----------\n')
            file.write(f'Uptime: {ver["kernel_uptime"]["hours"]}hrs_{ver["kernel_uptime"]["days"]}days_{ver["kernel_uptime"]["minutes"]}min\n')
            file.write('----------\n')
            file.write(f'Serial_num: {inv["Chassis"]["serial_number"]}\n')
            file.write('----------\n')
            file.write(f'Model: {inv["Chassis"]["pid"]}\n')
            file.write('----------\n')            
            print("********** The file creation has been done successfull **********\n")
   except Exception as e:

      print("The request could not be completed and the error is: ",e)


print("********** The info of all the  devices has been gathered successfully**********")
