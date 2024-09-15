from telnetlib import Telnet

import time

from cred import iosxe as device



tn = Telnet(host=device["hostname"])

tn.read_until(b"Username: ")

tn.write(device["username"].encode() + b"\n")

print("Username sent")

tn.read_until(b"Password: ")

tn.write(device["password"].encode() + b"\n")

print("Password sent")

print("Connection established successfully")

time.sleep(5)

tn.write(b"config t" + b"\n")

tn.write(b"interface loopback10" + b"\n")

time.sleep(5)

tn.write(b"ip address 2.2.2.2 255.0.0.0" + b"\n")

time.sleep(5)

tn.write(b"end" + b"\n")


response = tn.read_until(b"config-if")

print(response.decode('ascii'))

response1 = tn.read_until(b"cat8000v")

print(response1.decode('ascii'))







