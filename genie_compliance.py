from genie.testbed import load

expected_output = { 

         "interface": {

                "GigabitEthernet1": {

                          "status": "up",

                          "protocol": "up",

                          "ip": "10.10.20.48"
 

},

                "GigabitEthernet2": {

                          "status": "up",

                          "protocol": "up",

                          "ip": "10.10.20.40"

}
}
}

def connect():
   try:

      testbed = load("testbed.yml")

      device = testbed.devices["router1"]

      device.connect(log_stdout=False)

      print("The SSH connection to the device has been EST successfully\n")

      return device

   except Exception as e:

      print("The SSH connection to the device is failed and the error is: ",e)

def parsed_output(device):

   return  device.parse("show ip int brief")


conn = connect()

if conn:

   actual_output = parsed_output(conn)
   
   interfaces = actual_output["interface"]

   expect = expected_output["interface"]

   for inter,details in expect.items():

      if inter in interfaces:

         if details["status"] == interfaces[inter]["status"] and details["protocol"] == interfaces[inter]["protocol"] and details["ip"] == interfaces[inter]["ip_address"]:

            print(f"The interface info of {inter} is compliant with the actual status of the interface\n")

         else:

            print(f"The interface info of {inter} is not compliant with the actual status of the interface and the details are as below:\n")

            print(f"The expected output is: {details['status']} , {details['protocol']} and {details['ip']}\n")       

            print(f"The actual output is: {interfaces[inter]['status']} , {interfaces[inter]['protocol']} and {interfaces[inter]['ip_address']}")

   
