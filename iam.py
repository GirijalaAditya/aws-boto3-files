import boto3

aws_session=boto3.session.Session(profile_name="")

# print("Available Resources:")
# resources=aws_session.get_available_resources()
# print(resources)

# print("Available Services:")
# services=aws_session.get_available_services()
# print(services)

iam_resource=aws_session.resource(service_name='iam',region_name='us-west-2')
iam_client=aws_session.client(service_name="iam",region_name="us-west-2")


# Listing using Resource Object
for each_user in iam_resource.users.all():
    print(each_user.user_name)

# Listing using Client Object
for user in iam_client.list_users()['Users']:
    print(user['UserName'])

# Listing using Resource Object
for each_role in iam_resource.roles.all():
    print(each_role.role_name)

# Listing using Client Object
for role in iam_client.list_roles()['Roles']:
    print(role['RoleName'])


