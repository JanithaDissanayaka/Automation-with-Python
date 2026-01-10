import boto3
from operator import itemgetter

client = boto3.client('ec2', region_name="ap-south-1")
resource= boto3.resource('ec2', region_name="ap-south-1")

instance_id='i-06dc2a744a1d41ad1'

volumes=client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume=volumes['Volumes'][0]

snapshots = client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId'] ]
        }
    ]
    )

latest_snap_shot=sorted(snapshots['Snapshots'],key=itemgetter('StartTime'),reverse=True)[0]
print(latest_snap_shot['StartTime'])

new_Volume=create_volume=client.create_volume(
    SnapshotId=latest_snap_shot['SnapshotId'],
    AvailabilityZone='ap-south-1b',
    TagSpecifications=[
        {
            'ResourceType':'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                },
            ]
        }
    ]
)

while True:
    vol=resource.Volume(new_Volume['VolumeId'])
    print(vol.state)
    if vol.state=="available":
        resource.Instance(instance_id).attach_volume(
            VolumeId=new_Volume['VolumeId'],
            Device='/dev/xvdb'
            
        )
        break