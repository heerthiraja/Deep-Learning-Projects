import cv2
import time
import json
import base64
import requests
from authKey import SECRET_KEY

cam = cv2.VideoCapture(0)
while True:

    _,img = cam.read()
    key = cv2.waitKey(1) & 0xff
    cv2.imshow("LicensePlate",img)
    if ( key == ord('q')):
        
        cv2.destroyAllWindows()       
        print("Captured...")
        cv2.imwrite("first.jpg",img)       
        time.sleep(5)        
        IMAGE_PATH = 'first.jpg'

        with open(IMAGE_PATH, 'rb') as image_file:
            img_base64 = base64.b64encode(image_file.read())

        url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
        r = requests.post(url, data = img_base64)

        num_plate=(json.dumps(r.json(), indent=2))
        info=(list(num_plate.split("candidates")))
        print(info)
        plate=info[1]
        plate=plate.split(',')[0:3]
        p=plate[1]
        p1= p.split(":")
        number=p1[1]
        number=number.replace('"','')
        number=number.lstrip()
        print (number)

        if number == "MH120E4433":
            print("----------------------------")
            print("Owner Name: Champ")
            print("Vehicle Nmuber: %s"%number)
            print("Address: MAHARASHTRA")

    elif key == 27:
        break

cam.release()
cv2.destroyAllWindows()
