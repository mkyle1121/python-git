import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName = 'test_q')

for mes in queue.receive_messages():
    print (mes.body)
    mes.delete()



