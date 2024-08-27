# This is the {__init__.py} file
# This is essential for initiating a directory
# This directory consist of a Python Script named as {get_post_requests.py} and a relevant HTML Code File, named as {form.html}

# Author: Anirban Majumder
# Date: 26th August, 2024

# Here,
    # In this case,
    # The script of {__init__.py} consist of all the required codes and commands as well as the procedure to perform the asked task (Q.No.-49)

# The combined code has also been provided here:

"""
    Question No. - 49:
    Make a fully functional web application using flask, Mongodb, Signup, Signin page.
    After successful login, say "Hello Geeks" message at webpage.
"""

"""
# Import Necessary Modules
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from pymongo import MongoClient
import bcrypt

# Instance of Flask App
app = Flask(__name__)

# Configure Secret Key
app.secret_key = 'secretkey'

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/") 
db = client['flask_mongo_app']
users = db['users']

# App Route for Signup
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('welcome'))
        return 'Username already exists!'

    return render_template('signup.html')

# App Route for Signin
@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        login_user = users.find_one({'username': request.form['username']})
        if login_user:
            if bcrypt.checkpw(request.form['password'].encode('utf-8'), login_user['password']):
                session['username'] = request.form['username']
                return redirect(url_for('welcome'))
        return 'Invalid username/password combination'
    
    return render_template('signin.html')

# App Route for Welcome
@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f'Hello Geeks, {session["username"]}!'
    return redirect(url_for('signin'))

# App Route for Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
"""

# HTML Codes:

#Signup:
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign Up</title>
</head>
<body>
    <h2>Sign Up</h2>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Sign Up">
    </form>
    <p>Already have an account? <a href="{{ url_for('signin') }}">Sign In</a></p>
</body>
</html>
"""

# Signin:
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign In</title>
</head>
<body>
    <h2>Sign In</h2>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Sign In">
    </form>
    <p>Don't have an account? <a href="{{ url_for('signup') }}">Sign Up</a></p>
</body>
</html>
"""

# Welcome:
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
</head>
<body>
    <h2>{{ message }}</h2>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
"""

# Structure:
"""
    flask_mongo_app/
    ├── app.py
    ├── templates/
    │   ├── signup.html
    │   ├── signin.html
    │   └── welcome.html
    ├── static/
    │   └── style.css
    ├── venv/
    └── requirements.txt
"""

# Prerequisites:
"""
    Python installed on your machine.
    MongoDB installed and running on your local machine or accessible via a cloud service like MongoDB Atlas.
    Basic knowledge of Python, Flask, HTML, and MongoDB.
"""

# Step-by-Step Process:
"""
    Step 1: Project Setup
        Organize the project files and setup a virtual environment (recommended, for ease of handling the tasks).
    
    Step 2: Create a Virtual Environment (Optional)
        Navigate to the Project directory and create a virtual environment.
        Required Command:
            cd flask_mongo_app
            python3 -m venv venv
            source venv/bin/activate            # For Windows use `venv\Scripts\activate`
    
    Step 3: Install Required Packages
        Install Flask, PyMongo, and other necessary packages:
        Required Command:
            pip install flask pymongo
    
    Step 4: Setup MongoDB
        If using a local MongoDB server, ensure it's running.
        If using MongoDB Atlas, set up the cluster and get the connection string.
    
    Step 5: Create the Flask Application
        Write relevant code in Python.
    
    Step 6: Connect to MongoDB
        Connect the Flask App to MongoDB
    
    Step 7: Create the HTML Templates
        Create 'welcome.html', 'signup.html' and 'signin.html'.
    
    Step 8: Run the Flask Application
        With everything set up, run your Flask application:
        Required Command:
            python app.py
    
    Step 9: Access the Application
        Open the browser and go to 'http://127.0.0.1:5000/signup' to create a new account.
        After signing up, you should be redirected to the welcome page.
        Log out and sign in again at 'http://127.0.0.1:5000/signin'.
        Test:- Ensure everything works correctly by testing the signup and signin process.
    
    Step 10: Deploy to Production (Optional)
        Optionally, deploy to a production server.
        One can follow the Gunicorn and Nginx steps
"""