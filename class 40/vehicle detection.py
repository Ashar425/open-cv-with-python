import cv2
import numpy as np

carcaascade=cv2.CascadeClassifier("class 40\\haarcascade_cars.xml")
video1=cv2.VideoCapture("class 40\\traffic.mp4")
count=0
while video1.isOpened():
    ret,frame1=video1.read()
    carlist=carcaascade.detectMultiScale(frame1,1.1,5)

    for (x,y,w,h) in carlist:
        frame1=cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
        count=count+1
    cv2.imshow("car detection",frame1)
    if cv2.waitKey(33)==27:
        break

cv2.destroyAllWindows()
print(count)