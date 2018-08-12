import two

def one():
    print 'this is one function'

print 'one before main'
print __name__

if __name__=='__main__':
    print 'this is one after main'
    print __name__
    two.two()

