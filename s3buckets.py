#!/usr/bin/python 
import boto3
import sys
import botocore
#used for exception handling

action = sys.argv[1]
bucket_name = sys.argv[2]

s3=boto3.resource('s3')

if action == 'create_bucket':
    print " creating bucket "
    s3.create_bucket(Bucket=bucket_name)

s3_resource=boto3.resource('s3')
#here we are using resource to be able to  perform other actions that are possible on s3

if action == 'delete_bucket':
    print " deleting bucket "
    bucket= s3_resource.Bucket(bucket_name)
    for key in bucket.objects.all():
        key.delete()
        bucket.delete()

if action == 'upload_object':
    print " uploading object "
    s3.resource.Object(bucket_name,hello.txt).put(Body=open('/home/ubuntu/hello.txt', 'r'))
