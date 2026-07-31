import sqlite3


connection = sqlite3.connect("medcare.db")

cursor = connection.cursor()


# Check queue_tokens table

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
)

tables = cursor.fetchall()


print("Tables:")

for table in tables:
    print(table[0])



if ("queue_tokens",) in tables:


    cursor.execute(
        "PRAGMA table_info(queue_tokens)"
    )

    columns = cursor.fetchall()


    column_names = [
        column[1]
        for column in columns
    ]


    print("\nExisting columns:")
    print(column_names)



    if "department" not in column_names:

        cursor.execute(
            """
            ALTER TABLE queue_tokens
            ADD COLUMN department VARCHAR(100)
            """
        )

        print(
            "Department column added successfully"
        )

    else:

        print(
            "Department column already exists"
        )


else:

    print(
        "queue_tokens table not found"
    )



connection.commit()

connection.close()