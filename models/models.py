import json
import os
import random
import datetime

import controller.controller


class Joueur :
    def __init__(self, q_identifiant, q_nom, q_prenom, q_sexe,
                 q_date_naissance, q_remarque, stat_liste_tournois,
                 stat_moyenne_points):
        self.identifiant = q_identifiant
        self.nom = q_nom
        self.prenom = q_prenom
        self.sexe = q_sexe
        self.date_naissance = q_date_naissance
        self.remarque = q_remarque
        self.liste_tournois = stat_liste_tournois
        self.moyenne_points = stat_moyenne_points

    def dictionnaire(self):
        #on crée un dictionnaire
        dict_joueur = {
            "Identifiant national" : self.identifiant,
            "Nom du joueur" : self.nom,
            "Prénom du joueur" : self.prenom,
            "Sexe" : self.sexe,
            "Date de naissance" : self.date_naissance,
            "Remarque du directeur" : self.remarque,
            "Liste des tournois" : self.liste_tournois,
            "Moyenne des points par tournoi" : self.moyenne_points
        }
        return dict_joueur
    def enregistreJoueur(self):
        #On crée le dossier JSON pour stocker les BDD s'il n'existe pas
        os.makedirs("JSON", exist_ok=True)
        bdd_joueurs = "JSON/joueurs.json"
        joueur_voulu = "//"
        if os.path.exists(bdd_joueurs):
            #Si le fichier JSON pour les joueurs existe, on vérifie que le joueur n'existe pas déjà et on l'enregistre
            with open(bdd_joueurs, 'r') as f :
                contenu = json.load(f)
            for rjoueur in contenu :
                if rjoueur["Identifiant national"] == self.identifiant :
                    #On commence par vérifier si le joueur existe déjà
                    joueur_voulu = rjoueur["Nom du joueur"]+" "+rjoueur["Prénom du joueur"]
                    break
            if joueur_voulu != "//" :
                reponse = "Le joueur " + joueur_voulu + " existe déjà."
                return reponse
            else :
                #Si le joueur n'existe pas, on peut le créer et ajouter le joueur
                with open(bdd_joueurs, "w") as f :
                    contenu.append(self.dictionnaire())
                    json.dump(contenu, f, indent=4)
                    reponse = "Le joueur a bien été créé."
                    return reponse
        else :
            #Si le fichier JSON pour les joueurs n'existe pas encore, on le crée et on y ajoute le nouveau joueur
            with open(bdd_joueurs, "w") as f :
                json.dump([self.dictionnaire()], f)
                reponse = "Le joueur a bien été créé."
                return reponse
    def consulter_joueur(self):
        bdd_joueurs = "JSON/joueurs.json"
        joueur_voulu = "//"
        if os.path.exists(bdd_joueurs):
            #Si le fichier JSON pour les joueurs existe on peut récupérer le contenu
            with open(bdd_joueurs, 'r') as f :
                contenu = json.load(f)
            for rjoueur in contenu :
                if rjoueur["Identifiant national"] == self.identifiant :
                    #On commence par vérifier si le joueur existe via une boucle et une condition
                    joueur_voulu = rjoueur
                    break
            if joueur_voulu != "//" :
                return joueur_voulu
            else:
                reponse = "ce joueur n'existe pas ! Voulez vous l'enregistrer ?"
                return reponse
        else :
            reponse = "Soit aucun joueur n'a encore été enregistré, soit le fichier JSON a été supprimé. Veuillez contacter l'administrateur."
            return reponse


class ListeJoueurs :
    def recup_liste():
        # On crée le dossier JSON pour stocker les BDD s'il n'existe pas
        os.makedirs("JSON", exist_ok=True)
        bdd_joueurs = "JSON/joueurs.json"
        if os.path.exists(bdd_joueurs):
            # Si le fichier JSON pour les joueurs existe, on récupère la liste des joueurs
            with open(bdd_joueurs, 'r') as f:
                contenu = json.load(f)
                return contenu
        else :
            print("Aucune base de données n'est présente. Merci de contacter votre administrateur !")
            input("Tapez 'ENTER' pour retourner au menu principal")
            controller.controller.Lancement.lancementMenuPrincipal()


class Tournoi :
    def __init__(self, nb_tours, liste_joueurs, nom_tournoi, date_debut, date_fin, lieu_tournoi, commentaire_tournoi):
        self.nb_tours = nb_tours
        self.liste_joueurs = liste_joueurs
        self.nom_tournoi = nom_tournoi
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.lieu_tournoi = lieu_tournoi
        self.commentaire_tournoi = commentaire_tournoi

    def organisationtournoi(self):
        num_tour = 0
        liste_tours = []
        while num_tour < self.nb_tours:
            num_tour += 1
            nom_tour = "Round ", str(num_tour)
            liste_tours.append(nom_tour)
        le_tournoi = [self.nb_tours, self.liste_joueurs, self.nom_tournoi, self.date_debut, self.date_fin, self.lieu_tournoi, self.commentaire_tournoi, liste_tours]
        return le_tournoi

    def fintournoi(self) :
        pass


class Tours :
    def __init__(self, le_tournoi):
        self.le_tournoi = le_tournoi

    def organisationtours(self):
        liste_joueurs = self.le_tournoi[1]
        liste_tours = self.le_tournoi[7]
        nb_match = len(liste_joueurs) // 2
        date_debut_tour = datetime.datetime.now()
        num_match = 0
        liste_matchs = []
        while num_match < nb_match :
            num_match += 1
            nom_match = "M", str(num_match)
            liste_matchs.append(nom_match)
        les_matchs = [date_debut_tour, liste_matchs]
        return les_matchs


class Match :
    def __init__(self, nom_tour, nom_match, liste_joueurs):
        self.nom_tour = nom_tour
        self.nom_match = nom_match
        self.liste_joueurs = liste_joueurs

    def creation_paires(self):
        if self.nom_tour == "Round 1":
            liste_joueurs = random.shuffle(self.liste_joueurs)
        else:
            liste_joueurs = sorted(self.liste_joueurs, key="points", reverse=True)
        paires = []
        paire = []
        for match in self.nom_match :
            paire.append(liste_joueurs[0], liste_joueurs[1])
            liste_joueurs.remove(liste_joueurs[0], liste_joueurs[1])
            joueur_blanc = random.choice(paire)
            paire.remove(joueur_blanc)
            joueur_noir = paire[0]
            dico_paire = {"Blanc" : joueur_blanc, "Noir" : joueur_noir}
            dico_match = {match : dico_paire}
            paires.append(dico_match)
        return paires


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
