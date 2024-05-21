App structure :

lingua-franca/
│
├── app/                     # Folder containing the Flask application
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Defines the application's routes
│   ├── static/              # Contains static files (CSS, JS, ...)
│   │   ├── style.css        # CSS stylesheet
│   └── templates/           # Contains HTML templates
│       └── index.html       # Main page of the application
│
├── data/                    # Folder for generated data files
│   └── history.csv          # CSV file with translation history
│
├── picture/                 # Folder containing images displayed in the README 
├── translator/              # Folder containing the translation code
│   ├── __init__.py          # Initializes the translation module
│   └── google_translate.py  # Connects to Google's translation API
│
├── .gitignore               # Git file to ignore specific files/folders
├── README.md                # Project documentation
└── requirements.txt         # List of Python dependencies

