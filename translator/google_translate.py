# Google Translation API connection code
from googletrans import Translator 

class GoogleTranslate: # Creation of the GoogleTranslate class
    def __init__(self): # Class initialization
        self.translator = Translator() # Creating an instance of the Translator class
    
    def translate(self, text, src='auto', dest='en'):
        if src == 'binary':
            text = self.binary_to_text(text)
            src = 'auto'  # Set source language to 'auto' after converting from binary
        if dest == 'binary':
            return self.text_to_binary(text)
        else:
            translation = self.translator.translate(text, src=src, dest=dest)
            return translation.text
   
    def detect(self, text):
        if set(text) <= {'0', '1'}:
            return 'binary'
        else:
            detection = self.translator.detect(text)
            return detection.lang


    
    def text_to_binary(self, text):
        return ' '.join(format(ord(char), '08b') for char in text)

    def binary_to_text(self, binary):
        binary_values = binary.split(' ')
        ascii_string = ''.join([chr(int(binary_value, 2)) for binary_value in binary_values])
        return ascii_string