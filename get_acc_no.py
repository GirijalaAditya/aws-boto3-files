import boto3

sts = boto3.client(service_name="sts")
acc_no = sts.get_caller_identity()["Account"]
print(acc_no)
print("----------------------------")

acc_no = sts.get_caller_identity().get('Account')
print(acc_no)