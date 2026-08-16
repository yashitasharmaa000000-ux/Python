import mysql.connector
from mysql.connector import Error


try:
    print("Connecting to MySQL...")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yashita",
        database="my_database"
    )

    if conn.is_connected():
        print("Connected to MySQL successfully!")

        my_cursor = conn.cursor()

        # Your SQL operations would go here

        conn.commit()
        print("Connection completed successfully.")

except Error as e:
    print(f"MySQL Error: {e}")

finally:
    try:
        if "my_cursor" in locals() and my_cursor:
            my_cursor.close()

        if "conn" in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

    except Error as e:
        print(f"Error while closing connection: {e}")