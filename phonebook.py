#controller
import messages
import model
from config import config_func


config_func.check_config()


print(messages.MSG_MENU)


while True:
    try:
        operation = input(messages.MSG_INPUT_COMMAND).upper()
        if operation in ('c', 'C'):
            model.create_record()

        elif operation in ('F', 'f'):
            model.find_name()

        elif operation in ('U', 'u'):
            model.update_record()

        elif operation in ('D', 'd'):
            model.del_record()

        elif operation in ('A', 'a'):
            model.print_records()

        elif operation in ('S', 's'):
            config_func.save()

        elif operation in ('L', 'l'):
            config_func.load()

        else:
            quit()

    except KeyError as e:
        print(e)
    except ValueError:
        print(messages.MSG_DIGITS_ERROR)
        continue
