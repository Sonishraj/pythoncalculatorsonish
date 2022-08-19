import json
import boto3
import mysql.connector
from mysql.connector import errorcode
from flask import Flask
from typing import List, Dict
app = Flask(__name__)

def create_queue():
    sqs_client = boto3.client("sqs", region_name="us-east-1",endpoint_url="http://localstack:4566")
    response = sqs_client.create_queue(
        QueueName="calculation-queue",
        Attributes={
            "DelaySeconds": "0",
            "VisibilityTimeout": "60",  # 60 seconds
        }
    )
    print(response)
def send_message(value):
    sqs_client = boto3.client("sqs", region_name="us-east-1",endpoint_url="http://localstack:4566")

    message = {"key": value}
    response = sqs_client.send_message(
        QueueUrl="http://localhost:4566/000000000000/calculation-queue",
        MessageBody=json.dumps(message)
    )
    print(response)
def receive_message():
    sqs_client = boto3.client("sqs", region_name="us-east-1",endpoint_url="http://localstack:4566")
    response = sqs_client.receive_message(
        QueueUrl="http://localhost:4566/000000000000/calculation-queue",
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10,
    )

    print(f"Number of messages received: {len(response.get('Messages', []))}")
    value=""
    for message in response.get("Messages", []):
        message_body = message["Body"]
        pathval=json.loads(message_body)
        print(pathval["key"])
        value=pathval["key"]
    return value
        #print(f"Message body: {json.loads(message_body)}")
        #print(f"Receipt Handle: {message['ReceiptHandle']}")
    
#create_queue()    


def getConnection()-> List[Dict]:
    try:
       
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': '3308',
            'database': 'pythoncalc'
        }
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Your user name or password is incorrect")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            con.rollback()
            print(err)


@app.route('/multiplication/<path:varargs>')
def index1(varargs=None):
    mul=1
    send_message(varargs)
    varargs_receive = receive_message()
    varargs1=varargs_receive.split("/")
    operation = 'multiplication'
    print(varargs1)
    con = getConnection()
    # Using cursor() method to create cursor object
    cursor = con.cursor()
    select_movies_query = "SELECT * FROM pythoncalc.input_output  WHERE operationtype ='{}' ".format(operation)
    cursor.execute(select_movies_query)
    result = cursor.fetchall()
    print(type(result))
    print(result)
    inputargslist = []
    for row in result:
        print(row[0])
        input=row[1]
        inputargslist.append(input)
        output=row[2]
        operation=row[3]
        print(input)
        print(output)
        print(operation)
    output = 0
    #print(bool(varargs in result for i in result))
    #print(bool(operation in result for i in result))
    if(varargs in inputargslist):
        print('element exist')
    else:
        print('element doesnt exist')
    if(varargs in inputargslist):
        select_movies_query = "SELECT * FROM pythoncalc.input_output WHERE inputargs='{}' and operationtype='{}' LIMIT 1".format(varargs,operation)
        cursor.execute(select_movies_query)
        result = cursor.fetchall()
        print(result)

        for row in result:
            print(row[0])
            input=row[1]
            output=row[2]
            operation=row[3]
            print(input)
            print(output)
            print(operation)
            mul = output
        print('returning from DB')
    else:
        for i in varargs1:
            if(i!=''):
                mul*=int(float(i))
        # Sql query to insert date into table
        sql_query = "INSERT INTO input_output(inputargs, output, operationtype) VALUES ('{}','{}', '{}' )".format(varargs,mul,operation)

        # Executing the SQL command
        cursor.execute(sql_query)

        # Commit your changes in the database
        con.commit()
    return json.dumps({'result': mul,
                       })

app.run(host="0.0.0.0")
