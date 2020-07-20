import smtplib
from email.message import EmailMessage
import imghdr
def mail_sender():
    EMAIL_ADDRESS = 'xxxxxxx@gmail.com' #GLobal val
    EMAIL_PASSWORD = '' #GLobal val

    contacts = [''] 

    msg = EmailMessage()
    msg['Subject'] = 'secure system'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ', '.join(contacts)
    msg.set_content('')

    files = ['intruder.jpg'] #many files

    for file in files:
        with open(file,'rb') as file_: #Call open(file, mode) with the desired file as file and "rb" as mode to open the binary file.
            file_data = file_.read()
            file_type = imghdr.what(file_.name) #for an image
            file_name = file_.name
            msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name) #for different files you need different main type and subtype
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) #loging in function
        print('logged in securely')
        ######################
        smtp.send_message(msg)
        print('all good the mail has been sent')
