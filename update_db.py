import sqlite3
import os


db_path = "instance/medcare.db"


if not os.path.exists(db_path):

    print("Database not found")

    exit()


conn = sqlite3.connect(db_path)

cursor = conn.cursor()



# Check tables

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
)


tables = cursor.fetchall()


print("Tables found:")

for table in tables:
    print(table[0])



# Check queue_tokens columns

if ("queue_tokens",) in tables:

    cursor.execute(
        "PRAGMA table_info(queue_tokens)"
    )


    columns = cursor.fetchall()


    print("\nQueue Token Columns:")

    for column in columns:
        print(column[1])


    existing_columns = [
        column[1] for column in columns
    ]


    if "department" not in existing_columns:

        cursor.execute(
            """
            ALTER TABLE queue_tokens
            ADD COLUMN department VARCHAR(100)
            """
        )


        print(
            "department column added"
        )


    else:

        print(
            "department already exists"
        )


else:

    print(
        "queue_tokens table does not exist"
    )



conn.commit()

conn.close()