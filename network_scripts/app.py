from flask import Flask,request,render_template,jsonify

import subprocess

import os

import sys

app = Flask(__name__)

@app.route('/')

def index():

   return render_template('index.html')


@app.route('/run_script', methods=['POST'])

def script():

   script_name = request.form.get('script_name')
  
   script_path = os.path.join('scripts', script_name)

   if not os.path.isfile(script_path):

      return jsonify({'Status': 'ERROR', 'Output': f'Invalid or missing script at {script_path}'})

   else:

      
      try:  
   
         print(f"Attempting to run the script at {script_path}")

         result = subprocess.check_output(['ansible-playbook', script_path])

         output = result.decode('utf-8')

         return jsonify({'Status': 'Success', 'Output': output})
 
      except subprocess.CalledProcessError as e:

         return jsonify({'Status': 'ERROR', 'Output': 'e.output.decode("utf-8")'})

      except Exception as e:

         return jsonify({'Status': 'ERROR', 'Output': str(e)})

app.run(debug=True)      

      

