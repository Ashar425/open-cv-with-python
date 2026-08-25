import numpy as np
import cv2

birdimg=cv2.imread("class 37\\bird.jpg")
lineimg=cv2.resize(birdimg,(500,500))
lineimg=cv2.line(lineimg,(50,50),(500,500),(0,0,255),thickness=5)
cv2.imshow("line image",lineimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

rectangleimg=cv2.rectangle(lineimg,(100,100),(200,200),(255,0,0),thickness=-8)
cv2.imshow("rectangle image",rectangleimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

circleimg=cv2.circle(lineimg,(400,400),70,(0,255,0),thickness=4)
cv2.imshow("circle image",circleimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

circle2img=cv2.circle(lineimg,(250,250),50,(40,40,40),thickness=-1)
cv2.imshow("filled circle image",circle2img)
cv2.waitKey(0)
cv2.destroyAllWindows()

font=cv2.FONT_HERSHEY_SIMPLEX
start=(100,100)
fontscale=1
color=(255,0,255)
thickness=2
image=cv2.putText(lineimg,"bird image",start,font,fontscale,color,thickness,cv2.LINE_AA)
cv2.imshow("modified bird image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()