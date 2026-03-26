from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'email': ['mshr3ya@gmail.com'],  
    'email_on_failure': True,
    'email_on_retry': True
}

with DAG(
    dag_id='infosys_etl_pipeline',
    default_args=default_args,
    schedule='*/2 * * * *',
    catchup=False
) as dag:

    create_tables = BashOperator(
        task_id='create_tables',
        bash_command='python3 ~/airflow/scripts/create_tables.py'
    )

    load_data = BashOperator(
        task_id='load_data',
        bash_command='python3 ~/airflow/scripts/load_data.py'
    )

    transform_data = BashOperator(
        task_id='transform_data',
        bash_command='python3 ~/airflow/scripts/transform_data.py'
    )

    check_data = BashOperator(
        task_id='check_data',
        bash_command='python3 ~/airflow/scripts/check_data.py'
    )

    create_tables >> load_data >> transform_data >> check_data
