from src.classes.Tokenizer import Tokenizer

from tqdm import tqdm

class NModelPredictor():
    def __init__(self, n):
        self.n = n
        self.context = {}
    
    def fit(self, text):
        tokenizer = Tokenizer(text=text)
        all_n_grams = tokenizer.get_ngrams(n=self.n)
        bar = tqdm(total=len(list_of_previous_words))
        for n_gram in all_n_grams:
            previous_words = tuple(n_gram.get_context())
            current_word = n_gram.get_current_word()

            if previous_words in self.context:
                if current_word in self.context[previous_words]:
                    self.context[previous_words][current_word] += 1
                else:
                    self.context[previous_words][current_word] = 1
            else:
                self.context[previous_words] = dict()
                self.context[previous_words][current_word] = 1
            bar.update(1)
    
    def get_best_prediciton_based_on_previous_words(self, previous_words):
        frequency_dictionary = self.context[previous_words]
        best_prediciton = max(frequency_dictionary, key=frequency_dictionary.get)
        return best_prediciton
            
    def predict_single_word(self, previous_words):
        previous_words = tuple(previous_words)
        if previous_words in self.context:
            return self.get_best_prediciton_based_on_previous_words(previous_words)
        return None
    
    def predict(self, list_of_previous_words):
        predictions = list()
        bar = tqdm(total=len(list_of_previous_words))
        for previous_words in list_of_previous_words:
            prediction = self.predict_single_word(previous_words)
            predictions.append(prediction)
            bar.update(1)
        return predictions
            


    