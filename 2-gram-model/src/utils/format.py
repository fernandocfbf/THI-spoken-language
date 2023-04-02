from src.classes.Tokenizer import Tokenizer

def prepare_text_for_predicion(text, n):
    tokenizer = Tokenizer(text=text)
    all_n_grams = tokenizer.get_ngrams(n=n)
    to_predict = list()
    true_values = list()
    for n_gram in all_n_grams:
        previous_words = tuple(n_gram.get_context())
        current_word = n_gram.get_current_word()
        to_predict.append(previous_words)
        true_values.append(current_word)
    return to_predict, true_values

