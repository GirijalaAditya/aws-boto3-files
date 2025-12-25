import boto3

aws=boto3.session.Session(profile_name="")

s3=aws.resource('s3')

print("S3 Buckets:")
for each_bucket in s3.buckets.all():
    print(each_bucket.name)