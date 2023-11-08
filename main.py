from datetime import datetime, timedelta
from src.email_report import send_report, send_sms
import boto3
from botocore.exceptions import ClientError
import os

BUCKET_NAME= os.environ["BUCKET_NAME"]
REGION = os.environ['REGION']

today_date = datetime.now().strftime('%d-%m-%Y')
tomorrow_date = today_date + timedelta(days=1)
tomorrow_date_str = tomorrow_date.strftime('%d-%m-%Y')

s3_client = boto3.client("s3", region_name=REGION)

def main(event, context):

    object_key = f'Hana Call Summary Report/Hana Call Summary Full Report {today_date}.zip'

    object_key_2 = f'Hana SMS Blast/SMS_Blast_{tomorrow_date_str}.zip'

    try:
        # Download the file from S3
        s3_response_report = s3_client.get_object(Bucket=BUCKET_NAME, Key=object_key)
        file_content = s3_response_report['Body'].read()

        send_report(file_content, today_date)

        print("Email for Hana Daily Summary Report has been sent")

    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            print("No report file")
        else:
            print("An error occurred:", e)
    
    try:
        # Download the file from S3
        s3_response_sms = s3_client.get_object(Bucket=BUCKET_NAME, Key=object_key_2)
        file_content = s3_response_sms['Body'].read()
        
        send_sms(file_content, today_date, tomorrow_date_str)

        print("Email for SMS Blast has been sent")

    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            print("No SMS blast")
        else:
            print("An error occurred:", e)
    