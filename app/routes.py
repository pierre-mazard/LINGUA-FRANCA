# Defining application routes
from flask import render_template, request, session, send_file, redirect, url_for, make_response, send_from_directory
from app import app
from translator.google_translate import GoogleTranslate
import csv
import os
from datetime import datetime
from app.static.analytics.analysis import analyze_translations

if not os.path.isdir('data/'): # Check if the 'data/' directory exists
    print("The 'data/' directory does not exist")


@app.route('/', methods=['GET', 'POST'])
# Function to render the index template
def index(): 
    translator = GoogleTranslate() 
    translation = '' 
    text_to_translate = '' 
    history_text = ''  # New variable for the original text
    history_translation = ''  # new variable for the translation of the history
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

# Get the absolute path of the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Use the absolute path to access the data directory
data_dir = os.path.join(script_dir, '../data')

@app.route('/analytics', methods=['GET'])
# Function to render the analytics template
def analytics():
    # Call the function with the path to your data directory
    analyze_translations(data_dir)
    return render_template('analytics.html')

@app.route('/analytics/image')
# Function to serve the image
def analytics_image():
    # Return the image from the 'app/static/analytics' directory
    return send_from_directory('app/static/analytics', 'translation_analysis.png')