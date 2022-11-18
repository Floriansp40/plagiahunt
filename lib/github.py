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
    again = True # Loop control
    first = True # first résult flag
    page = 1 # pagination

    while again:      
        # Control for GitHub RateLimit          
        if res.status_code != 200:
            print("Github API stop with code : {}".format(res.status_code))
            if first:
                raise SystemExit
            else:
                return results

        # Result at JSON format 
        rjson = json.loads(res.text)

        # Question according the first result count (total count)
        if first:
            print("Github gave us {} result(s)".format(rjson['total_count']))
            answer = input("\nLet's Go ? [Yes|no] ")
            if answer.lower() in ['n', 'no'] :
                raise SystemExit

        print("Retrieved results : {}".format(len(rjson['items'])))

        # Concatenation
        if first:
            results = rjson
            first = False
        else:
            results['items'] += rjson['items']

        if len(rjson['items']) < 30:
            print("FIN DE LISTE")
            again = False
        else:
            print("ON CONTINU")
            time.sleep(1.5)
            page += 1

    print("SORTIE")
    return results

# Function to download file by url
def downloadFile(url):
    url = url.replace("https://github.com", "https://raw.githubusercontent.com/")
    url = url.replace("/blob", "")

    return requests.get(url)

# Function to clone repository
def gitClone(url):
    Repo.clone_from(url, "./origin")