# Requirements

> Regarder le fichier `Pipfile`

# Tasks

## Scraping 1/2

- [x] Récupérer les données relatives à la diffusion d’épisodes pour le mois en cours disponibles sur cette page :  https://www.spin-off.fr/calendrier_des_series.html

    - [x] Le nom de la série
    - [x] Le numéro de l’épisode
    - [x] Le numéro de la saison
    - [x] La date de diffusion de l’épisode
    - [x] Le pays d’origine
    - [x] La chaîne qui diffuse la série
    - [x] L’url relative de la page de l’épisode sur le site spin-off

- [x] Enregistrez ces données dans un fichier episodes.csv dans le dossier data/files (vous pouvez utiliser une librairie)
- [x] Écrire une fonction ou une classe qui permet de lire le fichier episodes.csv sans utiliser de librairie. Cette fonction ou classe devra renvoyer une liste de tuples avec les bons types

## SQL 1/2

- [x] Insérer les données de la question Scraping [1/2] dans base de données sqlite appelée database.db dans le dossier data/databases. La table devra s’appeler episode. Veillez à utiliser les types adéquats (la date peut toutefois être stockée en tant que chaîne de caractères avec un type TEXT).

## Algorithmie 1/2

- [x] Calculer le nombre d’épisodes diffusés par chaque chaîne de télévision (présente dans les données) en Octobre.
Vous pouvez faire directement des requêtes SQL, ou rapatrier les données depuis une table (ou un fichier dans lequel vous les auriez stocker) et faire les calculs avec Python. Indiquer dans le fichier README.md le nom des trois chaînes qui ont diffusé le plus d’épisodes.
    - Netflix : 39
    - Disney +: 32
    - Hulu: 24

- [x] Faire de même pour les pays (pensez à mutualiser votre code !)
    - Etats Unis : 238
    - Canada : 43
    - Royaume Uni: 31

- [x] Quels mots reviennent le plus souvent dans les noms des séries ? (attention à ne compter qu’une seule fois chaque série, et pas une fois chaque épisode) Les indiquer dans le fichier README.md
    - the : 21 
    - all : 4 
    - of : 3 
    - and : 3

## Scraping 2/2

- [ ] Sur les pages individuelles des épisodes (dont l’url à été récupérée lors de la première question), récupérer la durée de l’épisode. Les requêtes peuvent être un peu longue donc vous pouvez ne le faire que pour une seule chaîne comme Apple TV. Veiller à ne pas perdre les données pour pouvoir les insérer dans SQL. Pensez à utiliser un time.sleep entre les requêtes.

## SQL 2/2

- [ ] Stocker les données de durée d’épisode (en minutes) dans une nouvelles table duration qui contiendra une Foreign Key pointant sur l’épisode en question dans la table episode.

## Algorithmie 2/2

- [ ] Quelle est la chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs sur le mois d’Octobre ? (écrire une fonction qui permet de répondre à cet question)

## Orchestration

- [ ] On souhaite que la commande suivante : `python3 summarize_episodes.py --month 11` affiche dans la console :

```
    - [NOMBRE] episodes seront diffusés pendant le mois de [MOIS].
    - C'est [PAYS] qui diffusera le plus d'épisodes avec [NOMBRE] épisodes.
    - C'est [CHAINE] qui diffusera le plus d'episodes avec [NOMBRE] épisodes.
    - C'est [CHAINE] qui diffusera des épisodes pendant le plus grand nombre \
    de jours consécutifs avec [NOMBRE] de jours consécutifs.
```