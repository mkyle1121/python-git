import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName = 'test_q')


for i in range (5):
    #response = queue.send_message(MessageBody="{} item!".format(str(i)))
    queue.send_message(MessageBody = "{} item!".format(str(i)))

#print (response.get('MessageId'))
#print (response.get('MD5of MessageBody'))
