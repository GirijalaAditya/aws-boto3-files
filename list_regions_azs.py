import boto3

aws_session=boto3.session.Session(profile_name="")

ec2_client = aws_session.client(service_name="ec2",region_name="us-west-2")

# Retrieves all regions/endpoints that work with EC2
print("AWS Regions:")
for region in ec2_client.describe_regions()['Regions']:
    print(region['RegionName'])

# Retrieves availability zones only for region of the ec2 object
print("AWS Availability Zones:")
for az in ec2_client.describe_availability_zones()['AvailabilityZones']:
    print(az["ZoneName"])
