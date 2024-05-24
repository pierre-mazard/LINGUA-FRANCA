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
    - **forms.py** : Contain TranlsationForm class
    - **translation.py** : Contain functions to connect to the translation API
    - **app.py** : Contain the Flask app, and routes
        - `index()` : Display the interface
        - `detect()` : Detect the language
        - `translate()` : Translate the text

        - **images/** : Images files
            - **status/** : Status images
                - **success.png** : Success image
                - **error.png** : Error image
                - **loading.png** : Loading image
            - **auto_language.png** : Flag icon for automatic detection language
            - **background.png** : Background image
            - **favicon.ico** : Icon
            - **reverse_languages.png** : Image for reverse languages button
  
