# Lingua-Franca

This repository contains the Lingua-Franca project, a language translation application using an API with the ability to analyze translation history data.

## Table of Contents

1. [Directory Structure](#directory-structure)
2. [Getting Started](#getting-started)
    - [Install](#install)
    - [Use](#use)

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


[Back to Top](#lingua-franca)