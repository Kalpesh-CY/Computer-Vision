## Capture video from webcam 

import cv2



cap= cv2.VideoCapture(0)    #0- for webcam

fourcc= cv2.VideoWriter_fourcc(*"XVID")

#fourcc:codec tells video to save in which format(e.g.'XVID')

#output  contains 4 parameter: name,codec,fps,resolution
output= cv2.VideoWriter('G:\CV\output.avi',fourcc,25.0,(640,480))  #save video

print(cap)
while cap.isOpened():        
    ret,frame= cap.read() 
    if ret== True:              
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert BGR to Gray
        #frame= cv2.flip(frame,0)
        cv2.imshow("frame",frame)
        cv2.imshow('gray',gray)
        output.write(frame)          #write 'gray' to save gray image
        k= cv2.waitKey(25)
        if k== ord('q'):
            break


cap.release()
output.release()
cv2.destroyAllWindows()