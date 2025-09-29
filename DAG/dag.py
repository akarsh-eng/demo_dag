from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def sample_task():
	print("Hello from Astronomer & Airflow!")

default_args = {
	'owner': 'airflow',
	'start_date': datetime(2023, 1, 1),
	'retries': 1,
}

with DAG(
	dag_id='sample_astronomer_dag',
	default_args=default_args,
	schedule_interval='@daily',
	catchup=False,
) as dag:
	hello_task = PythonOperator(
		task_id='hello_task',
		python_callable=sample_task
	)

	hello_task
