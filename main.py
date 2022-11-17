import sys
from lib.message import *
from lib.github import *
from lib.path import *

from controller.clean import *
from controller.search import *
from controller.check import *
from controller.github import *

# First if not enough arguments
if len(sys.argv) < 2:
    helpMessage()
    raise SystemExit


# Dispatcher according CLI arguments
match sys.argv[1]:
    case "path":
        displayPath()

    case "git":
        ctrlGit(sys.argv)

    case "search":
        ctrlSearch(sys.argv, 'simple')

    case "clean":
        if len(sys.argv) < 3:
            helpMessage()
            raise SystemExit

        ctrlClean(sys.argv[2])

    case "check":
        if len(sys.argv) < 3:
            helpMessage()
            raise SystemExit

        ctrlCheck(sys.argv)
        
    case _:
        helpMessage()
        raise SystemExit

