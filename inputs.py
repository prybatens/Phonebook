import messages

def input_name():
    """ Func name input"""
    name = input(messages.MSG_INPUT_NAME).strip().capitalize()
    return name


def input_phone():
    """ Func phone number input"""
    phone = int(input(messages.MSG_INPUT_PHONE))
    return phone


def input_format():
    """Func input config [format] """
    FILE_FORMAT = input(messages.MSG_INPUT_FORMAT).upper()
    return FILE_FORMAT

