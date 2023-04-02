from src.classes.Ngram import Ngram

class Tokenizer():
    def __init__(self, text):
        self.text = text
    
    def tokenize(self):
        return self.text.split()
    
    def get_ngrams(self, n):
        tokenized_text = self.tokenize()
        list_of_n_grams = [Ngram([], '<@>')]*(n-1) 
        for index in range(len(tokenized_text)):
            word = tokenized_text[index] 
            previous_words = tokenized_text[index-(n-1): index]
            n_gram = Ngram(previous_words, word)
            list_of_n_grams.append(n_gram)
        return list_of_n_grams

