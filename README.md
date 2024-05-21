Structure :

lingua-franca/
│
├── app/                     # Dossier contenant l'application Flask
│   ├── __init__.py          # Initialise l'application Flask
│   ├── routes.py            # Définit les routes de l'application
│   ├── static/              # Contient les fichiers statiques (CSS, JS, ...)
│   │   ├── style.css        # Feuille de style CSS
│   └── templates/           # Contient les modèles HTML
│       └── index.html       # Page principale de l'application
│
├── translator/              # Dossier contenant le code de traduction
│   ├── __init__.py          # Initialise le module de traduction
│   └── google_translate.py  # Se connecte à l'API de traduction de Google
│
├── .gitignore               # Fichier Git pour ignorer les fichiers/dossiers spécifiques
├── README.md                # Documentation du projet
└── requirements.txt         # Liste des dépendances Python
