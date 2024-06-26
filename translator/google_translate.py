# Google Translation API connection code
from googletrans import Translator 

class GoogleTranslate: 
    # Constructor
    def __init__(self):
        self.translator = Translator() 
    
    # Function to translate text
    def translate(self, text, src='auto', dest='en'):
        if src == 'binary' or (src == 'auto' and self.detect(text) == 'binary'):
            text = self.binary_to_text(text)
            src = 'auto'  # Set source language to 'auto' after converting from binary
        if dest == 'binary':
            return self.text_to_binary(text)
        else:
            translation = self.translator.translate(text, src=src, dest=dest)
            return translation.text

   # Function to detect the language of the text
    def detect(self, text):
        binary_chars = {'0', '1', ' '}
        if set(text) <= binary_chars:
            # Split the text by spaces and check if each part is a valid binary number
            parts = text.split()
            if all(len(part) == 8 and set(part) <= {'0', '1'} for part in parts):
                return 'binary'
        detection = self.translator.detect(text)
        return detection.lang

    # Function to convert text to binary
    def text_to_binary(self, text):
        return ' '.join(format(ord(char), '08b') for char in text)

    # Function to convert binary to text
    def binary_to_text(self, binary):
        binary_values = binary.split(' ')
        ascii_string = ''.join([chr(int(binary_value, 2)) for binary_value in binary_values])
        return ascii_string