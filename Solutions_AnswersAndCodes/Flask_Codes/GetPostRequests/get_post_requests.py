"""
    Question No. - 40:
    Explain how to set up a Flask application to handle form submissions using POST requests.
"""

# Import Required Modules from flask package, namely - Flask, request, render_template
from flask import Flask
from flask import request
from flask import render_template

# Flask Application Instance
app = Flask(__name__)

# Get and Post Request Route
@app.route('/submit-form', methods=['GET', 'POST'])

# View Function
def submit_form():
    
    # Check if the request method is POST
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')

# Run the application
if __name__ == "__main__":
    app.run(debug=True)


# Step-by-Step Process:-
"""
    Step 1: Import Required Modules
        The 'Flask', 'request' and 'render_template' modules are imported from the flask package.
        These are essential for creating the Flask application, handling HTTP requests, and rendering HTML templates.
    Step 2: Create Flask Application Instance
        An instance of the Flask application is created using 'app = Flask(__name__)'.
    Step 3: Define a route for the Form
        The '@app.route('/submit-form', methods=['GET', 'POST'])' decorator defines a route for the URL '/submit-form'.
        This route can handle both GET and POST requests.
    Step 4: View function
        The 'submit_form()' function is the view function that handles requests to the '/submit-form' route.
    Step 5: Check Request Method
        Inside the 'submit_form()' function, there's a check to determine if the request method is POST.
        If it is, the form data is processed.
    Step 6: Extract from Data
        The form data is extracted using 'request.form['name']'.
        This assumes that the form in 'form.html' contains an input field named name.
    Step 7: Return a Response
        If the request method is POST, the function returns a string "Hello, {name}!", where {name} is the value submitted in the form.
        If the request method is GET (i.e., when the form is first accessed), the 'form.html' template is rendered.
    Step 8: Run the Application:
        The 'if __name__ == "__main__"': block ensures that the application runs in debug mode when the script is executed directly.
"""