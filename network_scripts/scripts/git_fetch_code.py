
import subprocess

import os

git_url = input("Please enter the git url: ")

script_name = input("Please enter the script name: ")

git_repo = git_url.split('/')[-1].replace('.git','')

org_dir = os.getcwd()

def checking_for_git_repo(branch):

   

   print("The git repo already exists , pulling the latest changes from git")

   os.chdir(git_repo)

   subprocess.run(['git', 'checkout', branch ],check=True)

   subprocess.run(['git', 'pull'])

   os.chdir(org_dir)

def cloning_git_repo():

   print("The git repo does not exist , cloning the git repo")

   subprocess.run(['git', 'clone', git_url])


def running_script():

   script_path = os.path.join(git_repo,script_name)

   subprocess.run(['python3', script_path])

def running_script_ansible():

   script_path = os.path.join(git_repo,script_name)

   subprocess.run(['ansible-playbook', script_path])

if  os.path.isdir(git_repo):

   checking_for_git_repo('main')

   if '.yml' in script_name:

      running_script_ansible()

   else:

      running_script()

   

else:

   cloning_git_repo()

   if '.yml' in script_name:

      running_script_ansible()

   else:

      running_script()







   
   




