
x = 'some text'

# print int(x)

try:
    print int(x)
except ValueError as a:
    print 'X is not number'
    print a
except:
    print 'something else went wrong'
else:
    print 'it was correct!'
finally:
    print 'something finally came!'

print 'the end'



