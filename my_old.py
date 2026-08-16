import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password="yashita",
    database='my_database')
my_cusor=conn.cursor()
conn.commit()
conn.close()
print("create connection successfully")