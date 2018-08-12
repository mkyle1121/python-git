import requests
import json

headers = {'my-new-headers': 'some-header'}
data = {"some":"some data for post"}

data = json.dumps(data)
#print(data)

#r = requests.get('https://cwvjkv3nlc.execute-api.us-west-2.amazonaws.com/default/test_random_int', headers=headers)
#h = requests.post('https://cwvjkv3nlc.execute-api.us-west-2.amazonaws.com/default/test_random_int', data=data)
i = requests.post('http://www.google.com', data=data)
#h = requests.get('http://www.google.com')

#print(r.text)
#print(r.content)

#print(h.text)
print(i.text)
#print(h.text)