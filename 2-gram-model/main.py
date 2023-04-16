from src.classes.PreProcess import PreProcess
from src.classes.Tokenizer import Tokenizer
from src.classes.NModelPredictor import NModelPredictor
from src.classes.Metrics import Metrics

from src.utils.database import read_txt_file
from src.utils.format import prepare_text_for_predicion

if __name__ == "__main__":
    train = read_txt_file("wiki.train.raw")
    test = read_txt_file("wiki.test.raw")
    preprocess = PreProcess()
    train = preprocess.remove_punctuation(train)
    train = preprocess.remove_useless_information(train)
    train = preprocess.remove_stop_words(train)
    train = preprocess.lemmatize_word(train)
    test = preprocess.remove_punctuation(test)
    test= preprocess.remove_useless_information(test)
    test = preprocess.remove_stop_words(test)
    test = preprocess.lemmatize_word(test)
    back_off = NModelPredictor(n=2)
    back_off.fit(train)
    model = NModelPredictor(n=3)
    model.set_back_office_model(back_off)
    model.fit(train)
    x_test, y_test = prepare_text_for_predicion(test, 3)
    y_pred = model.predict(x_test)
    metrics = Metrics(y_pred=y_pred, y_true=y_test)
    print(f"Acc: {metrics.accuracy()}")