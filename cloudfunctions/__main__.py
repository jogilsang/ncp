# # import pyjokes
# import boto3

# def main(args):
#     # return {"joke": pyjokes.get_joke()}
#     return {"boto3": boto3.resource('s3')}


import boto3

service_name = "s3"
endpoint_url = "http://test-0923.s3-website.kr.object.ncloudstorage.com"
access_key = 'IBFHiUvZEYu1Myhx5uTp'
secret_key = 'OwO07EyQOBsSvYcPyTWldgdACQZYbePewB8houNO'

def main(args):
  try:
    s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    bucket_name = "sample-bucket"
    object_name = args["object"]

    # add read permission to anonymous
    s3.put_object_acl(Bucket=bucket_name, Key=object_name, ACL="public-read")
    return {"result": "success"}

  except Exception as e:
    return {"error_msg": e}



# import boto3

# service_name = 's3'
# endpoint_url = 'https://kr.object.ncloudstorage.com'
# region_name = 'kr-standard'
# access_key = 'IBFHiUvZEYu1Myhx5uTp'
# secret_key = 'OwO07EyQOBsSvYcPyTWldgdACQZYbePewB8houNO'

# def main(args):
# #   name = args.get("name", "World")
# #   place  = args.get("place", "Naver")
# #   return {"payload": "Hello, " + name + " in " + place + "!"}

#     s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
#                       aws_secret_access_key=secret_key)

#     response = s3.list_buckets()

#     for bucket in response.get('Buckets', []):
#         print(bucket.get('Name'))