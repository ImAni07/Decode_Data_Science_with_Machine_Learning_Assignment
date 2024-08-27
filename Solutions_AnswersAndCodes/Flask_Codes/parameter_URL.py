"""
    Question No. - 41:
    Write a Flask route that accepts a parameter in the URL and displays it on the page.
"""

# Import Required Module
from flask import Flask

# Instance of Flask Application
app = Flask(__name__)

# Route including parameter
@app.route('/user/<username>')

# View Function
def show_user_profile(username):
    return f"Hello, {username}!"

# Run the Application
if __name__ == "__main__":
    app.run(debug=True)

# Step-by-Step Process:-
"""
    Step 1: Import Flask from the flask module.
    Step 2: Create a Flask application instance.
    Step 3: Define a route that includes a parameter in the URL using <parameter>.
    Step 4: Create a view function that accepts the parameter as an argument.
    Step 5: Return the parameter as part of the response.
"""