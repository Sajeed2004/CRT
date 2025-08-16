from db import connection
conn=connection()
if conn:
    print("connection is estabilished successfully")
else:
    print("connection failed")
def insert_data():
    serial_num=int(input("Enter the serial_num:"))
    category=input("Enter the category:")
    item=input("Enter Item:")
    cost=input("Enter Cost:")
    curser=conn.cursor()
    query="insert into expenses(serial_num,category,item,cost)value(%s,%s,%s,%s)"
    values=(serial_num,category,item,cost)
    curser.execute(query,values)
    conn.commit()
    print("Data inserted sucessfully")
def fetch_data():
    cursor=conn.cursor()
    query="select * from expenses"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)
fetch_data()
def update_data():
    serial_num=int(input("Enter the serial_num:"))
    category=input("Enter the updated category:")
    item=input("Enter updated Item:")
    cost=input("Enter updated Cost:")
    cursor=conn.cursor()
    query="update expenses set category=%s,item=%s,cost=%s where serial_num=%s"
    values=(category,item,cost,serial_num)
    cursor.execute(query,values)
    conn.commit()
    print("Data updated sucessfully")
def delete_data():
    serial_num = int(input("Enter the serial_num of the record to delete: "))
    cursor = conn.cursor()
    query = "DELETE FROM expenses WHERE serial_num=%s"
    cursor.execute(query,(serial_num,))
    conn.commit()
    print("Data deleted successfully")
print("1.insert data")
print("2.fetch data")
print("3.update data")
print("4.delete data")
print("enter 5 to exit")
while True:
    choice=int(input("Enter your choice(1-4):"))
    if choice==1:
        insert_data()
    elif choice==2:
        fetch_data()
    elif choice==3:
        update_data()
    elif choice==4:
        delete_data()
        print("exiting...")
        break