import requests
import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
from git import Repo

# Init environment
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

# Call github API with search term
def githubSearch(term, type):
    query = term+"+in:file+language:"+type+"&page=1"
    myHeaders = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(os.environ.get('TOKEN'))
    }

    res = requests.get(os.environ.get("GITHUB_API").format(query), headers=myHeaders)
    print(res.status_code)
    #print(json.loads(res.text))
    return json.loads(res.text)

# Function to download file by url
def downloadFile(url):
    url = url.replace("https://github.com", "https://raw.githubusercontent.com/")
    url = url.replace("/blob", "")

    return requests.get(url)

# Function to clone repository
def gitClone(url):
    Repo.clone_from(url, "./origin")