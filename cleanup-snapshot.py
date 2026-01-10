import boto3
from operator import itemgetter
from datetime import time

client = boto3.client('ec2')

volumes=client.describe_volumes(
        Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'prod',
            ]
        }
    ]
    )

for volume in volumes['Volumes']:

    snapshots = client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
        {
            'Name': 'volume_id',
            'Values': [volume['VolumeId'] ]
        }
    ]
    )
    sorted_by_Date=sorted(snapshots['Snapshots'],key=itemgetter('StartTime'),reverse=True)
    for snap in sorted_by_Date[2:]:
        delete_snapshots = client.delete_snapshot(
            SnapshotId=snap['SnapshotId']
        )

