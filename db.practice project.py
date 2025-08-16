import mysql.connector
def connect():
    connection = mysql.connector.connect(
           
       host='localhost',
       user='root',
       password='root',
       database='practice_crt'
    )
    return connection
if(connect()):
    print("connection established successfully")
else:
    print("connection failed")