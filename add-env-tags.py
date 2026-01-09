import boto3

# Mumbai region
ec2_client_mumbai = boto3.client('ec2', region_name="ap-south-1")
ec2_resource_mumbai = boto3.resource('ec2', region_name="ap-south-1")

# Get all instances
response = ec2_client_mumbai.describe_instances()

instance_ids = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

print("Instances found:", instance_ids)

# Add tags if instances exist
if instance_ids:
    ec2_client_mumbai.create_tags(
        Resources=instance_ids,
        Tags=[
            {'Key': 'environment', 'Value': 'dev'}
        ]
    )
    print(" Tag added successfully!")
else:
    print("No instances found in Mumbai region.")
