import pandas as pd
from tqdm import tqdm

from src.classes.PreProcess import PreProcess

class NaiveBayes():
    def __init__(self, df, x, y):
        self.df = df.copy()
        self.x = x
        self.y = y
        self.classes = df["y"].unique()
    
    def fit(self):
        self.relative_frequency_table = dict()
        for class_ in self.classes:
            filtered_df = self.df.query(f"{self.y} == @class_")
            class_words = ''.join(filtered_df[self.x])
            class_words_formated = pd.Series(class_words.split())
            frequency_table = class_words_formated.value_counts(True)
            self.relative_frequency_table[class_] = frequency_table
    
    def predict_single_phrase(self, phrase):
        preprocess = PreProcess()
        phrase = preprocess.apply_all(phrase)
        words = phrase.split(" ")
        p_total = 0
        predicted_class = ""
        for class_ in self.classes:
            p_class = 1
            for word in words:
                if word in self.relative_frequency_table[class_]:
                    p_word = self.relative_frequency_table[class_][word]
                else:
                    p_word = self.relative_frequency_table[class_].mean()
                p_class *= p_word
            if p_class >= p_total:
                p_total = p_class
                predicted_class = class_
        return predicted_class

    def predict(self, list_of_phrases):
        predictions = list()
        bar = tqdm(total=len(list_of_phrases))
        for phrase in list_of_phrases:
            prediction = self.predict_single_phrase(phrase)
            predictions.append(prediction)
            bar.update(1)
        return predictions