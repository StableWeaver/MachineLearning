import psutil
import os
import sys
import traceback
from Assignment12_1 import ProcessDisplay
from datetime import datetime
import time
import smtplib
from urllib.request import urlopen
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def is_connected():
    try:
        urlopen("http://216.58.192.142",timeout=2)
        return True
    except:
        return False    


def sendemail(filep):
    import email, smtplib, ssl
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "Process Log from Andromeda"
    body = "Process log ............."
    sender_email = "aru8ash@gmail.com"
    receiver_email = str(sys.argv[2])
    password = input("Type your password and press enter:")

    try:
      # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
       

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = filep  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        filename=os.path.basename(filename)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        server.close()

    except Exception :
        print("Some ERROR")
        print(traceback.format_exc())
      



def logprocesslistmail(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)
    if exists:
        filep=os.path.join(path,"ProcessMonitorLogger"+str(datetime.now()))
        fd=open(filep,encoding="utf-8" ,mode="w")
        proclist=ProcessDisplay()
        for i in proclist:
            fd.write(str(i)+"\n")

        fd.close()   

        sendemail(filep) 
    else:
        print("Folder doesn't exists.")

def main():

    if len(sys.argv)==2:
        if sys.argv[1].lower=="-h":
                print("Script is designed to create a log file in desired folder and mail it" )
                exit()

        if sys.argv[1].lower=="-u":
                print("Usage: Appname Folder_name Email_id")
                exit() 

    if len(sys.argv)<3 or len(sys.argv)>3:
        print("ERR: Invalid no of Args")
        exit()
    try :
        print("#"*80)
        print(" "*29+"Process mail to email")
        print("#"*80)

        logprocesslistmail(sys.argv[1])
        print("Email Sent..............")


    except Exception as e:
        print("ERR: Invalid Input"+str(e))

if __name__=="__main__":
    main()        

