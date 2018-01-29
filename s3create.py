#!/usr/bin/python3
import boto3
s3=boto3.resource('s3')
s3.create_bucket(Bucket='saurabh_dua2413')
