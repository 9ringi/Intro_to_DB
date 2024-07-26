import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',      # Update with your MySQL server host
            user='root',           # Update with your MySQL server username
            password='password'    # Update with your MySQL server password
        )

        if connection.is_connected():
            # Create a cursor object using the connection
            cursor = connection.cursor()
            
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Commit the transaction
            connection.commit()

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Handle specific MySQL errors
        print(f"MySQL Error: {e}")

    except Exception as e:
        # Handle other exceptions
        print(f"General Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
