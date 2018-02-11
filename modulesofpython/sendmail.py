import requests
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import File
print(os.listdir())
file=open("mails.txt","r")
mail=list()
for i in file:
    liste=(i.split(","))
    ad=liste[0]
    mail.append(liste[1].replace("\n","").strip())


mult=MIMEMultipart()
mult["from"]=mail[0]
mult["To"]=mail[2]
mult["Subject"]="Subject"
text="Send Message"
body=MIMEText(text,"plain")
mult.attach(body)


try:
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(mail[0],"******")
    server.sendmail(mult["from"],mult["To"],mult.as_string(),mult["Subject"])
    print("MEsaj gönderildi")
    server.close()
except:
    print("Error")
