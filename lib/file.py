import os
import glob
import shutil
from os.path import join, dirname
from dotenv import load_dotenv

# Init environment
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Function to create file in tmp folder
def createFile(name, content):
    fp = open("./tmp/"+name, "wb")
    fp.write(content)
    fp.close()

# Function to clean tmp folder after search
def clearTmp():
    answer = input("\nClear Tmp Files ? [yes|no] ")
    if answer.lower() in ['y', 'yes'] :
        files = glob.glob('./tmp/*')

        for f in files:
            os.remove(f)

# Function to clean origin folder
def clearOrigin():
    answer = input("\nClear Origin Files ? [yes|no] ")
    if answer.lower() in ['y', 'yes'] :
        files = glob.glob('./origin/*')

        for f in files:
            if os.path.isfile(f) or os.path.islink(f):
                os.remove(f)
            else:
                shutil.rmtree(f)

        # last clean for git
        os.remove('./origin/.gitignore')
        shutil.rmtree('./origin/.git')

        