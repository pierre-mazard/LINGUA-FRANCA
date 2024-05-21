# Définition des routes de l'application
from flask import render_template, request # Ajout de la fonction request
from app import app # Import de l'application Flask
from translator.google_translate import GoogleTranslate # Import de la classe GoogleTranslate


@app.route('/', methods=['GET', 'POST']) # Ajout de la méthode POST
def index():  # Définition de la route index
    translator = GoogleTranslate() # Création d'une instance de la classe GoogleTranslate
    translation = '' # Initialisation de la variable translation
    if request.method == 'POST': # Ajout de la condition pour la méthode POST
        text_to_translate = request.form['text_to_translate'] # Récupération du texte à traduire
        source_language = request.form['source_language'] # Récupération de la langue source
        target_language = request.form['target_language'] # Récupération de la langue cible
        translation = translator.translate(text_to_translate, source_language, target_language) # Traduction du texte
    return render_template('index.html', translation=translation) # Renvoi du template index.html avec la variable translation
