import urllib.request # to access url
import cv2
import numpy as np
import imutils

url= 'http://192.168.29.143:8080/shot.jpg'

while True:
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()), dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img=imutils.resize(img,width=450)
    cv2.imshow("cameraFeed",img)
    if ord('q') ==  cv2.waitKey(1):
        exit(0)
