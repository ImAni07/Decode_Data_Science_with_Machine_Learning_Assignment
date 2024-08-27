"""
    Question No. - 44:
    How would you create a RESTful API endpoint in Flask that returns JSON data?
"""

# Import Necessary Modules
from flask import Flask
from flask import jsonify

# Instance of Flask App
app = Flask(__name__)

# Route serving as API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'name': 'Anirban Majumder', 'age': 24, 'city': 'Kolkata'}
    return jsonify(data)

# Run the Application
if __name__ == "__main__":
    app.run(debug=True)

# Step-by-Step Process:-
"""
    Step 1: Import 'Flask' and 'jsonify' from the 'flask' module.
    Step 2: Create a Flask application instance.
    Step 3: Define a route that will serve as the API endpoint.
    Step 4: Create a view function that returns JSON data using 'jsonify'.
    Step 5: Run the application.
"""