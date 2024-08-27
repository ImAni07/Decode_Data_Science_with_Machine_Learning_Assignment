# run.py

# Import Necessary Module
from app import create_app

# Instance of App
app = create_app()

# Run the App
if __name__ == "__main__":
    app.run()