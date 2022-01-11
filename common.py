from termcolor import colored

def print_function(message):
    print(colored(message, 'blue'))

def print_fail(message):
    print(colored(message, 'red'))

def print_highlight(message):
    print(colored(message, 'yellow'))

def print_success(message):
    print(colored(message, 'green'))    

def input_highlight(message):
    return input(colored(message, 'yellow'))