import cv2
import time
import handtrackingmodule as htm
import numpy as np
import math
import pyautogui


wcam,hcam = 640,480
cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
ptime = 0
detector = htm.handdetector(detectionCon=0.7)


while True:
    success,img = cap.read()
    img=detector.findHands(img)
    lmlist = detector.findPosition(img,draw = False)
    if len(lmlist) != 0:
        # print(lmlist[4],lmlist[8])
        x1,y1 = lmlist[4][1],lmlist[4][2]
        x2,y2 = lmlist[8][1],lmlist[8][2]
        x3,y3=lmlist[12][1],lmlist[12][2]
        x4,y4=lmlist[16][1],lmlist[16][2]

        cv2.circle(img,(x1,y1),15,(0,255,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(0,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,255,0),2)
        cx,cy = (x1+x2)//2, (y1+y2)//2
        # cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
        length1 = math.hypot((x2-x1),(y2-y1))
        length2 = math.hypot((x3-x1),(y3-y1))
        length3 = math.hypot((x4-x1),(y4-y1))
        if length1 < 20:
            pyautogui.click()
        if length2 < 20:
            pyautogui.hold('left')
        if length3 < 20:
            pyautogui.hold('up')
        # print(length)
    
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img,str((int(fps))),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),2)
    cv2.imshow('Img',img)
    cv2.waitKey(1)
