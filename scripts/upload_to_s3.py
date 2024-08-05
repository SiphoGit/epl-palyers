# Create a new file named 'upload_to_s3.py' inside 'epl_players_scraper' lambda
# Copy and paste this code in 'upload_to_s3.py' 
import boto3
import json

s3_client = boto3.client('s3')

def upload_data(players: list) -> str:
    bucket_name = '' # Enter the first bucket name inside ''
    
    # Upload each player to S3
    for player in players:
        name = player['name']['display']
        json_data = json.dumps(player)
        s3_client.put_object(
            Bucket=bucket_name,
            Key=f'{name}.json',
            Body=json_data
        )