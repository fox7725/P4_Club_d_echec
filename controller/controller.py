import sys
import datetime
import random

from view.view import *
from models.models import *

class Lancement :

    def lancementMenuPrincipal() :
        '''Gestion du menu principal et des différentes options (lancement de tournoi, enregistrement de joeurs,
        édition des rapports'''
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

            liste_objets_joueurs = []
            for joueur in liste_joueurs :
                objet_joueurs = Joueur(joueur["ID"], joueur["nom_joueur"], joueur["prenom_joueur"], joueur["sexe"],
                                       joueur["date_naissance"], score_actuel=0)
                liste_objets_joueurs.append(objet_joueurs)

            nom_tournoi = infos_tournoi[0]
            lieu_tournoi = infos_tournoi[1]
            remarque_tournoi = infos_tournoi[2]
            debut_tournoi = infos_tournoi[3]
            fin_tournoi = infos_tournoi[4]
            nb_tours = infos_tournoi[5]
            liste_tours = infos_tournoi[6]

            #Création de l'objet Tournoi
            tournoi=Tournoi(nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi,
                            nb_tours, liste_tours, liste_objets_joueurs)


            liste_joueurs = []
            liste_objets_tours = []
            liste_opposants = []
            for tour in tournoi.liste_tours :
                tournoi.tour_en_cour = tour
                date_debut_tour = ViewInformationTour.lancement_tour(tour)
                liste_joueurs = liste_objets_joueurs
                nb_match = len(liste_joueurs) // 2
                num_match = 0
                liste_matchs = []
                while num_match < nb_match:
                    num_match += 1
                    nom_match = "M" + str(num_match)
                    liste_matchs.append(nom_match)
                if tour == "Round 1":
                    random.shuffle(liste_joueurs)
                else:
                    liste_joueurs.sort(key=lambda x: x.nom_joueur)

                objet_tour = Tour(liste_joueurs, nb_match, liste_matchs, date_debut_tour, date_fin_tour=" ")
                liste_objets_tours.append(objet_tour)

                liste_objet_match = []
                paire = []

                for jeu in liste_matchs :
                    i = 1
                    paire = [liste_joueurs[0], liste_joueurs[i]]
                    if paire in liste_opposants :
                        while paire in liste_opposants and i < len(liste_joueurs) - 1 :
                            i += 1
                            paire = [liste_joueurs[0], liste_joueurs[i]]
                            liste_opposants.append(paire)
                            liste_joueurs.remove(liste_joueurs[0])
                            liste_joueurs.remove(liste_joueurs[i-1])
                            joueur_blanc = random.choice(paire)
                            paire.remove(joueur_blanc)
                            joueur_noir = paire[0]
                            paire.remove(joueur_noir)

                            #on crée l'objet match
                            objet_match = Match(tour, jeu, joueur_blanc, joueur_noir)
                            liste_objet_match.append(objet_match)

                match_joue = objet_tour.liste_matchs_restants


                while len(match_joue) > 1 :
                    jeu = ViewMatch.appel_match(match_joue)
                    #On demande quel match vient de se terminer
                    if jeu in match_joue :
                        score = ViewMatch.declaration_scores(joueur_blanc, joueur_noir, jeu)
                        #On récupère le score de chaque joueur

                        le_match = {}
                        if score == "JB" :
                            le_match = {jeu : ([joueur_blanc, 1], [joueur_noir, 0])}
                            score_a_actu = 1
                            objet_match.score_JB += score_a_actu
                        if score == "JN" :
                            le_match = {jeu : ([joueur_blanc, 0], [joueur_noir, 1])}
                            score_a_actu = 1
                            objet_match.score_JN += score_a_actu
                        if score == "N" :
                            le_match = {jeu : ([joueur_blanc, 0.5], [joueur_noir, 0.5])}
                            score_a_actu = 0.5
                            objet_match.score_JB += score_a_actu
                            objet_match.score_JN += score_a_actu

                        #mise à jour des données du joueur
                        for joueur_cherche in liste_objets_joueurs :
                            if joueur_cherche == joueur_blanc :
                                score_a_actu = joueur_cherche.score_actuel
                                score_actualise = le_match[jeu][0][1] + score_a_actu
                                joueur_cherche.score_actuel = score_actualise
                            if joueur_cherche == joueur_noir:
                                score_a_actu = joueur_cherche.score_actuel
                                score_actualise = le_match[jeu][0][1] + score_a_actu
                                joueur_cherche.score_actuel = score_actualise
                            else :
                                break
                        match_joue.remove(jeu)
                    else :
                        Erreurs.erreur2()

                if len(match_joue) == 1 :
                    pass
                if len(match_joue) < 1:
                    break


            fin_tour = ViewInformationTour.fin_tour(tour)
            tour.date_fin_tour = fin_tour


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
