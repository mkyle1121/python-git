import boto3

client = boto3.client('route53')

response = client.list_resource_record_sets(HostedZoneId='Z1ESZTLUAN73VU', StartRecordName='robot.themikekyle.com', StartRecordType='A')

print('\n')

for i in response['ResourceRecordSets']:
    print(i)

#print(response['ResourceRecordSets'])
#print(response['ResourceRecordSets'][0])
#print(response['ResourceRecordSets'][1])
#print(response['ResourceRecordSets'][0]['Name'])
#print(response['ResourceRecordSets'][0]['ResourceRecords'][0]['Value'])

