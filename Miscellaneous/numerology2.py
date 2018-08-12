import time

for a in range (1, 10001):
    b = a
    while int(len(str(b))) > 1:
        c = 0
        for i in range(len(str(b))):
            b = str(b)
            c = c+int(str(b[i]))
        b = c
    print(str(a)+' = '+str(b))
    time.sleep(.0025)