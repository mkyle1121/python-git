import boto3
import uuid

client = boto3.client('dynamodb')

item = {'id':uuid.uuid4().hex, 'color': 'red', 'size': 'large'}

client.put_item(TableName='miketable', Item={'string' : {'id':7, 'S' : 'string'}})