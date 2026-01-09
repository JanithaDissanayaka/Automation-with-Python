import boto3
import schedule


ec2_client = boto3.client('ec2')
ec2_resource=boto3.resource('ec2')

def instance_statuses():
    statuses=ec2_client.describe_instance_status(IncludeAllInstances=True)
    for status in statuses['InstanceStatuses']:
        int_status=status['InstanceStatus']['Status']
        sys_status=status['SystemStatus']['Status']
        state = status['InstanceState']['Name']



        print(f"Instance {status['InstanceId']} is {state} with instance status {int_status} and System status is {sys_status}")
        print("#####################################\n")

schedule.every(10).seconds.do(instance_statuses)

while True:
    schedule.run_pending()

