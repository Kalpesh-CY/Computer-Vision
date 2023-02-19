# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 12:18:36 2023

@author: Kalpesh Chaudhari
"""

## Capture video from external source

import cv2

camera = "http://192.168.222.100:8080/video"
#connect your laptop and android device with same network
cap = cv2.VideoCapture(0)   
cap.open(camera)
print("check===",cap.isOpened())

fourcc = cv2.VideoWriter_fourcc(*"XVID")  

output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret == True:
    
        frame = cv2.resize(frame,(900,700))
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        #output.write(frame)
        if cv2.waitKey(1) == ord('q'):   #press to exit
            break
    
 
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()



