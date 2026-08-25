import cv2
import numpy as np

img1 = cv2.imread(r"class 36\lion.jpg")
img2 = cv2.imread(r"class 36\parrot.jpg")

resizeimg1 = cv2.resize(img1, (500, 500))
resizeimg2 = cv2.resize(img2, (500, 500))

addimg = cv2.add(resizeimg1, resizeimg2)

cv2.imshow("Addition image", addimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

subimg = cv2.subtract(resizeimg1, resizeimg2)

cv2.imshow("Subtraction image", subimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

multiplyimg = cv2.multiply(resizeimg1, resizeimg2)

cv2.imshow("Multiplication image", multiplyimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

divideimg = cv2.divide(resizeimg1, resizeimg2)

cv2.imshow("Division image", divideimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

guassianblur = cv2.GaussianBlur(resizeimg2, (33, 33), 0)

cv2.imshow("Gaussian blur image", guassianblur)
cv2.waitKey(0)
cv2.destroyAllWindows()

medianblur = cv2.medianBlur(resizeimg2, 13)

cv2.imshow("Median blur image", medianblur)
cv2.waitKey(0)
cv2.destroyAllWindows()

bilateralblur = cv2.bilateralFilter(resizeimg2, 9, 300, 300)

cv2.imshow("Bilateral blur image", bilateralblur)
cv2.waitKey(0)
cv2.destroyAllWindows()

greyimg2 = cv2.imread(r"class 36\parrot.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)

erodeimg = cv2.erode(greyimg2, kernel, iterations=1)

cv2.imshow("Eroded image", erodeimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

flamingo = cv2.imread(r"class 36\flamingo.jpg")

resizeflamingo = cv2.resize(flamingo, (500, 500))

gaussianflamingo = cv2.GaussianBlur(resizeflamingo, (5, 5), 0)

cv2.imshow("Flamingo Gaussian Blur", gaussianflamingo)
cv2.waitKey(0)
cv2.destroyAllWindows()

medianflamingo = cv2.medianBlur(resizeflamingo, 5)

cv2.imshow("Flamingo Median Blur", medianflamingo)
cv2.waitKey(0)
cv2.destroyAllWindows()

reflectiveflamingo = cv2.copyMakeBorder(gaussianflamingo, 20, 20, 20, 20, cv2.BORDER_REFLECT)

cv2.imshow("Flamingo Reflective Border", reflectiveflamingo)
cv2.waitKey(0)
cv2.destroyAllWindows()