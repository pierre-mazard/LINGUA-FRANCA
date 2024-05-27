# routes.py
import glob
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

    # Ensure 'data/' directory exists
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    filename = os.path.join(data_dir, 'translations_history.csv')
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if os.path.getsize(filename) == 0:  # Write header if file is empty
            writer.writerow(["Time", "Source Language", "Target Language", "Original Text", "Translated Text"])
        writer.writerows(session['translations'])
    
    session['translations'] = []
    return redirect(url_for('index'))


@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['translations'] = []
    return redirect(url_for('index'))

@app.route('/clear_csv', methods=['POST'])
def clear_csv():
    filenames = glob.glob(os.path.join(data_dir, '*.csv'))
    for filename in filenames:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Time", "Source Language", "Target Language", "Original Text", "Translated Text"])
    return redirect(url_for('index'))

@app.route('/analytics', methods=['GET'])
def analytics():
    analyze_translations(data_dir)
    stats_path = os.path.join(data_dir, 'translation_stats.txt')
    with open(stats_path, 'r') as f:
        stats_data = f.read()
    if "No data available" in stats_data:
        return render_template('analytics.html', no_data=True)
    else:
        sections = stats_data.split('\n\n')
        source_languages = sections[0] if len(sections) > 0 else "No data available"
        target_languages = sections[1] if len(sections) > 1 else "No data available"
        translation_length_stats = sections[2] if len(sections) > 2 else "No data available"
        translation_time_stats = sections[3] if len(sections) > 3 else "No data available"
        return render_template('analytics.html', no_data=False, source_languages=source_languages, target_languages=target_languages, translation_length_stats=translation_length_stats, translation_time_stats=translation_time_stats)

@app.route('/analytics/image')
def analytics_image():
    return send_from_directory('../data', 'translation_analysis.png')
