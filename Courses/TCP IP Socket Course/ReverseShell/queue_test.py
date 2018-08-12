import queue

new = queue.Queue()

new.put('hello')
new.put('world')

print (new.qsize())

x = new.get()
print (x)

x = new.get()
print (x)

print (new.qsize())