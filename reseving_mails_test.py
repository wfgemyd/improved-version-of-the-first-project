import imaplib
import email
from email.header import decode_header
import sound
import temp

command = 0
def reseving_mail():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    username = 'xxxx@gmail.com'
    password = ''
    imap.login(username, password)
    status, messages = imap.select("INBOX")
    N = 2
    messages = int(messages[0])

    for i in range(messages, messages-N, -1): #going from the top to the bottom, the newest email messages got the highest id number
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)") # fetches the email message by ID using the standard format specified in RFC 822.
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode()
                # email sender
                from_ = msg.get("From")
                if str(from_) == "name <xxx@gmail.com>" or "name <xxx@gmail.com>":
                    print("From:", from_)
                    print("Subject:", subject)
                    temp.rawraw = str(subject)
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            #print(body)
                            return str(subject)
                
    imap.close()
    imap.logout()
    
    

def mail_commands():
    raw_command = reseving_mail()
    print(raw_command)
    if raw_command == "":
        sond.soundd()
        
    elif new_command == "start_recording":
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        time.sleep(5)
        cap.release()
        
    elif new_command == "take_photo":
        cv2.imwrite('.jpg'%pq, frame1)
        img = cv2.imread('.jpg'%pq,1) 
        img_up = cv2.putText(img, datetime_, (10,50), font, 1,(255,255,0), 1, cv2.LINE_AA)
        cv2.imwrite('.jpg', img_up) 
            
        
    
    #else: #remainder ##tkinter
        
   

