import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
print(response)
print("###########################\n")

vpcs=response['Vpcs']
print(vpcs)
print("###########################\n")

for vpc in vpcs:
    print(vpc['VpcId'],['OwnerId'])
    cidrs=vpc['CidrBlockAssociationSet']
    print (type ("cidrs") )
    for cidr in cidrs:
        print(cidr['CidrBlock'])