import cv2
import time
import numpy as np


########################################################

wCam, hCam = 648, 480
pTime = 0
########################################################


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}',(40, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0, 255), 3)

    cv2.imshow("img", img)
    cv2.waitKey(1)