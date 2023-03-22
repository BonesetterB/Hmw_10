from collections import UserDict
memory={}
class AddressBook(UserDict):
    pass
class Record:
    pass
class Field:
    pass
class Name:
    pass
class Phone:
    pass
def check_command(command):
    def wrapper(string):
        try:
            return command(string)
        except IndexError:
            return "Type all param for command. For help, type 'command'"
        except KeyError:
            return f"No record {string}, check param. For help, type 'command'"
        except ValueError:
            return "Phone must contains only digit"
    return wrapper


def exit(string):
    return "Good bye!"


def command(string):
    help_text = ['exit: exit',
       'add: add new contact need write name and number with\
           space command shoulde be look like this "add name number"',
       'change: change numbers already created contact command\
           shoulde be look like this "change name number"',
       'show_all: show all the contacts',
       'phone: this command shows the persons phone command\
           should be look like this "name number"']
    return '\n'.join(help_text)


@check_command
def add(string):
    data = string.split(' ')
    memory[data[0]] = int(data[1])
    return 'Number was success add!'

@check_command
def phone(string):
    name_person = string
    return memory[name_person]

@check_command
def change(string):
    data =string.split(' ')
    memory[data[0]] = int(data[1])
    return 'Number was success change!'


def show_all(string):
    list_of_numbers=[]
    for k, v in memory.items():
        list_of_numbers.append(f'{k}: {v}')
    return '\n'.join(list_of_numbers)


COMMANDS = {command: 'command',
            exit: 'exit',
            add: 'add',
            change: 'change',
            phone: 'phone',
            show_all: 'show_all'}


def command_handler(text: str):
    for command, key_word in COMMANDS.items():
        if text.lower().startswith(key_word):
            return command, text.replace(key_word, '').strip()
    return None, 'You write wrong command, for  to get a list of commands write command'


def main():
    while True:
        command_user = input('>>>')
        command, data = command_handler(command_user)
        if command:
            print(command(data))
        else:
            print(data)
        if command == exit:
            break
main()