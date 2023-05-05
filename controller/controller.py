import sys
import datetime
import random

from view.view import *
from models.models import *
from fonctions.fonctions import *

class Lancement :
    '''Gestion du menu principal et des différentes options (lancement de tournoi, enregistrement de joeurs,
            édition des rapports'''

    @staticmethod
    def lancementMenuPrincipal() :
        reponse = 0
        reponse = MenuPrincipal.menuprincipal(reponse)
        if reponse == 1 :
        #1. Commencer un nouveau tournoi
            infos_tournoi = ViewInformationsTournoi.infos_generales_tournoi()

            demande_nv_joueur = ViewInformationsTournoi.demande_nv_joueurs()
            #On demande à l'organisateur s'il veut récupérer la liste des joueurs (réponse "oui") ou s'il veut
            #la créer ("non")
            if demande_nv_joueur == "oui" :
                preliste_joueurs = liste_joueur_JSON()
                if preliste_joueurs == "ERR01" :
                    Erreurs.erreur1()
                    Lancement.lancementMenuPrincipal()
                else :
                    liste_joueurs = ViewInformationsTournoi.ajout_joueurs_invites(preliste_joueurs)
            else :
                liste_joueurs = ViewInformationsTournoi.ajout_joueurs()

            #Création des objets joueur et concaténation en liste
            liste_objets_joueurs = []
            for j in liste_joueurs :
                joueur = Joueur(j["ID"], j["nom_joueur"], j["prenom_joueur"], j["sexe"],
                                       j["date_naissance"], score_actuel=0)
                liste_objets_joueurs.append(joueur)

            # Création de l'objet Tournoi
            nom_tournoi = infos_tournoi[0]
            lieu_tournoi = infos_tournoi[1]
            remarque_tournoi = infos_tournoi[2]
            debut_tournoi = infos_tournoi[3]
            fin_tournoi = infos_tournoi[4]
            nb_tours = infos_tournoi[5]
            tournoi = Tournoi(nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi,
                              nb_tours, liste_objets_joueurs)

            #On créé les itérations des tours via une première boucle
            num_tour = 0
            while num_tour < tournoi.nb_tours:
                num_tour += 1
                #On nomme les tours : 'Round 1', 'Round 2', ...
                nom_tour = "Round " + str(num_tour)

                #Dans les tours, on doit classer les joueurs en fonction de leur score et du nom (random si 1er tour)
                #On commence par créer une variable contenant la liste des joueurs de ce tout
                liste_joueurs_tour = []
                for j in tournoi.liste_joueurs :
                    liste_joueurs_tour.append(j)
                if nom_tour == "Round 1":
                    random.shuffle(liste_joueurs_tour)
                else:
                    liste_joueurs_tour.sort(key=lambda x: (-x.score_actuel, x.nom_joueur))

                #Dans les tours, on doit savoir combien il y a de match
                nb_match = len(liste_joueurs_tour) // 2

                #On récupère la date et l'heure du début du tour et on les affiche à l'utilisateur
                date_debut_tour = ViewInformationTour.lancement_tour(nom_tour, nb_match)

                #On peut maintenant créer l'objet tour
                tour = Tour(nom_tour, liste_joueurs_tour, nb_match, date_debut_tour, date_fin_tour=" ")

                #On va maintenant pouvoir créer une nouvelle boucle pour créer les matchs
                liste_paires_passees = []
                liste_matchs = []
                num_match = 0
                while num_match < nb_match:
                    num_match += 1
                    #On nomme les matchs : 'M1', 'M2', ...
                    nom_match = "M" + str(num_match)

                    #On doit associer une paire de joueur à chaque match en veillant à ce qu'ils n'aient déjà joué
                    #aucun match ensemble
                    i = 1
                    paire = [liste_joueurs_tour[0], liste_joueurs_tour[i]]
                    if paire in liste_paires_passees:
                        while paire in liste_paires_passees and i < len(liste_joueurs_tour) - 1:
                            i += 1
                            paire = [liste_joueurs_tour[0], liste_joueurs_tour[i]]

                    #On ajoute la paire de joueur dans une variable pour éviter qu'ils ne rejouent ensemble
                    liste_paires_passees.append(paire)

                    #On choisit au hasard dans la paire pour la couleur de chaque joueur
                    liste_joueurs_tour.remove(liste_joueurs_tour[0])
                    liste_joueurs_tour.remove(liste_joueurs_tour[i - 1])
                    joueur_blanc = random.choice(paire)
                    paire.remove(joueur_blanc)
                    joueur_noir = paire[0]
                    paire.remove(joueur_noir)

                    # on crée l'objet match
                    match = Match(tour.nom_tour, nom_match, joueur_blanc, joueur_noir)

                    # on fait une liste avec tous les matchs
                    liste_matchs.append(match)

                    #on définit la variable qui contiendra les matchs restant à jouer dans le tour
                    liste_matchs_restant = liste_matchs

                #L'opérateur sélectionne le match dont il a le retour
                while len(liste_matchs_restant) > 0 :
                    if len(liste_matchs_restant) > 1 :
                        choix_match = ViewMatch.choix_match(liste_matchs_restant)
                        liste_matchs_restant.remove(choix_match)
                    else :
                        choix_match = liste_matchs_restant[0]
                        liste_matchs_restant.remove(choix_match)

                    #On récupère ensuite les score
                    score = ViewMatch.declaration_scores(choix_match)

                    #On attribue les points à chaque joueur
                    le_match = {}
                    if score == "JB":
                        le_match = {choix_match: ([match.joueur_blanc, 1], [match.joueur_noir, 0])}
                        score_a_actu = 1
                    if score == "JN":
                        le_match = {choix_match: ([match.joueur_blanc, 0], [match.joueur_noir, 1])}
                        score_a_actu = 1
                    if score == "N":
                        le_match = {choix_match: ([match.joueur_blanc, 0.5], [match.joueur_noir, 0.5])}
                        score_a_actu = 0.5

                    # mise à jour des données du joueur
                    for joueur_cherche in tournoi.liste_joueurs:
                        if joueur_cherche == match.joueur_blanc.identifiant_nationale:
                            score_a_actu = joueur_cherche.score_actuel
                            score_actualise = le_match[jeu][0][1] + score_a_actu
                            joueur_cherche.score_actuel = score_actualise
                        if joueur_cherche == match.joueur_noir:
                            score_a_actu = joueur_cherche.score_actuel
                            score_actualise = le_match[jeu][0][1] + score_a_actu
                            joueur_cherche.score_actuel = score_actualise
                        else:
                            break

                date_fin_de_tour = ViewInformationTour.fin_tour(tour.nom_tour)

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
