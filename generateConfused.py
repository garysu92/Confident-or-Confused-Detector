# sudo python3 generateConfused.py

import cv2
import time
import keyboard

cap = cv2.VideoCapture(0)
time.sleep(1)
for i in range(20):
    print("generating" + str(i))
    ret, frame = cap.read()
    imgname = "./train/images/confused" + str(i) + ".jpg"
    cv2.imwrite(imgname, frame)
    keyboard.wait('space')

