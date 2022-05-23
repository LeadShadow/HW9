dictionary = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return """If you write command 'add' please write 'add' 'name' 'number'
If you write command 'change' please write 'change' 'name' 'number'
If you write command 'phone' please write 'phone' 'name'"""
        except KeyError:
            return "..."
    return wrapper


def input_help():
    return """help - output command, that help find command
hello - output command 'How can I help you?' 
add - add contact, use 'add' 'name' 'number'
change - change your contact, use 'change' 'name' 'number'
phone - use 'phone' 'name' that see number this contact
show all - show all your contacts
"""


def input_bye(*args):
    return "Good bye"


def input_hello(*args):
    return "How can I help you?"


@input_error
def input_add(*args):
    dictionary.update({args[0]: args[1]})
    return f"Contact {args[0].title()} add successful"


@input_error
def input_change(*args):
    dictionary[args[0]] = args[1]
    return f"Contact {args[0].title()} change successful"


@input_error
def input_phone(*args):
    return dictionary[args[0]]


def input_show(*args):
    return "\n".join([f"{k.title()} : {v} " for k, v in dictionary.items()])


commands = {
    input_hello: "hello",
    input_add: "add",
    input_phone: "phone",
    input_show: "show all",
    input_change: "change",
    input_bye: "good bye",
    input_help: "help"
}


def command_parser(user_input1):
    data = []
    command = ""
    for k, v in commands.items():
        if user_input1.startswith(v):
            command = k
            data = user_input1.replace(v, "").split()
    return command, data


def main():
    while True:
        user_input = input()
        user_input1 = user_input.lower()
        command, data = command_parser(user_input1)
        print(command(*data))
        if command == input_bye:
            break


if __name__ == "__main__":
    main()
