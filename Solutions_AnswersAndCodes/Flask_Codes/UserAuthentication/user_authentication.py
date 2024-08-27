"""
    Question No. - 42:
    How can you implement user authentication in a Flask application?
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