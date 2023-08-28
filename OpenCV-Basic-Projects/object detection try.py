import cv2
import imutils

video_path = "video_1"  # Replace with the path to your video file

cam = cv2.VideoCapture(video_path)

firstFrame = None
area = 500

while True:
    ret, img = cam.read()  # read frame from video

    if not ret:
        print("End of video.")
        break

    text = "Normal"
    img = imutils.resize(img, width=500)  # resize
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)  # smoothened

    if firstFrame is None:
        firstFrame = gaussianImg  # capturing 1st frame on 1st iteration.
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)  # absolute diff b/w
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        text = "Moving Object Detected"

        print(text)
        cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("videoFeed", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
