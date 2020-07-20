import cv2
import time
import os
# import sound
import full_body_detec
import mail
import reseving_mails_test
import temp
import unseenTOseen

if __name__ == '__main__':
    while True:
        if temp.ph==True:
            if unseenTOseen.UNseenTOseen():
                reseving_mails_test.mail_commands()
                temp.Seen = False
            temp.ph = False
        if full_body_detec.body_detec():
            
            mail.mail_sender()
            print("you got it")
            
            #os.remove('intruder.jpg')
            #print(" every thing is ok")
            # sound.soundd()
            # time.sleep(60)
        #time.sleep(0.5)
0