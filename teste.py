import os
import shutil
import pendulum
import subprocess
import pandas as pd
from time import sleep
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

data = datetime.today()
data = data + timedelta(days=1)
data = data.strftime('%Y-%m-%d')
def extraindo_dados(data):
    os.chdir('/home/enricolm/Desktop/Air')
    subprocess.call(['source','venv/bin/activate'],shell=True)
    sleep(1)
    subprocess.call(['python3', 'airflow.py'])
    sleep(3)
    shutil.move(f'/home/enricolm/Desktop/Air/Dados/{data}','/home/enricolm/Documents/airflowalura/PastaExemplo1/')
    


extraindo_dados(data)