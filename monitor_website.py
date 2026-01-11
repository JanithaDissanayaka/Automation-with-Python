import requests
import smtplib

response=requests.get('http://ec2-35-154-161-68.ap-south-1.compute.amazonaws.com:8080/')
if response.status_code==200:
    print("Application running successfully")
else:
    print("Apllication running Unsuccsfull")
#send email if application not work
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.starttls()
    smtp.ehlo()
    smtp.login("testworks454@gmail.com","")