import pickle
import model


Path = ".\\save_and_load\\Phonebook.pickle"


def load():
    with open(Path, 'rb') as f:
        return pickle.load(f)


def save():
    with open(Path, 'wb') as f:
        pickle.dump(model.phonebook, f)
        f.close()
