import os
import subprocess

# Cloner le repository
subprocess.run(["git", "clone", "https://github.com/pierre-mazard/LINGUA-FRANCA.git"])

# Naviguer dans le répertoire du projet
os.chdir("LINGUA-FRANCA")

# Installer les dépendances Python
subprocess.run(["pip", "install", "-r", "requirements.txt"])
