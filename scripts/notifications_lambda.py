# Copy and paste this code in 'lambda_functions.py' inside 'epl-scraper-notifications' lambda

import boto3
import json

sns_arn = '' # Copy and paste the Amazon SNS topic ARN inside the ''

def lambda_handler(event, context):
    client = boto3.client('sns')
    
    client.publish(
        TargetArn=sns_arn, 
        Message=json.dumps(event),
        Subject=f'EPL Players Scraper Lambda Function Failed'
        )
    
    return {
    'statusCode': 200,
    'body': json.dumps('Scraping EPL players completed!')
    }