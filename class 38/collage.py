import numpy as np
import cv2
import os
from PIL import Image

averagewidth=0
averageheight=0
os.chdir("C:\\Users\\gulqa\\OneDrive\\Desktop\\Ashar open cv\\class 38\\images")
path="C:\\Users\\gulqa\\OneDrive\\Desktop\\Ashar open cv\\class 38\\images"
numberofimg=len(os.listdir("."))
print(numberofimg)

for i in os.listdir():
    currentimg=Image.open(os.path.join(path,i))
    width,height=currentimg.size
    averagewidth=averagewidth+width
    averageheight=averageheight+height

averagewidth=averagewidth//numberofimg
averageheight=averageheight//numberofimg
print(averageheight)
print(averagewidth)

for i in os.listdir():
    currentimg=Image.open(os.path.join(path,i))
    resizedimg=currentimg.resize((averagewidth,averageheight),Image.Resampling.LANCZOS)
    resizedimg.save(i,"jpeg")

videoname="collage.avi"
images=[]
for i in os.listdir("."):
    images.append(i)

print(images)
video=cv2.VideoWriter(videoname,0,2,(averagewidth,averageheight))

for i in images:
    video.write(cv2.imread(os.path.join(".",i)))

cv2.destroyAllWindows()
video.release()