from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    return 'Welcome to my Flask application!'


# Function to establish SQLite connection
def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row
    return conn

# API endpoint to add data to the database
@app.route('/add_data', methods=['POST'])
def add_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Extract data from JSON request
    data = request.json
    name = data['name']
    age = data['age']

    # Insert data into the database
    cursor.execute('INSERT INTO Table1 (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Data added successfully'})

# API endpoint to delete data from the database
@app.route('/delete_data/<int:id>', methods=['DELETE'])
def delete_data(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Delete data from the database
    cursor.execute('DELETE FROM Table1 WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Data deleted successfully'})

# API endpoint to get all data from the database
@app.route('/get_data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all data from the database
    cursor.execute('SELECT * FROM Table1')
    data = cursor.fetchall()

    # Convert data to JSON format
    data_json = []
    for row in data:
        data_json.append({'id': row['id'], 'name': row['name'], 'age': row['age']})

    conn.close()

    return jsonify(data_json)

# API endpoint to update data in the database
@app.route('/update_data/<int:id>', methods=['PUT'])
def update_data(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Extract data from JSON request
    data = request.json
    name = data['name']
    age = data['age']

    # Update data in the database
    cursor.execute('UPDATE Table1 SET name = ?, age = ? WHERE id = ?', (name, age, id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Data updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)
