from djitellopy import tello
from time import sleep
import cv2

# Tello WIFI Name = F#####
F16 = tello.Tello()
F16.connect()
print(F16.get_battery(), "%")

# Take-Off
F16.takeoff()
# Hover
sleep(0.5)
F16.flip_forward()
# Landing
F16.land()




