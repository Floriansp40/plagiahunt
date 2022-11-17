from termcolor import colored, cprint

def helpMessage():
    cprint("Usage", "yellow")
    cprint("\tpython3 main.py git [Repository url]", "yellow")
    cprint("\t\tMake a git clone from repository url in origin folder and display tree")

    cprint("\n\tpython3 main.py path", "yellow")
    cprint("\t\tDisplay tree system from origin folder")
    cprint("\n")
    cprint("\tpython3 main.py search [\"search term\"] [file type]", "yellow")
    cprint("\t\tSend request to Github about the \"search term\" and compare files found and make plagiat %")
    cprint("\n")
    cprint("\t\tsearch term\t one or several words (string)")
    cprint("\t\tfile type\t his extension like js jsx html py css etc...")
    cprint("\n")
    cprint("\tpython3 main.py check [\"search term\"] [file type] {--path path from origin folder}", "yellow")
    cprint("\t\tSend request to Github about the \"search term\" and compare files found with origin file and make plagiat %")
    cprint("\t\tWithout path parameter an origin file must be present in origin folder", "blue")
    cprint("\t\tI.e to compare a js file, you have to past the file in origin folder and rename it origin.js", "blue")
    cprint("\n")
    cprint("\t\tWith path parameter the selected file will be copied and pasted to origin folder and the search on github start")
    cprint("\n")
    cprint("\tpython3 main.py clean [tmp|origin|all]", "yellow")
    cprint("\n")
    cprint("\t\ttmp\tFor only tmp folder")
    cprint("\t\torigin\tFor only origin folder")
    cprint("\t\tall\tFor both folders")
    cprint("\n")

def errorMessage(message):
    cprint(message, 'red')

def warningMessage(message):
    cprint(message, 'yellow')

def successMessage(message):
    cprint(message, 'green')