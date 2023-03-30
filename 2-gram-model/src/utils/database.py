from src.constants.path import ROOT_PATH

def read_txt_file(file, path=f"{ROOT_PATH}/src/data/"):
    with open(f"{path}{file}") as f:
        return f.read()
    