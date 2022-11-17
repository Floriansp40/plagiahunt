from lib.file import *
from lib.message import *

# Function to select folder to clean it
def ctrlClean(place):
    match place:
        case "tmp":
            clearTmp()
        case "origin":
            clearOrigin()
        case "all":
            clearTmp()
            clearOrigin()
        case _:
            errorMessage("Can't find where to clean")

    
