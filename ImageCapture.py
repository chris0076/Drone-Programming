import sys

from djitellopy import tello
from time import sleep
import KeyPressModule as kp
import cv2

# Tello WIFI Name = F166EC
F16 = tello.Tello()
F16.connect()
print(F16.get_battery(), "%")

F16.streamon()
while True:
    img = F16.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

