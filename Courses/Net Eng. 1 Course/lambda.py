
a = lambda x,y: x * y

print (a(4,5))


def myfunc(list):
    prod_list=[]
    for x in range(10):
        for y in range(5):
            product = x*y
            prod_list.append(product)
    return prod_list + list

print (myfunc([100,101,102]))


b = lambda list: [x*y for x in range(10) for y in range(5)] + list

print (b([100,101,102]))




def product10(a):
    return a*10

list1=range(10)
print (list1)

new_list = list(map(product10, list1))

print (new_list)

print(list(map((lambda a: a*10),list1)))

### map takes function + list

print(list(filter(lambda a: a>5, list1)))

#print(reduce(myfunc, [1,2,3,4,5]))

#print(reduce(lambda a,b: a+b, list1))

# import math
print(sum(list1))







