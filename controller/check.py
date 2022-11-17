import os
import shutil
from lib.message import *

from controller.search import *

# Function to check plagiat with origin file in tmp folder
def checkOnOrigin(argv):
    if not os.path.exists('./tmp/origin.'+argv[3]): 
        errorMessage("There is no file to compare (origin.{})".format(argv[3]))
        errorMessage("Please check python3 main.py --help")
        raise SystemExit

    # Send search on github and plagiat engine
    ctrlSearch(argv, 'origin')

# Function to check plagiat with spécific file in origin folder
def checkOnPath(argv):
    if not os.path.exists('.'+argv[5]): 
        errorMessage("The file does not exists")
        raise SystemExit

    # Copie and rename to tmp folder
    shutil.copy('.'+argv[5], './tmp/origin.{}'.format(argv[3]))

    # Send search on github and plagiat engine
    ctrlSearch(argv, 'origin')

# Controller dispatcher according argv
def ctrlCheck(argv):
    if len(argv) == 4:
        checkOnOrigin(argv)
    elif len(argv) == 6:
        checkOnPath(argv)
    else:
        helpMessage()
        raise SystemExit