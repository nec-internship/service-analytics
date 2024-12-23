import boto3
from ..classes.sqs_queue_classes import SQSQueueAttributes, SQSQueueTags

class AwsController:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.sqs = boto3.client('sqs')
        
    def s3_list_bucket_names(self):
        s3 = self.s3
        for bucket in s3.buckets.all():
            print(bucket.name)
        pass
    
    def s3_upload_file_to_bucket(
        self, 
        bucket_name: str, 
        file_location : str):
        s3 = self.s3
        with open(file_location, 'rb') as data:
            s3.Bucket(bucket_name).put_object(Key=file_location, Body=data)
        pass
    
    # Return SQSQueue Objects
    def sqs_create_queue(
        self, queue_name: str, 
        attributes: object = {}, 
        tags: object = {}
    ):
        sqs = self.sqs
        queue = sqs.create_queue(
            QueueName=queue_name,
            Atrributes=attributes,
            tags=tags
        )
        return queue
    
    def sqs_list_all_queues(self):
        sqs = self.sqs
        for queue in sqs.queues.all():
            print(queue.url)
