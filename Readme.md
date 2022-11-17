# Un outil de comparaison de fichiers

Projet en console pour :
- Faire une recherche de termes sur github
- Comparer le contenu de fichiers
- Faire une recherche par rapport à un fichier

Et afficher le pourcentage de ressemblace.

## Contenu

Un script Python avec utilisation de [Sklearn](https://scikit-learn.org/stable/).

### "Packages" et matériel requis

- Python >= 3.0

- Tout le nécessaire est dans requirements.txt

### Installation et démarrage (consignes adaptées pour utilisateurs/utilisatrices de Mac)

Etape 1: clonez le projet.

Etape 2: naviguez dans le dossier avec la commande ``cd plagiahunt`` puis installez dans le répertoire un environnement virtuel (avec [pipenv](https://docs.python-guide.org/dev/virtualenvs/), ou avec [venv et pip](https://docs.python.org/fr/3/library/venv.html)).
I.e ``python3 -m venv env``

Etape 3: activez l'environnement virtuel avec la commande appropriée ``source env/bin/activate``

Etape 4 : installez au projet les packages requis ; ceux-ci sont fournis dans le fichier ``requirements.txt`` La commande suivante le fera : ``pip3 install -r requirements.txt``.

Etape 5 : créer et récupérer votre token d'accès pour github et le placer dans le fichier env

### Exécuter le script
Toutes les commandes utiles ainsi que leur description sont dans le message d'aide.
Pour l'afficher il suffit de lancer ``python3 main.py``


## Utilisateur
* **Alexandre Kuzo**  [@alexandrekuzo](https://github.com/AlexandreKuzo)


## Améliorer le projet ? 
- Possibilité d'ajouter une application web (Django?) pour choisir l'extension des documents comparés, le nombre de documents comparés, etc.
