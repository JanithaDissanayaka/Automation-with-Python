import boto3
ec2_client = boto3.client('ec2')
ec2_resource=boto3.resource('ec2')

reservations=ec2_client.describe_instances()


for reservation in reservations['Reservations']:
    instances=reservation['Instances']
    for instance in instances:
        print(f"Instance {instance['InstanceId']}is {instance['State']}")


statuses=ec2_client.describe_instance_status()

for status in statuses['InstanceStatuses']:
    int_status=status['InstanceStatus']['Status']
    sys_status=status['SystemStatus']['Status']

    print(f"Instance {status['InstanceId']} status is {int_status} and System status is {sys_status}")