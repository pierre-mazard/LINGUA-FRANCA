# routes.py
from flask import render_template, request, session, redirect, url_for, send_from_directory
from app import app
from translator.google_translate import GoogleTranslate
import csv
import os
from datetime import datetime
from analytics.analysis import analyze_translations

# Ensure 'data/' directory exists
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '../data')
if not os.path.isdir(data_dir):
    os.makedirs(data_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
    translator = GoogleTranslate()
    translation = ''
    text_to_translate = ''
    history_text = ''
    history_translation = ''
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
        session['translations'].append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), source_language, target_language, history_text, history_translation))
        session.modified = True
    return render_template('index.html', translation=translation, text_to_translate=text_to_translate, translations=session['translations'])

@app.route('/save_history', methods=['POST'])
def save_history():
    if not session['translations']:
        return redirect(url_for('index'))
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(data_dir, date_time + '_history.csv')
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Source Language", "Target Language", "Original Text", "Translated Text"])
        writer.writerows(session['translations'])
    session['translations'] = []
    return redirect(url_for('index'))

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['translations'] = []
    return redirect(url_for('index'))

@app.route('/analytics', methods=['GET'])
def analytics():
    analyze_translations(data_dir)
    stats_path = os.path.join(data_dir, 'translation_stats.txt')
    with open(stats_path, 'r') as f:
        stats_data = f.read()
        source_languages = stats_data.split('\n\n')[0]
        target_languages = stats_data.split('\n\n')[1]
        translation_length_stats = stats_data.split('\n\n')[2]
        translation_time_stats = stats_data.split('\n\n')[3]
    return render_template('analytics.html', source_languages=source_languages, target_languages=target_languages, translation_length_stats=translation_length_stats, translation_time_stats=translation_time_stats)

@app.route('/analytics/image')
def analytics_image():
    return send_from_directory('../data', 'translation_analysis.png')
