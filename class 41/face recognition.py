import cv2
import numpy as np
import os

datasetpath=r"class 41\dataset"
images=[]
labels=[]
id=0

for subfolders in os.listdir(datasetpath):
    for image in os.listdir(os.path.join(datasetpath,subfolders)):
        currentimg=cv2.imread(os.path.join(datasetpath,subfolders,image),0)
        

        facecaascade=cv2.CascadeClassifier("class 41\haarcascade_frontalface_default.xml")
        facelist=facecaascade.detectMultiScale(currentimg,1.3,2)
        print(facelist)

        for (x,y,w,h) in facelist:
            currentimg=cv2.rectangle(currentimg,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.imshow("current image",currentimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
           

        currentimg=cv2.resize(currentimg,(200,200))
        images.append(currentimg)
        labels.append(id)

    id=id+1
print(images)
print(labels)
print([img.shape for img in images])
(images, labels) = [np.array(lis) for lis in [images, labels]]
model=cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
test1=cv2.imread(r"class 41\ronaldo11.jpg",0)
result=model.predict(test1)
print(result)
