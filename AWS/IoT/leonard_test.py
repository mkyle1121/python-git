from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

stop = ''

def mycallback(client, userdata, message):
    global stop
    pay_msg = message.payload.decode()
    print(pay_msg)
    if pay_msg == 'exit':
        stop = 'exit'

myMQTT = AWSIoTMQTTClient('Leonard')
myMQTT.configureEndpoint('a111amujev1y9r.iot.us-west-2.amazonaws.com', 8883)
myMQTT.configureCredentials('AWS_Root_CA.txt', 'Leonard.private.key', 'Leonard.cert.pem')
myMQTT.configureOfflinePublishQueueing(-1)
myMQTT.configureDrainingFrequency(2)
myMQTT.configureConnectDisconnectTimeout(10)
myMQTT.configureMQTTOperationTimeout(5)

msg = {'data': '1'}
msg2 = 1

messageJson = json.dumps(msg)


myMQTT.connect()
myMQTT.subscribe('randomtopic', 0, mycallback)
#while True:
#    if stop == 'exit':
#        break

myMQTT.publish('randomtopic', messageJson, 0)
myMQTT.unsubscribe('randomtopic')
myMQTT.disconnect()

