import requests
import smtplib
import os
import paramiko
import boto3
import time
import schedule

EMAIL_ADDRESS=os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')

def send_notification(email_msg):
     with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            message=f"Subject:Application Error\n{email_msg}"
            smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,message)

def restart_container():
     #fix errors
     print("restarting the application......")

     ssh=paramiko.SSHClient()
     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     ssh.connect(hostname='13.232.197.1',username='ec2-user',key_filename="C:/Users/Janitha/Music/python.pem")
     stdin,stdout,stderr =ssh.exec_command('docker start 50113d1fed44')
     print(stdout.readlines())
     ssh.close()
     
def reboot_and_resatrt():
    print("Reboooting .....")
    client = boto3.client('ec2')
    response = client.reboot_instances(
    InstanceIds=[
        'i-0db759e73a2f75359',
    ],
    )
    print(response)

    #restartt application 
    print("Restarting.....")   
    while True:
        response = client.describe_instances(
        InstanceIds=["i-0db759e73a2f75359"]
        )
        reservations = response["Reservations"]
        instances = reservations[0]["Instances"]
        state = instances[0]["State"]["Name"]

        if state=="running":
             time.sleep(10)
             restart_container()
             break
        else:
             time.sleep(10)


def monitor_application():
    try:
        response=requests.get('dns url')
        if response.status_code==200:   
            print("Application running successfully")
        else:
            print("Apllication running Unsuccsfull")
            #send email if application not work
            msg=f'application returened {response.status_code}'
            send_notification(msg)
            restart_container()

            
            
    except Exception as ex:
        print(f"Connection error happned :\n {ex}" )
        msg=f'application not asscessible!!!' 
        send_notification(msg)
        reboot_and_resatrt()

schedule.every(5).minutes.do(monitor_application)

while True:
     schedule.run_pending()
