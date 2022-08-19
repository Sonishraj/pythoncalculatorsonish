from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import boto3

app = Flask(__name__)

endpoint_url = "http://localstack:4566"
def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'mysqlp_db_1',
        'port': '3308',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    #cursor = connection.cursor()
    #cursor.execute('SELECT * FROM test_table')
    #results = [{name: color} for (name, color) in cursor]
    #cursor.close()
    #connection.close()

    return connection


@app.route('/')
def index2() -> str:
    sqs = boto3.client("sqs", endpoint_url=endpoint_url)
    response = sqs.create_queue(
    QueueName='calculation-queue',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
    )

    print(response['QueueUrl'])

    #return json.dumps({'test_table': response['QueueUrl']})
    return json.dumps({'test_table': test_table()})
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

@app.route('/addition/<path:varargs>')
def index(varargs=None):
    operation='addition'
    sum=0
    send_message(varargs)
    varargs_receive = receive_message()
    varargs1=varargs_receive.split("/")
    print(varargs)
    '''for i in varargs1:
        if(i!=''):
            sum+=int(float(i))
            print('calculating')'''
    con = test_table()
    # Using cursor() method to create cursor object
    cursor = con.cursor()
    select_movies_query = "SELECT * FROM devopsroles.input_output  WHERE operationtype ='{}' ".format(operation)
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
        select_movies_query = "SELECT * FROM devopsroles.input_output WHERE inputargs='{}' and operationtype='{}' LIMIT 1".format(varargs,operation)
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
            sum = output
        print('returning from DB')
    else:
        for i in varargs1:
            if(i!=''):
                sum+=int(float(i))
                print('calculating')
        # Sql query to insert date into table
        sql_query = "INSERT INTO devopsroles.input_output(inputargs, output, operationtype) VALUES ('{}','{}', '{}' )".format(varargs,sum,operation)

        # Executing the SQL command
        cursor.execute(sql_query)

        # Commit your changes in the database
        con.commit()
    return json.dumps({'result': sum,
                       })    


if __name__ == '__main__':
    app.run(host='0.0.0.0')

