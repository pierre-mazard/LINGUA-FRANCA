# Initializing the Flask application and its routes

from flask import Flask # Import the Flask class
from flask_babel import Babel # Import the Babel extension

app = Flask(__name__) # Initialize the Flask application
babel = Babel(app) # Initialize the Babel extension

# Set the secret key
app.secret_key = 'your-secret-key'  # Change this to your secret key

from . import routes  # Move this line to the end
