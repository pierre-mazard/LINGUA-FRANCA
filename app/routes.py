# Defining application routes
from flask import render_template, request, session, send_file, redirect, url_for, make_response
from app import app
from translator.google_translate import GoogleTranslate
import csv
import os
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    translator = GoogleTranslate()
    translation = ''
    text_to_translate = ''
    if 'translations' not in session:
        session['translations'] = []
    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        source_language = request.form['source_language']
        target_language = request.form['target_language']
        translation = translator.translate(text_to_translate, source_language, target_language)
        # Store the translation in the session with the current time and languages
        session['translations'].append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), source_language, target_language, text_to_translate, translation))
        session.modified = True
    return render_template('index.html', translation=translation, text_to_translate=text_to_translate, translations=session['translations'])

@app.route('/save_history', methods=['POST'])
def save_history():
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
def clear_history():
    # Clear the session
    session['translations'] = []

    # Redirect to the index page
    return redirect(url_for('index'))