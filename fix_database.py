import sqlite3
import os


db_path = "instance/medcare.db"


if not os.path.exists(db_path):

    print("Database not found:", db_path)

else:

    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()


    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )


    tables = cursor.fetchall()


    print("Existing tables:")
    
    for table in tables:
        print(table[0])


    connection.close()