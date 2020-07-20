from picamera import PiCamera
import numpy as np
import time
import cv2
import datetime
import os

def face_detec(pq,classifier):
    datetime_ = str(datetime.datetime.now()) #setting the date
    font = cv2.FONT_HERSHEY_SIMPLEX #setting the font
    cap = cv2.VideoCapture(0)
    found_objects = False
# Define the codec and create VideoWriter object
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    
    
    while(cap.isOpened()):
        ret, frame1 = cap.read()
        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        objects = classifier.detectMultiScale(gray,1.3,5)
        if ret==True:
            
            for (x, y, w, h) in objects:    
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('frame',frame1)
            
            if len(objects) > 0:
                found_objects = True
                print("humam is detected")   
                #cap.release()
                cv2.imwrite('intruder%s.jpg'%pq, frame1) #creating the file
                print("the photo")
            #frame = cv2.flip(frame, 0)
                img = cv2.imread('intruder%s.jpg'%pq,1) #reading image
            #shoving into the image the date and time 
                img_up = cv2.putText(img, datetime_, (10,50), font, 1,(255,255,0), 1, cv2.LINE_AA) #if its an video you need to mange it like an image, frame by frame
                cv2.imwrite('intruder%s.jpg'%pq, img_up) #rewritnig the image with the new params
                    
                    
            
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

# Release everything if job is finished
    cap.release()
    #out.release()
    cv2.destroyAllWindows()
        
     


