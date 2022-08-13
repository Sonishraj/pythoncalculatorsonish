import json
import mysql.connector
from mysql.connector import errorcode
from flask import Flask
app = Flask(__name__)


def getConnection():
    try:
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='pythoncalc')
        return con
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Your user name or password is incorrect")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            con.rollback()
            print(err)

@app.route('/addition/<path:varargs>')
def index(varargs=None):
    operation='addition'
    sum=0
    varargs1=varargs.split("/")
    print(varargs)
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
            sum = output
        print('returning from DB')
    else:
        for i in varargs1:
            if(i!=''):
                sum+=int(float(i))
                print('calculating')
        # Sql query to insert date into table
        sql_query = "INSERT INTO input_output(inputargs, output, operationtype) VALUES ('{}','{}', '{}' )".format(varargs,sum,operation)

        # Executing the SQL command
        cursor.execute(sql_query)

        # Commit your changes in the database
        con.commit()
    return json.dumps({'result': sum,
                       })
@app.route('/multiplication/<path:varargs>')
def index1(varargs=None):
    mul=1
    varargs1=varargs.split("/")
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

@app.route('/subtraction/<path:varargs>')
def index2(varargs=None):
    sub=0
    varargs1=varargs.split("/")
    print(varargs1)
    operation= 'subtraction'
    con = getConnection()
    # Using cursor() method to create cursor object
    cursor = con.cursor()
    select_movies_query = "SELECT * FROM pythoncalc.input_output WHERE operationtype ='{}' ".format(operation)
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
            sub = output
        print('returning from DB')
    else:
        for i in varargs1:
            if(i!=''):
                if(sub==0 and int(i)>0):
                    sub=int(float(i))
                else:
                    sub-=int(float(i))
         # Sql query to insert date into table
        sql_query = "INSERT INTO input_output(inputargs, output, operationtype) VALUES ('{}','{}', '{}' )".format(varargs,sub,operation)

        # Executing the SQL command
        cursor.execute(sql_query)

        # Commit your changes in the database
        con.commit()
    return json.dumps({'result': sub,
                       })
@app.route('/division/<path:varargs>')
def index3(varargs=None):
    varargs1=varargs.split("/")
    div=int(float(varargs1[0]))
    new=varargs1[1::]
    print(varargs1[1::])
    operation = 'division'
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
            div = output
        print('returning from DB')
    else:
        for i in new:
            if(i!=''):
                div=div/int(float(i))
        # Sql query to insert date into table
        sql_query = "INSERT INTO input_output(inputargs, output, operationtype) VALUES ('{}','{}', '{}' )".format(varargs,div,operation)

        # Executing the SQL command
        cursor.execute(sql_query)

        # Commit your changes in the database
        con.commit()
    return json.dumps({'result': div,
                       })
app.run()
