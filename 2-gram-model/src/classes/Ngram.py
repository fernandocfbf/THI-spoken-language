class Ngram():
    def __init__(self, previous_n_words, target_word):
        self.previous_n_words = previous_n_words
        self.target_word = target_word
    
    def get_context(self):
        return self.previous_n_words

    def get_current_word(self):
        return self.target_word
