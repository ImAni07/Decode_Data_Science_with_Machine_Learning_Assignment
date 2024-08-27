# This is {__init__.py} Python Script

# Author: Anirban Majumder
# Date: 26th August, 2024

# This file can remain empty, but it is essential to initialize a directory

"""
    Question No. 42:
    How can you implement user authentication in a Flask application?
"""

# Python Script Code:

"""

# Import Required Modules
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user

# Flask Application Instance
app = Flask(__name__)

# User Class for Authentication Methods
app.secret_key = 'secret_key'

# Instance of 'LogInManager
login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Route for LogIn Method
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User(user_id)
        login_user(user)
        return redirect(url_for('protected'))
    return render_template('login.html')

# Route for Protected Method
@app.route('/protected')
@login_required
def protected():
    return f"Hello, {current_user.id}!"

# Route for LogOut Method
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Run the Application
if __name__ == "__main__":
    app.run(debug=True)
"""

# HTML Code:-

"""
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h1>Login</h1>
    <form action="" method="post">
        <label for="user_id">User ID:</label>
        <input type="text" id="user_id" name="user_id" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

# Step-by-Step Process:-
"""
    Step1: Import necessary modules, including 'Flask', 'Flask-Login' and 'LoginManager'.
    Step2: Create a user class that implements user authentication methods.
    Step3: Set up a 'LoginManager' instance and configure it.
    Step4: Create routes for login, logout, and protected views.
    Step5: Implement login and logout logic.
    Step6: Use 'login_required' decorator to protect routes.
"""