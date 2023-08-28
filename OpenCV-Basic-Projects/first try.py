import cv2
import imutils

img= cv2.imread("sample2.jpg")
cv2.imwrite("sample1Copy.png",img)
cv2.imshow("AI_Master_Class",img)
