from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    #Definindo um nome para o Dag
    dag_id= 'Projeto_AirFlow_clima',
    #Definindo uma data de inicio para o Deg
    start_date=days_ago(2),
    #Definindo periodo de execucao (Nesse dag o periodo de execucao e 00h)
    schedule_interval= '@daily'
)as dag:

    tarefa1 = EmptyOperator(task_id='Tarefa_1')
    tarefa2 = EmptyOperator(task_id='Tarefa_2')
    tarefa3 = EmptyOperator(task_id='Tarefa_3')
    tarefa4 = BashOperator(
        task_id = 'Tarefa_4',
        bash_command = "mkdir -p '/home/enricolm/Documents/airflowalura/PastaExemplo1/{{data_interval_start}}'"
    )
    tarefa5 = BashOperator(
        task_id = 'Tarefa_5',
        bash_command = "mkdir -p '/home/enricolm/Documents/airflowalura/PastaExemplo1/{{data_interval_end}}'"
    )




tarefa1 >> [tarefa2, tarefa3]
tarefa3 >> [tarefa4, tarefa5]