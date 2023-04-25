import pandas as pd
from src.constants.path import ROOT_PATH

def read_file(file, path=f"{ROOT_PATH}/src/data/"):
    with open("./src/data/SMSSpamCollection") as file:
        return file.readlines()

def get_df():
    file_content = read_file("SMSSpamCollection")
    labels = list()
    messages = list()
    for line in file_content:
        label, message = line.split("\t")
        labels.append(label)
        messages.append(message)
    dataframe = pd.DataFrame({"x": messages, "y": labels})
    return dataframe