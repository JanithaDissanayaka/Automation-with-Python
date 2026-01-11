import requests
import smtplib
import os
import paramiko

EMAIL_ADDRESS=os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')

def send_notification(email_msg):
     with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            message=f"Subject:Application Error\n{email_msg}"
            smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,message)
     


try:
    response=requests.get('http://ec2-13-232-197-1.ap-south-1.compute.amazonaws.com:8080/')
    if False:#response.status_code==200:   
        print("Application running successfully")
    else:
        print("Apllication running Unsuccsfull")
        #send email if application not work
        msg=f'application returened {response.status_code}'
        send_notification(msg)

        #fix errors
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='13.232.197.1',username='ec2-user',key_filename="C:/Users/Janitha/Music/python.pem")
        stdin,stdout,stderr =ssh.exec_command('docker ps')
        print(stdout.readlines())
        ssh.close()
        
except Exception as ex:
    print(f"Connection error happned :\n {ex}" )
    msg=f'application not asscessible!!!' 
    send_notification(msg)
