#external libraries
import string

#constants
from src.constants.preprocess import NORMALIZATION_RULES, STOP_WORDS

class PreProcess():

    def lower_case(self, text):
        return text.lower()
    
    def remove_punctuation(self, text):
        text_transformed = text.translate(str.maketrans('', '', string.punctuation))
        text = text_transformed
        return text

    def remove_stop_words(self, text):
        words = text.split()
        filtered_words = [word for word in words if word.lower() not in STOP_WORDS]
        filtered_text = " ".join(filtered_words)
        return filtered_text
    
    def remove_numbers(self, text):
        words = text.split()
        filtered_words = [word for word in words if not word.isdigit()]
        filtered_text = " ".join(filtered_words)
        return filtered_text

    def lemmatize_text(self, text):
        words = text.split()
        lemmatized_words = [self.lemmatize_word(word) for word in words]
        filtered_text = " ".join(lemmatized_words)
        return filtered_text

    def lemmatize_word(self, word):
        for suffix, replacement in NORMALIZATION_RULES.items():
            if word.endswith(suffix):
                word = word[:-len(suffix)] + replacement
                break
        return word
    
    def apply_all(self, text):
        text = self.lower_case(text)
        text = self.remove_punctuation(text)
        text = self.remove_numbers(text)
        text = self.remove_stop_words(text)
        text = self.lemmatize_word(text)
        return text
    
