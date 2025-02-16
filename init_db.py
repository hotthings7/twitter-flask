import sqlite3

# Create a new SQLite database file (if it doesn't exist)
conn = sqlite3.connect('credentials.db')

# Create a table to store credentials
conn.execute('''CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);''')

print("Database and table created successfully!")

# Close the connection
conn.close()
