import click

from netmiko import ConnectHandler

import subprocess

def connection(ip,username,password,device_type):
   
   return  ConnectHandler(ip=ip,username=username,password=password,device_type=device_type)


@click.group()
def device_tools():
   pass
@device_tools.group()
def device():
   pass

@device.command()
@click.option('--ip',prompt='device_ip',help='IP address of the device')

def ping(ip):

   try:
  
     click.echo(f"Trying to ping the ip {ip}\n")

     subprocess.run(['ping', '-c', '2', ip],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)


     click.echo("\n")

     click.echo(f"The ping to the {ip} is successful")

   except subprocess.CalledProcessError as e:

      click.echo(f"The ping to the device is failed and the error is {e}")

@device.command()
@click.option('--ip',prompt='device_ip',help='The IP address of the device')
@click.option('--username',prompt='username',help='Username of the device')
@click.option('--password',prompt='password',hide_input=True,help='Password of the device')
@click.option('--device_type',prompt='device_type',default='cisco_ios',show_default=True,help='The device_type of the device')

def show_version(ip,username,password,device_type):
   try:

      conn = connection(ip,username,password,device_type)

      click.echo(f"The SSH connection to the {ip} is EST successfully")

      ver = conn.send_command("show version")
      
      click.echo("********The info of the device********\n")
          
      click.echo(ver)

   except Exception as e:

      click.echo("The SSH connection is failed and the error is: ",e)

@device.command()
@click.option('--ip',prompt='device_ip',help='The IP address of the device')
@click.option('--username',prompt='username',help='username of the device')
@click.option('--password',prompt='password',hide_input=True,help='Password of the device')
@click.option('--device_type',prompt='device_type',default='cisco_ios',show_default=True)
def show_run(ip,username,password,device_type):

   try:

      conn = connection(ip,username,password,device_type)

      click.echo("The SSH connection to ip has been EST")

      run = conn.send_command("show run")

      click.echo("**********The running configuration of the device***********\n")

      click.echo(run)

   except Exception as e:

      click.echo(f"The SSH connection to {ip} is failed and the error is: ",e)

device_tools()
