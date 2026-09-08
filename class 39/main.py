import cv2
import numpy as np

test1=cv2.imread("class 39\\face1.jpg")
test2=cv2.imread("class 39\\face2.jpg")
test3=cv2.imread("class 39\\face3.jpg")
test4=cv2.imread("class 39\\faces1.jpg")
test5=cv2.imread("class 39\\people1.jpg")

facecascade=cv2.CascadeClassifier("class 39\\haarcascade_frontalface_default.xml")
faceslist=facecascade.detectMultiScale(test4,1.1,10)
print(faceslist)

for (x,y,w,h) in faceslist:
    test4=cv2.rectangle(test4,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("face detection",test4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()