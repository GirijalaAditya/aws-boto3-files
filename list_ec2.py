import boto3
from pprint import pprint

aws_session = boto3.session.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
    aws_session_token=""
)

sts = aws_session.client(service_name="sts")
acc_no = sts.get_caller_identity()["Account"]
print(acc_no)

# EC2 using Client
ec2_client = aws_session.client(service_name="ec2",region_name="us-west-2")

for instances in ec2_client.describe_instances()['Reservations']:
    for instance in instances['Instances']:
        print("The Instance ID is:{}\nThe IP Address is {}\n".format(instance['InstanceId'],instance['PrivateIpAddress']))


# ec2_resource = aws_session.resource(service_name="ec2",region_name="us-west-2")

# for instance in ec2_resource.instances.all():
#     print(instance.instance_id,":",instance.private_ip_address,":",instance.instance_type)


