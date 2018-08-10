import boto3

client = boto3.client('route53')

response = client.change_resource_record_sets(HostedZoneId='Z1ESZTLUAN73VU',
ChangeBatch={'Changes':[{'Action':'DELETE','ResourceRecordSet':{'Name':'test.themikekyle.com.',
'Type':'A','TTL':300,'ResourceRecords':[{'Value': '1.1.1.1'}]}}]})

print(response)