import sys

import models.models
import view.view
from view.view import *
from models.models import *

class Lancement :

    def lancementMenuPrincipal() :
        reponse = 0
        reponse = MenuPrincipal.menuprincipal(reponse)

        if reponse == 1 :
        #1. Commencer un nouveau tournoi
            infos_tournoi = ViewInformationsTournoi.infos_generales_tournoi()
            #contient : nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours, liste_tours

            demande_nv_joueur = ViewInformationsTournoi.demande_nv_joueurs()
            #On demande à l'organisateur s'il veut récupérer la liste des joueurs (réponse "oui")
            #ou s'il veut la créer ("non")
            if demande_nv_joueur == "oui" :
                preliste_joueurs = Joueurs.liste_joueur_JSON()
                if preliste_joueurs == "ERR01" :
                    Erreurs.erreur1()
                    Lancement.lancementMenuPrincipal()
                else :
                    liste_joueurs = ViewInformationsTournoi.ajout_joueurs_invites(preliste_joueurs)
            else :
                liste_joueurs = ViewInformationsTournoi.ajout_joueurs()

            joueurs = []
            for joueur in liste_joueurs :
                objet_joueurs = Joueur(joueur[0], joueur[1], joueur[2], joueur[3], joueur[4], joueur[5], joueur[6], score_actuel=0)

            nom_tournoi = infos_tournoi[0]
            lieu_tournoi = infos_tournoi[1]
            remarque_tournoi = infos_tournoi[2]
            debut_tournoi = infos_tournoi[3]
            fin_tournoi = infos_tournoi[4]
            nb_tours = infos_tournoi[5]
            liste_tours = infos_tournoi[6]

            tournoi=models.models.Tournoi(nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi,
                                          nb_tours, liste_tours, liste_joueurs)
            #Création de l'objet Tournoi


        elif reponse == 2 :
        #2. Consulter un ancien tournoi
            print(reponse)
            Lancement.lancementMenuPrincipal()

        elif reponse == 3 :
        #3. Gestion des joueurs du club
            print(reponse)
            Lancement.lancementMenuPrincipal()

        elif reponse == 4 :
        #4. quitter le programme
            sys.exit("Merci et à bientôt !")

        else :
            print("Une erreur s'est produite")
            input("Pressez 'ENTER' pour continuer")
            Lancement.lancementMenuPrincipal()


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")