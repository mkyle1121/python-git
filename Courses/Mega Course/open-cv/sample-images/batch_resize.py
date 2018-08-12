import os
import cv2


directory=os.listdir()
directory.pop(0)

print(directory)

for picture in directory:
    print(picture)
    image=cv2.imread(picture,0)
    cv2.imshow('Picture',image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    resized_image=cv2.resize(image,(100,100))
    cv2.imshow('Resized',resized_image)
    cv2.waitKey(2000)
    cv2.imwrite('RESIZED '+picture,resized_image)
    cv2.destroyAllWindows()
