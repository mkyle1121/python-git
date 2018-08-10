import boto3

client = boto3.client('route53')

#response = client.list_resource_record_sets(HostedZoneId='Z1ESZTLUAN73VU')

#print(response['ResponseMetadata'])
#print('\n')
#print(response['ResourceRecordSets'])


response = client.change_resource_record_sets(HostedZoneId='Z1ESZTLUAN73VU',
ChangeBatch={'Changes':[{'Action':'CREATE','ResourceRecordSet':{'Name':'test.themikekyle.com.',
'Type':'A','TTL':300,'ResourceRecords':[{'Value': '1.1.1.1'}]}}]})

client.change_resource_record_sets(HostedZoneId='Z1ESZTLUAN73VU',
ChangeBatch={'Changes':[{'Action':'CREATE','ResourceRecordSet':{'Name':'ham.themikekyle.com.',
'Type':'A','TTL':300,'ResourceRecords':[{'Value': '1.1.1.2'}]}}]})

#'SetIdentifier':'?????',
#'Weight':100,
#'Region':'us-east-2',
