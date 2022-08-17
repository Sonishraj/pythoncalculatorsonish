import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="root",
        database="pythoncalc",
    ) as connection:
        print(connection)
        select_movies_query = "SELECT * FROM input_output LIMIT 5"
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:
                print(row[0])
                input=row[1]
                output=row[2]
                operation=row[3]
                print(input)
                print(output)
                print(operation)
except Error as e:
    print(e)

