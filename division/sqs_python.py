import boto3 
sqs = boto3.resource("sqs") 
queue = sqs.get_queue_by_name(QueueName="calculation-queue") 

def process_message(message_body): 
    print(f"processing message: {sqs_message}") # do what you want with the message here 
    pass 
if _name_ == "_main_": 
    while True: 
        messages = sqs_queue.receive_messages() 
        for message in messages: 
            process_message(message.body) 
            message.delete()