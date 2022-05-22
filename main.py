import re

dictionary = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("If you write command 'add' please write 'add' 'name' 'number':  ")
            print("If you write command 'change' please write 'change' 'name' 'number':  ")
            print("If you write command 'phone' please write 'phone' 'name':  ")
    return wrapper


def main():
    while True:
        user_input = input()
        user_input1 = user_input.lower()
        if user_input1 == "good bye" or user_input1 == "close" or user_input1 == "exit":
            print(input_bye())
            break
        if user_input1 == "help":
            print(input_help())
        if user_input1 == "hello":
            print(input_hello())
        if user_input1.startswith("add"):
            input_add(user_input1)
        if user_input1.startswith("change"):
            input_change(user_input1)
        if user_input1.startswith("phone"):
            input_phone(user_input1)
        if user_input1.startswith("show all"):
            input_show()


def input_help():
    return """help - output command, that help find command
hello - output command 'How can I help you?' 
add - add contact, use 'add' 'name' 'number'
change - change your contact, use 'change' 'name' 'number'
phone - use 'phone' 'name' that see number this contact
show all - show all your contacts
"""


def input_bye():
    return "Good bye"


def input_hello():
    return "How can I help you?"


@input_error
def input_add(user_input1):
    pattern = r'\w+'
    name_number = re.findall(pattern, user_input1)
    dictionary.update({name_number[1].title(): name_number[2]})
    return dictionary


@input_error
def input_change(user_input1):
    pattern1 = r'\w+'
    new_name_number = re.findall(pattern1, user_input1)
    name1 = new_name_number[1].title()
    number1 = new_name_number[2]
    for k, v in dictionary.items():
        if name1 == k:
            dictionary[k] = number1
    return dictionary


@input_error
def input_phone(user_input1):
    pattern2 = r'\w+'
    new_name_number1 = re.findall(pattern2, user_input1)
    number2 = new_name_number1[1].title()
    print(dictionary.get(number2))


def input_show():
    for k, v in dictionary.items():
        print(k + ': ' + "".join(v))


main()
