import boto3
ec2_client = boto3.client('ec2')
ec2_resource=boto3.resource('ec2')
vpc=ec2_resource.create_vpc(
    CidrBlock='10.0.0.0/16',
)

vpc.create_subnet(
    CidrBlock='10.0.1.0/24'
)
vpc.create_subnet(
    CidrBlock='10.0.2.0/24'
)

vpc.create_tags(
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Python_vpc'
        }
    ]
)

all_avilable_vpcs=ec2_client.describe_vpcs()
vpcs=all_avilable_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    association_set=vpc["CidrBlockAssociationSet"]
    for set in association_set:
        print(set["CidrBlock"])
        print(set["CidrBlockState"])
