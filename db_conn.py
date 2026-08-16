
import mysql.connector
from mysql.connector import Error


# MySQL connection configuration
config = {
    "host": "localhost",
    "user": "root",
    "password": "yashita",  # Replace with your MySQL root password
    "port": 3306,
}


def setup_database_and_operations():
    connection = None
    cursor = None

    try:
        # 1. Connect to MySQL Server
        print("Connecting to MySQL Server...")

        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("Connected to MySQL Server successfully.")

            cursor = connection.cursor()

            # 2. Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS app_db")
            print("Database 'app_db' verified/created.")

            # Select the database
            cursor.execute("USE app_db")

            # 3. Create table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """

            cursor.execute(create_table_query)
            print("Table 'users' verified/created.")

            # 4. Insert data
            insert_query = """
            INSERT INTO users (name, email)
            VALUES (%s, %s)
            """

            user_data = [
                ("Alice Smith", "alice@example.com"),
                ("Bob Jones", "bob@example.com"),
            ]

            rows_inserted = 0

            for user in user_data:
                try:
                    cursor.execute(insert_query, user)
                    rows_inserted += cursor.rowcount

                except Error as err:
                    # MySQL error 1062 = duplicate entry
                    if err.errno == 1062:
                        print(f"User with email {user[1]} already exists. Skipping.")
                    else:
                        raise

            # Save changes
            connection.commit()

            print(
                f"Data inserted/verified successfully. "
                f"New rows inserted: {rows_inserted}"
            )

            # 5. Retrieve data
            select_query = """
            SELECT id, name, email, created_at
            FROM users
            ORDER BY id
            """

            cursor.execute(select_query)
            rows = cursor.fetchall()

            print("\n--- User Records ---")

            if rows:
                for row in rows:
                    print(
                        f"ID: {row[0]} | "
                        f"Name: {row[1]} | "
                        f"Email: {row[2]} | "
                        f"Joined: {row[3]}"
                    )
            else:
                print("No users found.")

    except Error as e:
        print(f"MySQL Error: {e}")

    finally:
        # 6. Safe cleanup
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()
            print("\nMySQL connection safely closed.")


if __name__ == "__main__":
    setup_database_and_operations()
