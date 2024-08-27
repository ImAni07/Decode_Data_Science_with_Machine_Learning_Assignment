# This is the {__init__.py} file
# This is essential for initiating a directory
# This directory consist of a Python Script named as {get_post_requests.py} and a relevant HTML Code File, named as {form.html}

# Author: Anirban Majumder
# Date: 26th August, 2024

# Here,
    # In this case,
    # The script of {__init__.py} consist of all the required codes and commands as well as the procedure to perform the asked task (Q.No.-48)

# The combined code has also been provided here:

"""
    Question No. - 48:
    How would you deploy a Flask application to a production server using Gunicorn and Nginx?
"""

"""
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
"""

"""
# run.py

# Import Necessary Module
from app import create_app

# Instance of App
app = create_app()

# Run the App
if __name__ == "__main__":
    app.run()
"""

# Gunicorn Service File: '/etc/systemd/system/flaskapp.service'

"""
[Unit]
Description=Gunicorn instance to serve Flask application
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/path/to/your/app
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind unix:flaskapp.sock -m 007 app:app

[Install]
WantedBy=multi-user.target
"""

# Nginx Configuration: '/etc/nginx/sites-available/flaskapp/

"""
server {
    listen 80;
    server_name your_domain_or_IP;

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/app/flaskapp.sock;
    }

    location /static/ {
        alias /path/to/your/app/static/;
    }
}
"""

# Step-by-Step Process to deploy a Flask Application to a production server using Gunicorn and Nginx

"""
    Deploying a Flask application to a production server using Gunicorn and Nginx involves several steps.
    
    Here's a comprehensive guide along with the relevant Python code and configuration files.
    
    Step 1: Create the Flask Application
        First, let's create a simple Flask application.
        
    Step 2: Install Required Packages
        The required packages for Flask, Gunicorn, and Nginx should be installed.
        Required Command:
            pip install flask gunicorn
            
    Step 3: Test the Flask Application Locally
        Before setting up Nginx, the Flask Application can be tested locally.
        Required Command:
            gunicorn --bind 0.0.0.0:8000 app:app
        Note: Gunicorn is primarily used on Unix-like systems.
        For a Windows environment, consider using a Windows-compatible WSGI server like waitress:
        Required Command:
            pip install waitress
            waitress-serve --listen=*:8000 app:app
            
    Step 4: Set Up Gunicorn as a Systemd Service
        Create a systemd service file for Gunicorn so that it runs in the background and starts on boot.
        Add the following content to the file:
            [Unit]
            Description=Gunicorn instance to serve Flask application
            After=network.target

            [Service]
            User=your_username
            Group=www-data
            WorkingDirectory=/path/to/your/app
            ExecStart=/usr/local/bin/gunicorn --workers 3 --bind unix:flaskapp.sock -m 007 app:app

            [Install]
            WantedBy=multi-user.target
            
    Step 5: Start and Enable the Gunicorn Service
        Check if Gunicorn is running.
        
    Step 6: Configure Nginx
        Now, configure Nginx to proxy requests to Gunicorn.
        Required Command:
            nano /c/Program Files/nginx-1.21.0/conf/nginx.conf

        Add the following configuration:
            server {
                listen 80;
                server_name your_domain_or_IP;

                location / {
                    include proxy_params;
                    proxy_pass http://unix:/path/to/your/app/flaskapp.sock;
                }

                location /static/ {
                    alias /path/to/your/app/static/;
                }
            }
    Step 7: Test Nginx Configuration and Restart Nginx
        After making changes, restart Nginx from GitBash
        Required Command:
            /c/Program Files/nginx-1.21.0/nginx.exe -s reload

    Step 8: Allow Nginx through the Firewall
        Required Command:
            netsh advfirewall firewall add rule name="Nginx" dir=in action=allow protocol=TCP localport=80

    Step 9: Verify the Deployment
        Run the Flask App
        python app.py
"""

# Structure:
# The structure of the project or app to be deployed using Gunicorn or Nginx is given below:

"""
    my_flask_app/
    ├── app/
    │   ├── __init__.py
    │   ├── routes.py
    │   └── ...
    ├── venv/
    ├── config.py
    ├── run.py
    └── requirements.txt
"""