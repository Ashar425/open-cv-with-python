import cv2
import numpy as np

test1=cv2.imread("class 39\\face1.jpg")
test2=cv2.imread("class 39\\face2.jpg")
test3=cv2.imread("class 39\\faces1.jpg")

eyecascade=cv2.CascadeClassifier("class 39\\haarcascade_eye.xml")
eyelist=eyecascade.detectMultiScale(test2,1.1,5)
print(eyelist)

for (x,y,w,h) in eyelist:
    test2=cv2.rectangle(test2,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("eye detection test",test2)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 