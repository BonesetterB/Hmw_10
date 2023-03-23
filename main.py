from collections import UserDict

class AddressBook(UserDict):
    data={}
    def show(self):
        list_of_numbers=[]
        for k, v in self.data.items():
            list_of_numbers.append(f'{k}: {v}')
        return '\n'.join(list_of_numbers)
    def search(self, key):
        if key.data[0] in self.data:
            return ''.join(self.data[key.data[0]])
        else:
            return f'Contact {key.data[0]} didnt add.'
User_book=AddressBook()
class Record:
    def __init__(self,data):
        self.N=Name()
        self.P=Phone()
        self.data=data
    def add(self):
        User_book.data[self.N.name()]=self.P.phone()
    def change(self):
        User_book.data[self.N.name()]=self.P.phone()
    def delete(self):
        User_book.data.pop(self.N.name())
class Field:
    def __init__(self,data):
        Field.data=data
class Name(Field):
    def __init__(self):
        super().__init__(Field.data)
    def name(self):
        return Field.data[0]
class Phone(Field):
    def __init__(self):
        super().__init__(Field.data)
    def phone(self):
        return Field.data[1:]
    

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
    help_text = ['delete: delete contact',
        'exit: exit',
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
    x=Record(string)
    x.add()
    return 'Number was success add!'

@check_command
def phone(string):
    s=User_book.search(string)
    return s

@check_command
def change(string):
    x=Record(string)
    x.change()
    return 'Number was success change!'

def delete(string):
    x=Record(string)
    x.delete()
    return 'User was success delete'
def show_all(string):
    return User_book.show()


COMMANDS = {delete:'delete',
            command: 'command',
            exit: 'exit',
            add: 'add',
            change: 'change',
            phone: 'phone',
            show_all: 'show_all'}


def command_handler(text: str):
    for command, key_word in COMMANDS.items():
        if text.lower().startswith(key_word):
            return command, text.replace(key_word, '').strip().split(' ')
    return None, 'You write wrong command, for  to get a list of commands write command'


def main():
    while True:
        command_user = input('>>>')
        command, data = command_handler(command_user)
        data=Field(data)
        if command:
            print(command(data))
        else:
            print(data)
        if command == exit:
            break
main()