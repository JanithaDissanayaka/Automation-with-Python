import boto3
import schedule

client = boto3.client('ec2')


def volume_backup():
    volumes=client.describe_volumes(
        Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'prod',
            ]
        }
    ],
    )
    for volume in volumes['Volumes']:
        new_sanpshot=client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_sanpshot)

schedule.every(10).seconds.do(volume_backup)

while True:
    schedule.run_pending()