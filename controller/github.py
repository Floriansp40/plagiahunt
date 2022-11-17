from lib.message import *
from lib.github import *
from lib.path import *

# Function to start git clone from repository
def ctrlGit(argv):
    if len(argv) < 3:
        helpMessage()
        raise SystemExit
    
    gitClone(argv[2])
    displayPath()