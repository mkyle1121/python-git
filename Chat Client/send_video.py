import cv2, pickle, socket

S = socket.socket()
S.connect(('192.168.200.10', 5678))
#S.connect(('localhost', 5678))

my_vid = cv2.VideoCapture(0)

while True:
    ret, frame = my_vid.read()

    #resize_frame = cv2.resize(frame, (700,500))

    #print (resize_frame)

    f1 = pickle.dumps(frame)
    #print (f1)
    print (len(f1))
    S.send(f1)

    #print(type(frame))

    #frame = cv2.flip(frame,0)
    #frame = cv2.rectangle(frame,(250,50),(450,400),(255,0,0),3)
    #font = cv2.FONT_HERSHEY_COMPLEX
    #cv2.putText(frame,'Derp',(200,400), font, 2, (255,0,0),2,cv2.LINE_AA)

    cv2.imshow('my_vid', frame)
    if cv2.waitKey(1) == ord('q') :
        break

my_vid.release()
cv2.destroyAllWindows()
S.close()