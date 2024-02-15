import sqlite3

# Connect to SQLite database (will create if not exists)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Check if the table already exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Table1'")
table_exists = cursor.fetchone()

if not table_exists:
    # Define SQL command to create a table if it doesn't exist
    create_table_query = '''
    CREATE TABLE Table1 (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    );
    '''

    # Execute the SQL command
    cursor.execute(create_table_query)
    print("Table 'Table1' created.")
else:
    print("Table 'Table1' already exists.")

# Commit changes and close connection
conn.commit()
conn.close()
