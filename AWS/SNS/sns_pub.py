import boto3
import json

sns = boto3.client('sns')

message = sns.publish(TargetArn = 'arn:aws:sns:us-west-2:717851530424:cellphone',
                      Message = json.dumps({'default':json.dumps({'key1':'foobar'})}),
                      MessageStructure = 'json'
                      )
#can use message type string or raw