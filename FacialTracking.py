import cv2
import numpy as np
from djitellopy import tello
from time import sleep

F16 = tello.Tello()
F16.connect()
print(F16.get_battery())
F16.streamon()
F16.takeoff()
F16.send_rc_control(0, 0, 20, 0)
sleep(2)

w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cx = x+w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img,(cx, cy), 5,(0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

def trackFace(F16, info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    fb = 0
    error = x - w//2
    speed = pid[0]*error + pid[1]* (error-pError)
    speed = int(np.clip(speed, -100, 100))

    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20
    if x == 0:
        speed = 0
        error = 0

    #print(speed, fb)
    F16.send_rc_control(0, fb, 0, speed)
    return error

cap = cv2.VideoCapture(0)

while True:
    #_, img = cap.read()
    img = F16.get_frame_read().frame
    img = cv2.resize(img,(w, h))
    img, info = findFace(img)
    pError = trackFace(F16, info, w, pid, pError)
    #print("Area", info[1], "Center", info[0])
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        F16.land()
        break
