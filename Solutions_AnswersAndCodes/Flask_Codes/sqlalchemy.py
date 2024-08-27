"""
    Question No. - 43
    Describe the process of connecting a Flask app to a SQLite database using SQLAlchemy.
"""

# Import Necessary Modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask Application Instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Model definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Creating tables
with app.app_context():
    db.create_all()

# Create Route for the Application
@app.route('/')
def index():
    user = User(username='John Doe')
    db.session.add(user)
    db.session.commit()
    return f"User {user.username} added to the database!"

# Run the Application
if __name__ == "__main__":
    app.run(debug=True)

# Step-by-Step Process:-
"""
    Step 1: Import necessary modules, including 'Flask' and 'SQLAlchemy'.
    Step 2: Create a Flask application instance and configure the SQLite database URI.
    Step 3: Create a 'SQLAlchemy' instance.
    Step 4: Define models representing the database tables.
    Step 5: Create and query database entries using the models.
    Step 6: Run the application.
"""