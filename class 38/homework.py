import cv2
import os
from PIL import Image

averagewidth = 0
averageheight = 0

path = "C:\\Users\\gulqa\\OneDrive\\Desktop\\Ashar open cv\\class 38\\homework images"

os.chdir(path)

waterfalls = {"Niagara Falls.jpg": "Niagara Falls", "Victoria Falls.jpg": "Victoria Falls", "Angel Falls.jpg": "Angel Falls", "Iguazu Falls.jpg": "Iguazu Falls"}

numberofimg = len(waterfalls)

print(numberofimg)

for i in waterfalls:
    currentimg = Image.open(os.path.join(path, i))
    width, height = currentimg.size
    averagewidth = averagewidth + width
    averageheight = averageheight + height

averagewidth = averagewidth // numberofimg
averageheight = averageheight // numberofimg

print(averageheight)
print(averagewidth)

videoname = "waterfalls.avi"

video = cv2.VideoWriter(videoname, 0, 1, (averagewidth, averageheight))

for i in waterfalls:
    image = cv2.imread(os.path.join(path, i))
    image = cv2.resize(image, (averagewidth, averageheight))
    cv2.putText(image, waterfalls[i], (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    video.write(image)

cv2.destroyAllWindows()

video.release()

print("Video created")