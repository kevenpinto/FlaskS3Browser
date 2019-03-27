import boto3
import os
from collections import namedtuple

class S3(object):
    _S3_BUCKET = ' '
    _S3_ACCESS_KEY = 'ENTER KEY HERE'
    _S3_SECRET =  'ENTER KEY HERE'
    _APP_SECRET_KEY = os.urandom(32)
    S3Config = namedtuple('S3Config','S3_ACCESS_KEY S3_SECRET S3_BUCKET APP_SECRET_KEY')

    @staticmethod
    def get_config():
        s3config = S3.S3Config(S3._S3_ACCESS_KEY, S3._S3_SECRET, S3._S3_BUCKET, S3._APP_SECRET_KEY)
        return s3config

    @staticmethod
    def get_resource():
        # Establish a Connection to AWS
        s3_resource = boto3.resource(
            "s3",
            aws_access_key_id = S3._S3_ACCESS_KEY,
            aws_secret_access_key = S3._S3_SECRET
        )
        return s3_resource

    @staticmethod
    def get_buckets_list():
        client = boto3.client('s3')
        return client.list_buckets().get('Buckets')
