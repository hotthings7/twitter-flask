import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('credentials.db')
cursor = conn.cursor()

# Query to fetch all records from the credentials table
cursor.execute("SELECT * FROM credentials")
rows = cursor.fetchall()

# Print out each record (id, email, password)
if rows:
    for row in rows:
        print(f"ID: {row[0]}, Email: {row[1]}, Password: {row[2]}")
else:
    print("No records found in the database.")

# Close the connection
conn.close()

