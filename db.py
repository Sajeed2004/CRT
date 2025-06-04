import mysql.connector
def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vyas@143",
        database="expenses_tracker"
    )
    return conn
if(connection()):
    print('connection established')
else:
    print('connection failed')