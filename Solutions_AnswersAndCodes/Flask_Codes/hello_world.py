"""
    Question No. - 39:
    How would you create a basic Flask route that displays "Hello, World!" on the homepage?
"""
# Import Required Module
from flask import Flask

# Flask Application Instance
app = Flask(__name__)

# Defining Route
@app.route('/')

# Creation of a view function
def hello_world():
    return "Hello, World!"

# Running the application
if __name__ == "__main__":
    app.run(debug=True)

# Step-by-Step Process:-
"""
    Step 1: Import Flask from the flask module.
    Step 2: Create a Flask application instance.
    Step 3: Define a route for the homepage using the '@app.route()' decorator.
    Step 4: Create a view function that returns "Hello, World!".
    Step 5: Run the Flask application.
"""