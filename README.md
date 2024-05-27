# Lingua-Franca

This repository contains the Lingua-Franca project, a language translation application using an API with the ability to analyze translation history data.

## Table of Contents

1. [Directory Structure](#directory-structure)
2. [Getting Started](#getting-started)
    - [Install](#install)
    - [Use](#use)
3. [Translation Capabilities](#translation-capabilities)
4. [Translation History](#translation-history)
5. [Adding Additional Languages](#adding-additional-languages)

## Directory Structure

- **analytics/**: Contains the files related to data analysis.
  - `analysis.py`: Python script for analyzing translation data.
  - `__pycache__/`: Cache directory for Python bytecode (automatically generated).

- **app/**: Contains the main application files.
  - `__init__.py`: Initialization script for the Flask application.
  - `routes.py`: Defines the URL routes and request handling logic.
  - **static/**: Contains static files for the Flask application.
    - `style.css`: CSS file for styling HTML templates.
  - **templates/**: Contains HTML templates for the Flask application.
    - `analytics.html`: HTML template for displaying analytics results.
    - `index.html`: HTML template for the main application interface.

- **data/**: Contains data files generated and used by the application.
  - `translation_analysis.png`: Image file for visualizing translation analysis.
  - `translation_stats.txt`: Text file containing statistics from translation analysis.
  - `translation_history.csv`: CSV file storing the history of translations.

- **translator/**: Contains files related to the translation functionality.
  - `__init__.py`: Initialization script for the translator module.
  - `google_translate.py`: Python script for Google Translation API integration.
  - `__pycache__/`: Cache directory for Python bytecode (automatically generated).

- **README.md**: This file, containing information about the project and its structure.
- **requirements.txt**: File listing the Python dependencies required to run the project.
- **.gitignore**: File specifying which files and directories to ignore in version control.


## Getting Started

To get started with Lingua-Franca, follow the installation instructions below and then learn how to use the application.

### Install

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/pierre-mazard/LINGUA-FRANCA.git

2. Navigate into the project directory.
    ```bash
    cd Lingua-Franca

3. Instal the required Python dependencies using pip.
    ```bash
    pip install -r requirements.txt

## Use

1. After installing dependencies, start the Flask application.
    ```bash
    flask run

2. Open your web browser and navigate to http://localhost:5000 to access the Lingue-Franca application.

3. Enter the text you want to translate, select the source and target languages, and click "Translate".

4. View the translated text and explore the application's features, including translation history and analytics.

## Translation Capabilities

The Lingua-Franca application allows users to translate text into various languages, including binary. This means users can translate text into human-readable languages like French, English, Spanish, etc., as well as binary code.


## Translation History

The translation history data is stored in the translation_history.csv file. This file contains records of past translations, including the date and time, source language, target language, original text, and translated text.

## Adding Additional Languages
To add more languages to the translat
ion options in the application, you can modify the index.html file located in the templates directory. Within the `<select>` elements for source and target languages, you can add new `<option>` elements for additional languages. Ensure that the value attribute of each `<option>` corresponds to the language code recognized by the translation API.

Ensure that the new languages added in the HTML file are supported by the translation API you are using.

```html
 <select name="source_language">
                    <option value="auto">Automatic detection</option>
                    <option value="fr">French</option>
                    <option value="en">English</option>
                    <option value="es">Spanish</option>
                    <option value="de">German</option>
                    <option value="it">Italian</option>
                    <option value="pt">Portuguese</option>
                    <option value="ru">Russian</option>
                    <option value="ja">Japanese</option>
                    <option value="ko">Korean</option>
                    <option value="ar">Arabic</option>
                    <option value="binary">Binary</option> 
                    <!-- add other languages ​​here -->
                </select>
                <select name="target_language">
                    <option value="fr">French</option>
                    <option value="en">English</option>
                    <option value="es">Spanish</option>
                    <option value="de">German</option>
                    <option value="it">Italian</option>
                    <option value="pt">Portuguese</option>
                    <option value="ru">Russian</option>
                    <option value="ja">Japanese</option>
                    <option value="ko">Korean</option>
                    <option value="ar">Arabic</option>
                    <option value="binary">Binary</option> 
                    <!-- add other languages ​​here -->
                </select>                
```

[Back to Top](#lingua-franca)