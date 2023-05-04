import json
import os
import random
import datetime


class Joueur :
    def __init__(self, identifiant_nationale, nom_joueur, prenom_joueur, sexe, date_naissance, score_actuel = 0):
        self.identifiant_nationale = identifiant_nationale
        self.nom_joueur = nom_joueur
        self.prenom_joueur = prenom_joueur
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.score_actuel = score_actuel


class Tournoi :
    def __init__(self, nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours, liste_joueurs,
                 tour_en_cours = " ", gagnant = " " ):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.remarque_tournoi = remarque_tournoi
        self.debut_tournoi = debut_tournoi
        self.fin_tournoi = fin_tournoi
        self.nb_tours = nb_tours
        self.liste_joueurs = liste_joueurs
        self.gagnant = gagnant


class Tour :
    def __init__(self, nom_tour, liste_joueurs, nb_matchs, date_debut_tour, date_fin_tour = " "):
        self.nom_tour = nom_tour
        self.liste_joueurs = liste_joueurs
        self.nb_matchs = nb_matchs
        self.date_debut_tour = date_debut_tour
        self.date_fin_tour = date_fin_tour


class Match :
    def __init__(self,nom_tour, nom_match, joueur_blanc, joueur_noir, score_JB = 0, score_JN = 0):
        self.nom_tour = nom_tour
        self.nom_match = nom_match
        self.joueur_blanc = joueur_blanc
        self.joueur_noir = joueur_noir
        self.score_JB = score_JB
        self.score_JN = score_JN


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
