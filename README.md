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
- **scripts/** : Bash scripts
    - **install.sh** : Install project
        - Create virtual environment
        - Install dependencies
    - **run.sh** : Run server
        - Activate virtual environment
        - Run src/app.py
- **src/** : Source files
    - **templates/** : Contain HTML templates
        - **index.html** : The interface
    - **forms.py** : Contain TranlsationForm class
    - **translation.py** : Contain functions to connect to the translation API
    - **app.py** : Contain the Flask app, and routes
        - `index()` : Display the interface
        - `detect()` : Detect the language
        - `translate()` : Translate the text
    - **static/** : Static files dirs
        - **js/** : JavaScript modules
            - **constants.js** : Constants namespaces
                - `DomElements` : Namespace for usefull HTML Dom elements
                - `ApiRoutes` : Namespace for API routes
            - **utils.js** : Utility functions namespaces
                - `FormUtils` : Namespace for utility forms functions
                    - `updateFormFields(form, formData)` : Update the form with the FormData object
                    - `displayErrors(errors, defaultParentElement, errorMessageClass="error-message")` : Display the errors in the fields
                - `ImgUtils` : Namespace for utility images functions
                    - `displayIcon(element, src)` : Change src and display img
            - **ajaxFunctions.js** : AJAX functions namespace
                - `AjaxFunctions` : Namespace for AJAX calls
                    - `detectLanguage(formData)` : Send a POST request to detect-language/ API route
                    - `translate(formData)` : Send a POST request to translate/ API route
            - **script.js** : Main JS script
                - `submitTranslationForm()` : Submit the form to the backend and modify display with the response
                - `reverseLanguages()` : Reverse source and target languages and submit form
                - `EnableDisableReverseLanguages()` : Enable/disable reverse languages button
                - `addFormChangeListeners()` : Add listeners on form fields to submit form when a field is modified
                - `changeFlag(select)` : Change Flag icon
                - `init()` : Initialize event listeners and put navigator language in target language
            - **mapCountries.js** : Map languages and countries
                - `languageToCountryMap` : Object to map countries with languages
        - **css/** : CSS files
            - **normalize.css** : To normalize styles
            - **variables.css** : Variables (Colors ...)
            - **style.css** : Project style
        - **images/** : Images files
            - **status/** : Status images
                - **success.png** : Success image
                - **error.png** : Error image
                - **loading.png** : Loading image
            - **auto_language.png** : Flag icon for automatic detection language
            - **background.png** : Background image
            - **favicon.ico** : Icon
            - **reverse_languages.png** : Image for reverse languages button
  
