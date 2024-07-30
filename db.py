import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='843RnR$$',
        port=3306
    )

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES;")
        for db in cursor.fetchall():
            print(db)

except Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        conn.close()
