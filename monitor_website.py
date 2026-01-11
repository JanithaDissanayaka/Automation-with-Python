import requests
import smtplib
import os

EMAIL_ADDRESS=os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')

def send_notification(email_msg):
     with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            msg=f"Subject:Application Error\n{email_msg}"
            smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)
     


try:
    response=requests.get('http://ec2-35-154-161-68.ap-south-1.compute.amazonaws.com:8080/')
    if response.status_code==200:
        print("Application running successfully")
    else:
        print("Apllication running Unsuccsfull")
        #send email if application not work
        msg=f'application returened{response.status_code}'
        send_notification(msg)
        
except Exception as ex:
    print(f"Connection error happned :\n {ex}" )
    msg=f'application not asscessible!!!'
    send_notification(msg)
