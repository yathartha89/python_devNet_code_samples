from genie.testbed import load



testbed = load("testbed.yml")


expect = {

         "interface": {

             "GigabitEthernet1": {

                   "status": "up",

                   "protocol": "up"
},
             "GigabitEthernet2": {

                    "status": "up",

                    "protocol": "up"



}
}
}


def connect():
   try:

      device = testbed.devices["router1"]

      device.connect(log_stdout=False)

      print("The remote SSH connection has been EST successfully")

      return device

   except Exception as e:

      print("The connection failed and the error is: ",e)


def final_output(device):

   return device.parse("show ip int brief")

   
def eva_output(parsed_output):

   interfaces = parsed_output["interface"]

   expected_output = expect["interface"]

   for interface, details in expected_output.items():

      if interface in interfaces:

         parsed_details = interfaces[interface]

         if (parsed_details["status"] == details["status"] and parsed_details["protocol"] == details["protocol"]):

            print(f"The interface {interface} is compliant")

         else:

            print(f"The interface {interface} is not compliant and the details are as below")

            print(f"Expected state is: {details['status']} and {details['protocol']}\n")

            print(f"Actual state is: {parsed_details['status']} and {parsed_details['protocol']} ")

      else:

        print("The interface could not be found")



device = connect()

if device:

   parsed_output = final_output(device)

   eva_output(parsed_output)



