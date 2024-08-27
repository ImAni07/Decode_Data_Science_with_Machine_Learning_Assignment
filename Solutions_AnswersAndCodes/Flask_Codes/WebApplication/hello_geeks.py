"""
    Question No. - 49:
    Make a fully functional web application using flask, Mongodb, Signup, Signin page.
    After successful login, say "Hello Geeks" message at webpage.
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