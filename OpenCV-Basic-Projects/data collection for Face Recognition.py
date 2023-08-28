import cv2 #opencv 
import os #library os

haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'dataset'  
sub_data = 'heerthi'
 

path = os.path.join(datasets, sub_data) #/dataset/sanjay

if not os.path.isdir(path): #if this folder is not present
    os.mkdir(path) #create that folder
(width, height) = (130, 100)   


face_cascade = cv2.CascadeClassifier(haar_file) #loading face detection alg.
webcam = cv2.VideoCapture(0) #camera initialization 

count = 1

while count < 31:
    print(count)
    (_, im) = webcam.read() #read frame from camera
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #color frame to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 4) #detect face.
    for (x,y,w,h) in faces: 
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle around face
        face = gray[y:y + h, x:x + w] #crop only face part
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path,count), face_resize)
        count += 1
	
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()

