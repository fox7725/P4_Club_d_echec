import json
import os


def liste_joueur_JSON():
    # On crée le dossier JSON pour stocker les BDD s'il n'existe pas
    os.makedirs("JSON", exist_ok=True)
    bdd_joueurs = "JSON/joueurs.json"
    if os.path.exists(bdd_joueurs):
        # Si le fichier JSON pour les joueurs existe, on récupère la liste des joueurs
        with open(bdd_joueurs, 'r') as f:
            contenu = json.load(f)
    else:
        contenu = "ERR01"
    return contenu
