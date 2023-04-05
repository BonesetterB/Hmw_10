from collections import UserDict
from datetime import datetime
import json




class AddressBook(UserDict):
    list_name=[]
    data={}
    def save(data):
        with open('memory.txt', "w") as fh:
            json.dump(data, fh)
    
    def read():
        with open('memory.txt', "r") as fh:
            return json.load(fh)
    
    data=read()

    def add_record(self,record):
        if type(record)==list:
            AddressBook.data.pop(Field.value[0])
            AddressBook.data.pop(Field.value[0])
            AddressBook.save(AddressBook.data)
            pass
        else:
            AddressBook.data.update(record)
            AddressBook.data.update(record)
            AddressBook.save(AddressBook.data)
    def show(self):
        list_of_numbers=[]
        for k, v in AddressBook.data.items():
            list_of_numbers.append(f'{k}: {v}')
        return '\n'.join(list_of_numbers)
    def search(self, key):
        list_of_contacts=[]
        for k,v in AddressBook.data.items():
            if key.value[0] == k[0:len(key.value)]:
                list_of_contacts.append(f'{k}:{v}')
            else:
                if key.value[0] == v[0][0:len(key.value[0])]:
                    list_of_contacts.append(f'{k}:{v}')
                    continue
                continue
        if list_of_contacts==[]:
            return f'Contact {key.value} didnt add.'
        else: 
            return '\n'.join(list_of_contacts)
    def iterator(self,value):
            try:
                lst=[]
                for i in range(int(value)):
                    x=f'{self.list_name[i]}: {AddressBook.data[self.list_name[i]]}'
                    lst.append(x)
                yield '\n'.join(lst)
            except IndexError:
                 c='\n'.join(lst)
                 yield f"{c}\nThat all u contacts"
        

User_book=AddressBook()


class Record:
    def __init__(self,name, phone=None, bithday=None):
        self.name = name
        self.phones = [phone] if phone else []
        self.bithday= bithday if bithday else []
    def add(self):
        User_book.list_name.append(self.name)
        if self.bithday==[]:
            return {self.name:[self.phones[0]]}
        return {self.name:[self.phones[0],'-'.join(self.bithday)]}
    def change(self):
        if self.bithday==[]:
            return {self.name:[self.phones[0]]}
        return {self.name:[self.phones[0],'-'.join(self.bithday)]}
    def delete(self):
        print(self.name)
        User_book.pop(self.name)
        return  self.name
    def days_to_birthday(self):
        try:
            x= User_book.search(self.name)
            x=x.split(' ')
            x=x[1].split('-')
            current_datetime = datetime.now()
            bithday=datetime(year=current_datetime.year, month=int(x[1]), day=int(x[0]))
            difference = bithday - current_datetime
            if difference.days<0:
                x=(difference.days*-1)+365
                return x
            return difference.days
        except IndexError:
                return 'In contact didnt add bithday.'


record_operator=Record

class Field:
    def __init__(self,value):
        self.value=value
    def setter(self):
        pass
    def getter(self):
        pass

field=Field


class Name(Field):
    pass
    



class Phone(Field):
    pass





class Birthday(Field):
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
    help_text = ['bithday: do know in how many days is the contacts birthday'
        'delete: delete contact',
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
    nm=Name(string.value[0])
    phn=Phone(string.value[1])
    brth=Birthday(string.value[2:])
    dict=record_operator(nm.value,phn.value,brth.value).add()
    User_book.add_record(dict)
    return 'Number was success add!'

@check_command
def phone(string):
    s=User_book.search(string)
    return s

@check_command
def change(string):
    nm=Name(string.value[0])
    phn=Phone(string.value[1])
    brth=Birthday(string.value[2:])
    dict=record_operator(nm.value,phn.value,brth.value).change()
    User_book.add_record(dict)
    return 'Number was success change!'

def bithday(string):
    nm=Name(string.value[0])
    dict=record_operator(nm.value).days_to_birthday()
    return dict

def delete(string):
    nm=Name(string.value[0])
    dict=record_operator(nm.value).delete()
    User_book.add_record(dict)
    return 'User was success delete'

def show_all(string):
    return User_book.show()

def iter(string):
    nm=Name(string.value[0])
    for i in User_book.iterator(nm.value):
        print(i)
    return 'For more contacts use agains common'

COMMANDS = {delete: 'delete',
            iter:'iter',
            bithday: 'bithday',
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