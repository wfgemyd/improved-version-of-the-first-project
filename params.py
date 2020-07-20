
import time
import cv2
import datetime
import os

def Photo_rename(pq):
    cap = cv2.VideoCapture(0) #starting the video
    cap.set(3,640) #width=640
    cap.set(4,480) #height=480
    datetime_ = str(datetime.datetime.now()) #setting the date
    font = cv2.FONT_HERSHEY_SIMPLEX #setting the font
    if cap.isOpened():
        _,frame = cap.read() #stoping the video on a single frame for the next processes
        cap.release() #releasing camera immediately after capturing picture
        print("the camera finished to take the photo")
        cv2.imwrite('intruder%s.jpg'%pq, frame) #creating the file
        print("now its a file")
        #frame = cv2.flip(frame, 0)
        img = cv2.imread('intruder%s.jpg'%pq,1) #reading image
        #shoving into the image the date and time 
        img_up = cv2.putText(img, datetime_, (10,50), font, 1,(255,255,0), 1, cv2.LINE_AA) #if its an video you need to mange it like an image, frame by frame
        cv2.imwrite('intruder%s.jpg'%pq, img_up) #rewritnig the image with the new params
        print("now its a rewriten file")
    
              