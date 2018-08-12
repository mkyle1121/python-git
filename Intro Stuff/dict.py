post = {"user":209, "message":"something","location":(44.345,54.656)}

post["area"] = 51


print post


post2={"type1":"something1","type2":"something2"}

post2["type3"] = "something3"

print post2

print(post2['type1'])
print("What's up")

print 'I am at',post['location']

if 'location' in post:
    print post['location']
else:
    print 'That is not in the dictionary'

try:
    print post['location']
except KeyError:
    print 'It is not there'

for key in post:
    value = post[key]
    print key, '=', value



