# Code de connection à l'API de traduction de Google

from googletrans import Translator 

class GoogleTranslate: # Création de la classe GoogleTranslate
    def __init__(self): # Initialisation de la classe
        self.translator = Translator() # Création d'une instance de la classe Translator

    def translate(self, text, src='auto', dest='en'): # Définition de la méthode translate
        translation = self.translator.translate(text, src=src, dest=dest) # Traduction du texte
        return translation.text # Renvoi du texte traduit

    def detect(self, text): # Définition de la méthode detect
        detection = self.translator.detect(text) # Détection de la langue du texte
        return detection.lang # Renvoi de la langue détectée
