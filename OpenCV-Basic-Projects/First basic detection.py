import cv2
import imutils

vs=cv2.VideoCapture(0) #Initialize the camera

# "here there is zero inside closed brackets. why. it changes depend on time. qq
    
while True:
    _,img=vs.read() #reading the frame from the camera
    cv2.imshow("VideoStream",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break
vs.release() #releasing the camera
cv2.destroyAllWindows() #close all windows
