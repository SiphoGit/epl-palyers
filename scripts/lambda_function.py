# Copy and paste this code in 'lambda_functions.py' inside 'epl_players_scraper' lambda

import requests
import json

from upload_to_s3 import upload_data
from utils import (
    url, 
    headers, 
    payload
)

def lambda_handler(event, context):
    response = requests.get(url, headers=headers, data=payload)
    data = response.json()
    players = data['content']
   
    # Upload data to S3 bucket
    upload_data(players)
    
    return {
    'statusCode': 200,
    'body': json.dumps('Scraping EPL players completed!')
    }