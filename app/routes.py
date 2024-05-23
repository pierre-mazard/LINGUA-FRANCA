# routes.py
from flask import render_template, request, session, redirect, url_for, send_from_directory
from app import app
from translator.google_translate import GoogleTranslate
import csv
import os
from datetime import datetime
from app.static.analytics.analysis import analyze_translations

if not os.path.isdir('data/'): # Check if the 'data/' directory exists
    print("The 'data/' directory does not exist")

# Obtenez le chemin d'accès absolu du répertoire du script actuel
script_dir = os.path.dirname(os.path.abspath(__file__))
# Utilisez le chemin d'accès absolu pour accéder au répertoire de données
data_dir = os.path.join(script_dir, '../data')

@app.route('/', methods=['GET', 'POST'])
# Function to render the index template
def index(): 
    translator = GoogleTranslate() 
    translation = '' 
    text_to_translate = '' 
    history_text = ''  # New variable for the original text
    history_translation = ''  # New variable for the translation of the history
    if 'translations' not in session: 
        session['translations'] = []
    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        source_language = request.form['source_language']
        target_language = request.form['target_language']
        if text_to_translate.strip() == '':
            history_text = 'empty text field'
            history_translation = 'empty text field'
        else:
            translation = translator.translate(text_to_translate, source_language, target_language)
            history_text = text_to_translate
            history_translation = translation
        # Store the translation in the session with the current time and languages
        session['translations'].append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), source_language, target_language, history_text, history_translation))
        session.modified = True
    return render_template('index.html', translation=translation, text_to_translate=text_to_translate, translations=session['translations'])

@app.route('/save_history', methods=['POST']) 
# Function to save the history
def save_history():
    # Check if the session is empty
    if not session['translations']:
        # If the session is empty, redirect to the index page
        return redirect(url_for('index'))

    # Get the current date and time
    now = datetime.now()

    # Format the date and time
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Create the filename
    filename = 'data/' + date_time + '_history.csv'

    # Write the translations to the file
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Source Language", "Target Language", "Original Text", "Translated Text"])
        writer.writerows(session['translations'])

    # After writing to the file, clear the session
    session['translations'] = []

    # Redirect to the index page
    return redirect(url_for('index'))


@app.route('/clear_history', methods=['POST'])
# Function to clear the history
def clear_history():
    # Clear the session
    session['translations'] = []

    # Redirect to the index page
    return redirect(url_for('index'))

@app.route('/analytics', methods=['GET'])
# Function to render the analytics template
def analytics():
    # Call the function with the path to your data directory
    analyze_translations(data_dir)
    
    # Obtenir le chemin d'accès absolu pour le fichier de statistiques
    stats_path = os.path.join(data_dir, 'translation_stats.txt')
    with open(stats_path, 'r') as f:
        # Lire les statistiques à partir du fichier
        stats_data = f.read()
        source_languages = stats_data.split('\n\n')[0]
        target_languages = stats_data.split('\n\n')[1]
        translation_length_stats = stats_data.split('\n\n')[2]
        translation_time_stats = stats_data.split('\n\n')[3]

    return render_template('analytics.html', 
                           source_languages=source_languages,
                           target_languages=target_languages,
                           translation_length_stats=translation_length_stats,
                           translation_time_stats=translation_time_stats)

@app.route('/analytics/image')
# Function to serve the image
def analytics_image():
    # Return the image from the 'data' directory
    return send_from_directory('../data', 'translation_analysis.png')
