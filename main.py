from djitellopy import tello  # Main Library
from time import sleep  # Time library
# import cv2  # Computer vision library

# Tello WIFI Name = F16662
# Setup
F16 = tello.Tello()
F16.connect()
print(F16.get_battery(), "%")
# F16.set_video_direction(F16.CAMERA_FORWARD)
# F16.set_video_resolution(F16.RESOLUTION_480P)
# F16.set_video_fps(F16.FPS_30)

# Launch
F16.takeoff()

# Main Code
if F16.get_battery() <= 20:
    F16.rotate_clockwise(360)
    sleep(1)
    F16.land()
else:
    # F16.streamon()
    F16.send_rc_control(0, 10, 10, 0)
    F16.move_up(10)
    sleep(1)
    F16.move_forward(10)
    sleep(2)
    F16.move_back(10)
    print(F16.get_height())
    sleep(1)
    F16.streamoff()
    F16.flip_forward()
    sleep(1)
    F16.flip_back()
    sleep(1)
    print(F16.get_battery())
    F16.land()

# Stream test
# while True:
#     img = F16.get_frame_read().frame
#     img = cv2.resize(img, (360, 240))
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
