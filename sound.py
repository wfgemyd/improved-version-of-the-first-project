import os

def soundd():
    file = "Alarm-Fast.mp3"
    print("alarm alarm")
    os.system("mpg123 " + file)
    

   
    