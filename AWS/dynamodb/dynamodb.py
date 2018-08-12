import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print (bucket.name)

client = boto3.client('dynamodb')

#response = client.get_item(TableName='miketable',Key={'int':{'S':'string','S':'string'}}


response = client.list_tables()
print (response)

ec2 = boto3.client('ec2')

response = (ec2.describe_subnets())
print (response)

for i in response.items():
    print (i[0])