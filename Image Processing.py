

import cv2

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1= cv2.imread('G:\CV\gojo.png',1)  # 1 for RGB
img1= cv2.resize(img1,(720,480))   # resize image width,height
#img1= cv2.flip(img1,1)            #flip image sides
print(img1)                        #imamge array
cv2.imshow("Gojo sataru",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
k= cv2.waitKey()                #image display holding time- waitKey(millisecond)

if k== ord('q'):                #Quit image when pressed 'q'
    cv2.destroyAllWindows()
    
elif k== ord('s'):
    cv2.imwrite("G:\CV\gojo new.png",img1)    #save image with given name when pressed 's'
    cv2.destroyAllWindows()      
    
    
    
    