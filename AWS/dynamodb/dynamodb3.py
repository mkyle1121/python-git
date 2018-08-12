import boto3
import uuid

client = boto3.resource('dynamodb')
table = client.Table('users')

item = {'id':uuid.uuid4().hex, 'color': 'red', 'size': 'large'}

table.put_item(Item=item)