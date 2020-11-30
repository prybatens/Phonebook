import messages
import inputs


phonebook = {}


def exist_name(name):
    """Func for check existing name in phonebook"""
    return name in phonebook


def find_name():
    name = inputs.input_name()
    if not exist_name(name):
        print(messages.MSG_NAME_NOT_FOUND.format(name))
    else:
        print("Name: ", name, "| Phone: ", get_record(name))


def create_record():
    """Func for creating new contact"""
    name = inputs.input_name()
    phone = inputs.input_phone()
    if exist_name(name):
        print(messages.MSG_NAME_EXISTS)
    else:
        phonebook[name] = phone
    print("Name: ", name, "| Phone: ", get_record(name))


def update_record():
    """Func for updating contact"""
    name = inputs.input_name()
    if not exist_name(name):
        print(messages.MSG_NAME_NOT_FOUND)
    else:
        phone = inputs.input_phone()
        phonebook[name] = phone
        print("Name: ", name, "| Phone: ", get_record(name))


def get_record(name):
    """Func for finding record"""
    return phonebook.get(name, messages.MSG_NAME_NOT_FOUND)


def del_record():
    """Func for deleting record"""
    name = inputs.input_name()
    if not exist_name(name):
        print(messages.MSG_NAME_NOT_FOUND)
    else:
        del phonebook[name]
        print("Name: ", name, " - deleted!")


def print_records():
    print("All contacts:", phonebook.items())
