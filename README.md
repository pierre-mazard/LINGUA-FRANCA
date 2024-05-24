App structure :

lingua-franca/ 
│
├── app/
│   ├── __init__.py
│   ├── routes.py           
│   ├── static/
│   │   ├── style.css
│   │   └── analytics/       
│   │       └── analysis.py  
│   └── templates/
│       ├── index.html       
│       └── analytics.html  
├── data/
│   └── history.csv
│
├── translator/
│   ├── __init__.py
│   └── google_translate.py
│
├── .gitignore
├── README.md
└── requirements.txt

# lingua-franca
Translator Flask app using Google Translate API

## Table of content
- [lingua-franca](#lingua-franca)
  - [Table of content](#table-of-content)
  - [Getting started](#getting-started)
    - [Install](#install)
    - [Use](#use)
  - [Project files](#project-files)

## Getting started
### Install
<!-- a faire -->
### Use
<!-- à faire -->

## Project files
- **README.md** : Project details (this file)

- **.gitignore** : Files ignored by Git

- **requirements.txt** : Project dependencies

- **analytics/** : Bash scripts
    - **analysis.py** : Transform data
        - Into visual graphs
        - Into a text format
- **app/** : Source files
    - **static/** : Static files dirs
        - **style.css** : Project style
    - **templates/** : Contain HTML templates
        - **index.html** : The interface
    - **routes.py** : Tell where the file should be stored
- **data/** : Data storage 
    - **history.csv** : cvs file where the data is stored
    - **translation_analysis.png** : png of the multiple graphs based on the data collected
    - **translation_stats.txt** : Text file based on the data collected
    - **translation.py** : Contain functions to connect to the translation API
- **translator/** : This is where the translation happens
    - **google_translate.py** : Detect the language, translate the text
