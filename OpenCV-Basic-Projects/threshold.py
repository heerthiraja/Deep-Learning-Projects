import cv2
import imutils


img=cv2.imread("sample2.jpg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #BGR- BLLUE,GREEN,RED
thresImg=cv2.threshold(grayImg,180,255,cv2.THRESH_BINARY) [1]
cv2.imwrite("thresholdImage2.jpg",thresImg)
