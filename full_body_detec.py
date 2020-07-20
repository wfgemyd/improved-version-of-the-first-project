import numpy as np
import time
import cv2
import datetime
import os
import temp
import unseenTOseen
import reseving_mails_test

def body_detec():
    face_cascade = cv2.CascadeClassifier('facial_recognition_model.xml')
    low_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
    datetime_ = str(datetime.datetime.now())
    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)
    is_change_occured = False
    faces_len = 0
    low_len = 0
    
    while cap.isOpened():
        
        ret,img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        low = low_cascade.detectMultiScale(gray, 1.1, 3)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (x, y, w, h) in low:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('frame', img )
        
        if len(faces) == len(low) and len(faces) != 0:
            if faces_len != len(faces) or low_len != len(low):
                is_change_occured = True
            else:
                is_change_occured = False
            
            faces_len = len(faces)
            low_len = len (low)
        
            if is_change_occured and faces_len >= 1:
                cv2.imwrite('intruder.jpg', img)                
                pic = cv2.imread('intruder.jpg', 1)                
                pic = cv2.putText(img, datetime_, (10, 50), font, 1, (255, 255, 0), 1, cv2.LINE_AA)
                cv2.imwrite('intruder.jpg', pic)
                time.sleep(3)
                temp.ph = True
                return True
                
            
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    os.remove('intruder.jpg')
    print(" every thing is ok")
    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()
    
