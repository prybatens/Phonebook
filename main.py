import messages
import phonebook

def print_menu():
    print(messages.MSG_MENU)


print_menu()

variant = 0

while True:
    operation = input(messages.MSG_INPUT_COMMAND).upper()
    if operation not in {'C', 'F', 'U', 'D', 'A', 'W', 'R'}:
        break
    phonebook()
