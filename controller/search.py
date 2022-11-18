import sys
import subprocess
from tqdm import tqdm
from lib.message import *
from lib.github import *
from lib.file import *
from lib.message import *

# Function to search on github and start engine
def ctrlSearch(argv, type):

    if len(argv) < 4:
        helpMessage()
        raise SystemExit

    # Get similar github repo
    plagiat = githubSearch(argv[2], argv[3])

    # Check if github found something else exit
    if plagiat['total_count'] == 0:
        warningMessage("No result found")
        raise SystemExit    

    # Iterate and download file in tmp folder
    for item in tqdm(plagiat['items']):
        res = downloadFile(item['html_url'])
        createFile(item['repository']['owner']['login']+"_"+item['name'], res.content)

    # Call the Alexandre's engine for check
    successMessage("\nGo to plagiat fiesta ;)")
    subprocess.call(["python3", "./core/main.py", "./tmp", argv[3], type])

    # Cleaning after search
    clearTmp()
