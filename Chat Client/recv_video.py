import cv2, pickle, socket

S = socket.socket()
S.bind(('localhost',5678))
S.listen(1)
print ('Waiting for connection...')
conn, addr = S.accept()

while True:
    packet = conn.recv(1000000)
    data = packet
    print (bytes.__len__(data))

    #print(data)
    #print(type(data))
    #print(len(data))
    f1 = pickle.loads(data)
    #print(f1)
    cv2.imshow('recv_test', f1)
    cv2.waitKey(1)
    data=None
    if not packet:
        break

#.imshow('recv_test',f1)
#cv2.waitKey(0)
cv2.destroyAllWindows()
S.close()