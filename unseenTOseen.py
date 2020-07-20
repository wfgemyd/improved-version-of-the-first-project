import imaplib
import email
from email.header import decode_header
import temp
def UNseenTOseen():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    (retcode, capabilities) = mail.login('xxx@gmail.com','pass')
    mail.list()
    mail.select('inbox')

    n=0
    (retcode, messages) = mail.search(None, '(UNSEEN)')
    if retcode == 'OK':
        if messages is not None:
            temp.Seen_ = True
       
        for num in messages[0].split():
            print ('Processing ')
            n=n+1
            typ, data = mail.fetch(num,'(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    original = email.message_from_bytes(response_part[-1])
                    print (original['From'])
                    print (original['Subject'])
                    typ, data = mail.store(num,'+FLAGS','\\Seen')
            return True

#print(n)