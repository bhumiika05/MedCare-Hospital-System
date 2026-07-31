import sqlite3


connection = sqlite3.connect("medcare.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS queue_tokens (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name VARCHAR(100) NOT NULL,

    phone VARCHAR(20),

    department VARCHAR(100),

    token_number INTEGER NOT NULL,

    status VARCHAR(30) DEFAULT 'Waiting',

    created_at DATETIME

)
""")


connection.commit()

connection.close()


print("queue_tokens table created successfully")