import csv
import model


Path = ".\\save_and_load\\Phonebook.csv"


def load():
    with open(Path, 'rt') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            model.phonebook[row[0]] = row[1]
        return model.phonebook


def save():
    with open(Path, 'w') as f:
        for key in model.phonebook.keys():
            f.writelines(f"{key},{model.phonebook[key]}\n")
