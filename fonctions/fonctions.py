import json
import os
import datetime
import send2trash


def liste_joueur_JSON():
    # On crée le dossier JSON pour stocker les BDD s'il n'existe pas
    os.makedirs("JSON", exist_ok=True)
    bdd_joueurs = "JSON/joueurs.json"
    if os.path.exists(bdd_joueurs):
        # Si le fichier JSON pour les joueurs existe, on récupère la liste des
        # joueurs
        with open(bdd_joueurs, 'r') as f:
            contenu = json.load(f)
    else:
        contenu = "ERR01"
    return contenu


def verification_date(date):
    format_date = "%d/%m/%Y"
    try:
        validation_date = datetime.datetime.strptime(date, format_date)
    except ValueError:
        return 0
    return 1


def rapports_tournois():
    os.makedirs("JSON/archives", exist_ok=True)
    bdd_tournois = "JSON/archives/tournois.json"
    if os.path.exists(bdd_tournois):
        with open(bdd_tournois, 'r') as f:
            contenu = json.load(f)
    else:
        contenu = "ERR01"
    return contenu


def suppression_encours():
    # On regarde les fichiers et les sous-répertoires dans le répertoire
    for dossier, sous_repertoires, fichiers in os.walk("JSON/en_cours"):
        # On supprime les fichiers en les déplaçant dans la corbeille pour
        # plus de sécurité
        for fichier in fichiers:
            chemin_fichier = os.path.join(dossier, fichier)
            send2trash.send2trash(chemin_fichier)

    # On supprime le répertoire vide restant
    os.rmdir("JSON/en_cours")