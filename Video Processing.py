# -*- coding: utf-8 -*-

## Video Processing : Giving video file
import cv2


cap= cv2.VideoCapture('G:\CV\Burn.mp4')
print(cap)

while True:                      #if ret is true then read frames
    ret,frame= cap.read()        # ret is boolean value
    frame= cv2.resize(frame,(700,450))
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow('gray',gray)
    k= cv2.waitKey(25)           #waitKey(25) value changes video speed
    if k== ord('q'): 
        break


cap.release()    
cv2.destroyAllWindows()





