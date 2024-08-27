"""
    Question No. - 47:
    Describe the steps to create a Flask blueprint and why you might use one.
"""

# Import Necessary Modules
from flask import Flask
from Flask import Blueprint

# Instance of Flask App
app = Flask(__name__)

# Blueprint definition
simple_page = Blueprint('simple_page', __name__)

# App Route for Blueprint
@simple_page.route('/blueprint')
def show():
    return "This is a blueprint route!"

# Registering the blueprint
app.register_blueprint(simple_page)

# Running the Application
if __name__ == "__main__":
    app.run(debug=True)

# Step-by-Step Process:-
"""
    Step 1: Import 'Flask' and 'Blueprint' from the flask module.
    Step 2: Create a Flask application instance.
    Step 3: Define a blueprint and associated routes.
    Step 4: Register the blueprint with the main application.
    Step 5: Use blueprints to organize and modularize your application, making it easier to manage large projects.
"""

# Reason of using Blueprint:-
"""
    A Flask Blueprint is a way to organize and modularize Flask application, especially when it becomes large and complex.
    By using blueprints, one can group related routes, views, and other code into a single, cohesive module.
    This helps in maintaining clean code, reduces redundancy, and makes it easier to collaborate on large projects.
    
    Here's why one might use Flask Blueprint:
    1. Modularization:
        It allows to break down the application into smaller, manageable parts, each with its own routes, templates, and static files.
    2. Reusability:
        Blueprints can be reused across different applications or projects, making it easier to maintain consistency and save time.
    3. Organization:
        With blueprints, one can organize one's routes and views by functionality, keeping related code together.
        This improves readability and makes it easier to navigate your codebase.
    4. Separation of Concerns:
        Blueprints help to keep different concerns separated, such as -
                                                                        user authentication,
                                                                        admin panel, and
                                                                        public-facing routes,
        which can all be handled by different blueprints.
    5. Collaboration:
        In a team environment, different developers can work on different parts of the application (each as a separate blueprint)
        without stepping on each other’s toes.
        
        In summary, using blueprints in a Flask application enhances the maintainability, scalability, and clarity of the codebase.
"""