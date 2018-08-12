import boto3
import uuid


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

title = "Robot DB"
year = 2018

response = table.put_item(
    Item={'id':str(uuid.uuid4().hex),
          'user':'joe',
          'pass':'pass123'
          }
)