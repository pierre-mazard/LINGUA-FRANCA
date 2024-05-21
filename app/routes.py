# Defining application routes
from flask import render_template, request # Added request function
from app import app # Import from the Flask application
from translator.google_translate import GoogleTranslate # Importing the GoogleTranslate class

@app.route('/', methods=['GET', 'POST']) # Added POST method
def index():  # Setting the index route
    translator = GoogleTranslate() # Creating an instance of the GoogleTranslate class
    translation = '' # Initialization of the translation variable
    text_to_translate = '' # Initialization of the text_to_translate variable
    if request.method == 'POST': # Added condition for POST method
        text_to_translate = request.form['text_to_translate'] # Recovery of the text to translate
        source_language = request.form['source_language'] # Source language recovery
        target_language = request.form['target_language'] # Target language recovery
        translation = translator.translate(text_to_translate, source_language, target_language) # Target language recovery
    return render_template('index.html', translation=translation, text_to_translate=text_to_translate) # Returning the index.html template with the translation and text_to_translate variables
