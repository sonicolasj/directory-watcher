# Directory Watcher

Application surveillant un ou plusieurs dossiers, dans le but de rediriger les fichiers y arrivant dans d'autres dossiers, selon des règles de filtrage définie en configuration.

## Exemple

Exemple de configuration :
~~~
- directory_path: "/data/Downloads"

  rules: 
  - destination_folder: "/data/Downloads/Images"
    ignore_hidden: yes
    extensions: 
    - "jpg"
    - "png"
    - "jpeg"
    
  - destination_folder: "/data/Documents/Admin/Banque"
    ignore_hidden: yes
    title_contains: "releve"
    extensions: 
    - "pdf"

~~~

Pour chaque nouveau fichier entrant dans le dossier `/data/Downloads`, les fichiers d'extension `*.jpg`, `*.png`, ou `*.jpeg` sont déplacés dans le dossier `/data/Downloads/Images`. De même, tous les fichiers `*.pdf` dont le nom contient *releve* sont déplacés dans `/data/Documents/Admin/Banque`.

## Installation

1. Cloner le dépot : `git clone https://github.com/sonicolasj/directory-watcher.git`
2. Installer les dépendances : `cd directory-watcher` puis `pip2 install -r requirements.txt`
3. Initialiser l'application : `python2 setup.py`
4. Renseigner les fichiers `directory-watcher/conf/directories.yaml` et `directory-watcher/conf/profiles.yaml` en se basant sur la documentation présente dans les fichiers `*.dist` pour activer la surveillance.
