import time

for a in range (1, 101):
    b = a
    while int(len(str(b))) > 1:
        b = str(b)
        b = int(str(b[0]))+int(str(b[1]))
    print(str(a)+' = '+str(b))
    time.sleep(.1)


