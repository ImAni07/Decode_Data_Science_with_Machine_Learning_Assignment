# This is the {__init__.py} file
# This is essential for initiating a directory
# This directory consist of a Python Script named as {get_post_requests.py} and a relevant HTML Code File, named as {form.html}

# Author: Anirban Majumder
# Date: 26th August, 2024

# The combined code has also been provided here:

# The Python Script

"""
    Question No. - 45:
    Explain how to use Flask-WTF to create and validate forms in a Flask application.
"""

"""
# Import Necessary Modules
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

# Flask App Instance
app = Flask(__name__)

# Secret Key Configuration
app.secret_key = 'secret_key'

# Form definition
class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# App Route
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        return f"Hello, {name}!"
    return render_template('form.html', form=form)

# Run the Application
if __name__ == "__main__":
    app.run(debug=True)
"""

# HTML Code
"""
<!DOCTYPE html>
<html>
<head>
    <title>Form Submission</title>
</head>
<body>
    <h1>Form Submission</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

# Step-by-Step Process:-
"""
    Step 1: Import necessary modules, including 'Flask', 'FlaskForm' and form fields from 'Flask-WTF'.
    Step 2: Create a Flask application instance and configure a secret key.
    Step 3: Define a form class that inherits from 'FlaskForm'.
    Step 4: Create a view function to render the form and handle form submission.
    Step 5: Validate form data on submission.
"""