from termcolor import colored, cprint

def helpMessage():
    cprint("Usage", "yellow")
    cprint("\tpython3 main.py \"[search term]\" [file type]")
    cprint("\n")
    cprint("\tsearch term\tAll sentence that you want check")
    cprint("\tfile type\t{js|css|html|...} All file types file you want but you have")

def errorMessage(message):
    cprint(message, 'red')

def warningMessage(message):
    cprint(message, 'yellow')

def successMessage(message):
    cprint(message, 'green')