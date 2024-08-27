# app.py

# Import Necessary Modules 
from flask import Flask 
from flask import jsonify

# Flask App Instance
app = Flask(__name__)

# Defining the App Route
@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask Application!")

@app.route('/hello/<name>')
def hello(name):
    return jsonify(message=f"Hello, {name}!")

# Run the App
if __name__ == '__main__':
    app.run()