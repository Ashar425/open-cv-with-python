import cv2
import numpy as np

platecascade=cv2.CascadeClassifier("class 40\\haarcascade_russian_plate_number.xml")

count=0

test1=cv2.imread("class 40\\car2.jpg",0)

platelist=platecascade.detectMultiScale(test1,1.2,5)
print(platelist)

for (x,y,w,h) in platelist:
    test11=cv2.rectangle(test11,(x,y),(x+w,y+h),(0,255,0),2)
    count=count+1

cv2.imshow("number plate detection",test1)

cv2.destroyAllWindows()
print(platelist)