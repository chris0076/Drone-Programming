from djitellopy import tello
import KeyPressModule as kp
from time import sleep
import cv2

kp.init()
F16 = tello.Tello()
F16.connect()
print(F16.get_battery())
F16.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    # Negative is Left
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed

    if kp.getKey("f"):
        F16.land()

    if kp.getKey("t"):
        F16.takeoff()

    if kp.getKey("p"):
        F16.flip_forward()

    if kp.getKey("l"):
        F16.flip_back()

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    F16.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
    img = F16.get_frame_read().frame
    # img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)


