import json
import model


Path = ".\\save_and_load\\Phonebook.json"


def load():
    with open(Path, 'rt') as f:
        return json.load(f)


def save():
    with open(Path, 'wt') as f:
        json.dump(model.phonebook, f)
        f.close()
