# This is the {__init__.py} file
# This is essential for initiating a directory
# This directory consist of a Python Script named as {get_post_requests.py} and a relevant HTML Code File, named as {form.html}

# Author: Anirban Majumder
# Date: 26th August, 2024

# The combined code has also been provided here:

# The Python Script

"""
    Question No. - 46:
    How can you implement file uploads in a Flask application?
"""

"""
# Import Necessary Modules
import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for

# Instance of Flask App
app = Flask(__name__)

# Configuring file uploader
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Defining Route
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File successfully uploaded'
    return render_template('upload.html')

# Run the Application
if __name__ == "__main__":
    app.run(debug=True)
"""

# HTML Code:

"""
<!DOCTYPE html>
<html>
<head>
    <title>Upload File</title>
</head>
<body>
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
"""

# Step-by-Step Process:-
"""
    Step 1: Import 'Flask' and 'request' from the 'flask' module.
    Step 2: Create a Flask application instance and configure the upload folder.
    Step 3: Define a route to handle file uploads.
    Step 4: In the view function, check if the file is in the request and save it.
    Step 5: Provide feedback to the user upon successful upload.
"""