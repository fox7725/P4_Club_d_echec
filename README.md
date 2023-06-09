# Club d'échec
Ceci est un projet de logiciel de gestion des tournois d'échec en python dans le cadre du projet 4 de la formation Développeur d'applications Python chez Open ClassRooms.

# Que fait-il ? 

Ce logiciel entièrement rédigé en Python gère intégralement les tournois et les joueurs d'un club d'échec. Il génère un nouveau tournoi, enregistre les joueurs, leurs points et les matchs et stock l'ensemble dans des fichiers JSON. Il permet aussi de consulter les tournois archivés et de consulter la liste des joueurs inscrits dans le club.

# Comment utiliser le fichier python
## Etape 1 : Créer votre environnement virtuel :
**Attention, les commande ci dessous fonctionnent sous windows 11, elles n'ont pas été testées sous d'autres systèmes d'exploitation.**
**De même, l'application présentée ici fonctionne de façon optimale sous Python 3.3 et n'a pas été testée sous des versions antérieure**

Pour chaque nouveau projet, il est recommandé d'installer un environnement virtuel pour partir sur de nouvelles bases
- Ouvrez votre Terminal préféré
- Dans le dossier où vous avez copié les fichiers du projet, tapez la commande `python -m venv env` pour créer votre environnement virtuel
- Puis lancez le en tapant `env\Scripts\activate.bat`
- Pour faire fonctionner ce logiciel de gestion des tournois, vous aurez besoin d'installer quelques packages, pour ce faire vous trouverez le fichier **"requierement.txt"** que vous pouvez utiliser en tapant `pip install -r requirements.txt`

## Etape 2 : Lancer le logiciel
Nous avons presque terminé, il ne vous reste plus qu'à démarrer le script, et pour ça rien de plus simple il vous suffit d'écrire la commande `python main.py`.
Maintenant Il ne vous reste plus qu'à vous laisser guider à travers les menus

## Etape 3 : Vérification de la bonne mise aux normes PEP8
pour vérifier que le code de ce logiciel respecte les normes **PEP8**, il vous suffit de taper `flake8 --format=html --htmldir=flake-report main.py view controller fonctions models`, pour plus de facilité nous l'avons déjà fait et vous pourrez trouver dans le dossier `flake-report` les fichiers HTML générés avec **Flake8**. Il vous suffit de lancer `index.html' pour consulter l'ensemble des normes non respectées.

## Etape 4 : Quitter l'environnement virtuel
N'oubliez pas de fermer la porte de votre environnement virtuel (et d'y éteindre la lumière) avec la commande `deactivate`
Vous pouvez maintenant aller chercher les fichiers image dans le dossier **"images"**, elles sont toutes classées dans des sous-dossiers aux noms des catégories.
Vous trouverez le fichier **livres.csv** dans le dossier CSV.

# Remerciements
Un grand merci à mon mentor **Aurélien MALVE** qui a su me guider tout en douceur et à **Zozor** (l'ancienne mascotte du site) qui m'a donné envie de revenir sur **le Site du Zéro** pour apprendre le Python
(P.S. : Rendez nous **Zozor** !!!)

# Auteur
Script réalisé par Christophe RENARD
