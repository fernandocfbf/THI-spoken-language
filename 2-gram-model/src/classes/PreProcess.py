#external libraries
import string

#constants
from src.constants.preprocess import USELESS_WORDS

class PreProcess():

    def __init__(self, text):
        self.text = text
    
    def remove_punctuation(self):
        text_transformed = self.text.translate(str.maketrans('', '', string.punctuation))
        self.text = text_transformed

    def remove_useless_information(self):
        for useless_word in USELESS_WORDS:
            self.text.replace(useless_word, '')
        self.text = self.text.translate(str.maketrans('', '', string.digits))