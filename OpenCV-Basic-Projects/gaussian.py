import cv2
import imutils
img=cv2.imread("sample2.jpg")
gaussianBlurImg=cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite("GaussianImg.jpg",gaussianBlurImg)
