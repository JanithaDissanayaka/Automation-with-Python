import requests
import smtplib
import os

EMAIL_ADDRESS=os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')



response=requests.get('http://ec2-35-154-161-68.ap-south-1.compute.amazonaws.com:8080/')
if response.status_code==200:
    print("Application running successfully")
else:
    print("Apllication running Unsuccsfull")
#send email if application not work
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    msg="Subject: SITE NOT WORK\nFix the Issue"
    smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)
