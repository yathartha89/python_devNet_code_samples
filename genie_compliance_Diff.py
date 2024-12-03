from genie.testbed import load

from genie.utils.diff import Diff

testbed = load("testbed.yml")

expected_output = {

          "interface": {

               "GigabitEthernet2": {

                      "status": "up",

                      "protocol": "up"

},
               "GigabitEthernet3": {

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

      print("The remote connection could not be EST and the error is: ",e)


def parse_output(device):

   return device.parse("show ip int brief")


def eva_output(parsed_output):

   diff = Diff(expected_output["interface"],parsed_output)

   diff.findDiff()
   

   if not diff:

      print("All the interfaces are compliant")

   else:

      print("The interfaces are not compliant and the details are as below: \n")

      print(diff)




device = connect()

parse_out = parse_output(device)

eva_output(parse_out["interface"])





  
