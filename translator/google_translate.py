# Google Translation API connection code
from googletrans import Translator 

class GoogleTranslate: # Creation of the GoogleTranslate class
    def __init__(self): # Class initialization
        self.translator = Translator() # Creating an instance of the Translator class
    def translate(self, text, src='auto', dest='en'): # Definition of the translate method
        translation = self.translator.translate(text, src=src, dest=dest) # Text translation
        return translation.text # Returning the translated text

    def detect(self, text): # Definition of the detect method
        detection = self.translator.detect(text) # Text language detection
        return detection.lang # Return detected language