import boto3

ec2_client = boto3.client('ec2')
all_avilable_vpc=ec2_client.describe_vpcs()
print(all_avilable_vpc)