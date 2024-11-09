import subprocess

import sys

import os

git_url = input("Please enter the git url: ")

repo_name = git_url.split('/')[-1].replace('.git','')

script_name = input("Please enter the script name: ")

org_dir = os.getcwd()



file_path = os.path.join(repo_name,script_name)

def checking_repo(git_url,branch='main'):

   if not os.path.isdir(repo_name):

      print("The repo does not exist , cloning the repo now")

      subprocess.run(['git', 'clone', git_url])


   else:

      print("The repo already exists,pulling out the latest changes")

      os.chdir(repo_name)

      subprocess.run(['git', 'checkout', branch],check=True)

      subprocess.run(['git', 'pull'],check=True)
      
      os.chdir(org_dir)

def executing_script(file_path):

   if not os.path.isfile(file_path):

      print("Error: File does not exist")

   else:

      if '.yml' in file_path:

         subprocess.run(['ansible-playbook', file_path],check=True)

      else:

         subprocess.run(['python3', file_path],check=True)



checking_repo(git_url)

executing_script(file_path)


   
   

   
