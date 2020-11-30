import os
import configparser
from save_and_load import to_json as to_format
from save_and_load import to_pickle as to_format
from save_and_load import to_csv as to_format

CONFIG_PATH = '.\\config\\config.ini'
FILE_FORMAT = ''


def create_config(CONFIG_PATH):
    """Create config file with needed format"""
    FILE_FORMAT = "JSON"                              # input format file
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "Format", FILE_FORMAT)    # input format file
    with open(CONFIG_PATH, "wt") as config_file:
        config.write(config_file)
        config_file.close()


def read_config(CONFIG_PATH):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    FILE_FORMAT = config['Settings']['FORMAT']
    return FILE_FORMAT


def check_config():
    if os.path.exists(CONFIG_PATH):
        print("1")
        read_config(CONFIG_PATH)
    else:
        create_config(CONFIG_PATH)


if FILE_FORMAT == "JSON":
    from save_and_load import to_json as to_format
elif FILE_FORMAT == "PICKLE":
    from save_and_load import to_pickle as to_format
elif FILE_FORMAT == "CSV":
    from save_and_load import to_csv as to_format


def load():
    return to_format.load()


def save():
    return to_format.save()
