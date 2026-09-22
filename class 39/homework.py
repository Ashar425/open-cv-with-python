import cv2

image = cv2.imread("class 39\\robert.jpg")
face_cascade = cv2.CascadeClassifier("class 39\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("class 39\\haarcascade_eye.xml")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 10)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face_gray = gray[y:y + h, x:x + w]
    face_color = image[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(face_gray, 1.1, 10)
    print(eyes)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

cv2.imshow("Face and Eye Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()