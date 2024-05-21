# Initialisation de l'application Flask et de ses routes

from flask import Flask # Import de la classe Flask
app = Flask(__name__)  # Initialisation de l'application Flask
from app import routes # Import des routes de l'application