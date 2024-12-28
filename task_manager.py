import os

import subprocess

import click

import json

def load_tasks():

   if os.path.exists("task.json"):

      file = open("task.json", "r")

      return json.load(file)

   else:

     print("Creating a new file")

     file = open("task.json", "w")

     return []

def save_tasks(task):

   file = open("task.json", "w")

   json.dump(task,file)
   

@click.group()

def task_manager():

   pass

@task_manager.command()
@click.argument('task')

def add(task):

   tasks = load_tasks()

   tasks.append(task)

   save_tasks(tasks)

@task_manager.command()

def list():

   list_tasks = load_tasks()

   if list_tasks:

      for id, n in enumerate(list_tasks,1):

         click.echo(f"{id} : {n}")

   else:

      click.echo("No tasks found")



      

@task_manager.command()
@click.argument('task_id')

def delete(task_id):

   id = load_tasks()

   del_id = id.pop(int(task_id) - 1)

   click.echo(f"The {del_id} is deleted")

   click.echo("Saving the updated tasks")

   save_tasks(id) 

   
task_manager()         
