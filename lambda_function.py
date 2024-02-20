import boto3
import json
from datetime import datetime

def send_email_notification(sns_client, sns_topic_arn, glue_job_name):
    timestamp = datetime.utcnow().strftime("%d %b %Y at %H:%M hrs")

    message = f"A Glue job named '{glue_job_name}' was triggered on the arrival of new sales data in your data lake at {timestamp}"

    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject=f"Glue Job Triggered: {glue_job_name}"
    )

def lambda_handler(event, context):
    glue_client = boto3.client('glue')
    sns_client = boto3.client('sns')

    glue_job_name = 'Sales_Glue_Job'
    sns_topic_arn = 'arn:aws:sns:us-east-1:278557494232:GlueJobNotification'

    try:
        response = glue_client.start_job_run(JobName=glue_job_name)
        run_id = response['JobRunId']

        print(f"Glue job {glue_job_name} started successfully. Run ID: {run_id}")

        send_email_notification(sns_client, sns_topic_arn, glue_job_name)

    except Exception as e:
        print(f"Error starting Glue job {glue_job_name}: {e}")
