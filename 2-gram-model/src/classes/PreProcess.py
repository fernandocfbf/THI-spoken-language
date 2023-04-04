#external libraries
import string

#constants
from src.constants.preprocess import USELESS_WORDS, NORMALIZATION_RULES, STOP_WORDS

class PreProcess():
    
    def remove_punctuation(self, text):
        text_transformed = text.translate(str.maketrans('', '', string.punctuation))
        text = text_transformed
        return text

    def remove_useless_information(self, text):
        for useless_word in USELESS_WORDS:
            text.replace(useless_word, '')
        text = text.translate(str.maketrans('', '', string.digits))
        return text

    def remove_stop_words(self, text):
        words = text.split()
        filtered_words = [word for word in words if word.lower() not in STOP_WORDS]
        filtered_text = " ".join(filtered_words)

    def lemmatize_word(word):
        for suffix, replacement in NORMALIZATION_RULES.items():
            if word.endswith(suffix):
                word = word[:-len(suffix)] + replacement
                break
        return word
    
