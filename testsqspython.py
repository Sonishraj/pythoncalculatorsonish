import boto3
import json

def create_queue():
    sqs_client = boto3.client("sqs", region_name="us-east-1",endpoint_url="http://localhost:4566")
    response = sqs_client.create_queue(
        QueueName="calculation-queue",
        Attributes={
            "DelaySeconds": "0",
            "VisibilityTimeout": "60",  # 60 seconds
        }
    )
    print(response)
def send_message():
    sqs_client = boto3.client("sqs", region_name="us-east-1",endpoint_url="http://localhost:4566")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl="http://localhost:4566/000000000000/calculation-queue",
        MessageBody=json.dumps(message)
    )
    print(response)
def receive_message():
    sqs_client = boto3.client("sqs", region_name="us-east-1",endpoint_url="http://localhost:4566")
    response = sqs_client.receive_message(
        QueueUrl="http://localhost:4566/000000000000/calculation-queue",
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10,
    )

    print(f"Number of messages received: {len(response.get('Messages', []))}")

    for message in response.get("Messages", []):
        message_body = message["Body"]
        pathval=json.loads(message_body)
        print(pathval["key"])
        
        #print(f"Message body: {json.loads(message_body)}")
        #print(f"Receipt Handle: {message['ReceiptHandle']}")
        
create_queue()    
#send_message()
#receive_message()
   
