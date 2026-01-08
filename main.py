import boto3

ec2_client = boto3.client('ec2')
all_avilable_vpcs=ec2_client.describe_vpcs()
vpcs=all_avilable_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    association_set=vpc["CidrBlockAssociationSet"]
    for set in association_set:
        print(set["CidrBlock"])
        print(set["CidrBlockState"])