import sys
import datetime
import random
import json

from view.view import *
from models.models import *
from fonctions.fonctions import *


class Lancement:
    '''Gestion du menu principal et des différentes options (lancement de
     tournoi, enregistrement de joeurs, édition des rapports'''

    @staticmethod
    def lancementMenuPrincipal(reponse):
        if reponse == 0:
            reponse = MenuPrincipal.menuprincipal(reponse)

        # 1. Commencer un nouveau tournoi
        if reponse == 1:
            infos_tournoi = ViewInformationsTournoi.infos_generales_tournoi()

            demande_nv_joueur = ViewInformationsTournoi.demande_nv_joueurs()

            # On demande à l'organisateur s'il veut récupérer la liste des
            # joueurs (réponse "oui") ou s'il veut la créer ("non")
            if demande_nv_joueur == "oui":
                preliste_joueurs = liste_joueur_JSON()
                if preliste_joueurs == "ERR01":
                    Erreurs.erreur1()
                    Lancement.lancementMenuPrincipal(0)
                else:
                    liste_joueurs = ViewInformationsTournoi.ajout_joueurs_invites(preliste_joueurs)
            else:
                liste_joueurs = ViewInformationsTournoi.ajout_joueurs()

            # Création des objets joueur et concaténation en liste
            liste_objets_joueurs = []
            for j in liste_joueurs:
                joueur = Joueur(j["ID"], j["nom_joueur"], j["prenom_joueur"],
                                j["sexe"], j["date_naissance"], score_actuel=0)
                liste_objets_joueurs.append(joueur)

            # Création de l'objet Tournoi
            nom_tournoi = infos_tournoi[0]
            lieu_tournoi = infos_tournoi[1]
            remarque_tournoi = infos_tournoi[2]
            debut_tournoi = infos_tournoi[3]
            fin_tournoi = infos_tournoi[4]
            nb_tours = infos_tournoi[5]
            tournoi = Tournoi(nom_tournoi, lieu_tournoi, remarque_tournoi,
                              debut_tournoi, fin_tournoi, nb_tours,
                              liste_objets_joueurs)
            # On sauvegarde le tournoi lancé et la liste des joueurs pour les
            # récupérer en cas de coupure
            tournoi.sauver_tournoi()
            tournoi.sauver_joueurs()

            # On créé les itérations des tours via une première boucle
            liste_tours = []
            liste_matchs_joues = []
            num_tour = 0
            while num_tour < tournoi.nb_tours:
                num_tour += 1
                # On nomme les tours : 'Round 1', 'Round 2', ...
                nom_tour = "Round " + str(num_tour)

                # Dans les tours, on doit classer les joueurs en fonction de
                # leur score et du nom (random si 1er tour)
                # On commence par créer une variable contenant la liste des
                # joueurs de ce tout
                liste_joueurs_tour = []
                for j in tournoi.liste_joueurs:
                    liste_joueurs_tour.append(j)
                if nom_tour == "Round 1":
                    random.shuffle(liste_joueurs_tour)
                else:
                    liste_joueurs_tour.sort(key=lambda x: (-x.score_actuel,
                                                           x.nom_joueur))

                # Dans les tours, on doit savoir combien il y a de match
                nb_match = len(liste_joueurs_tour) // 2

                # On récupère la date et l'heure du début du tour et on les
                # affiche à l'utilisateur
                date_debut_tour = ViewInformationTour.lancement_tour(nom_tour,
                                                                     nb_match)

                # On peut maintenant créer l'objet tour
                tour = Tour(num_tour, nom_tour, liste_joueurs_tour, nb_match,
                            date_debut_tour, date_fin_tour=" ")

                # On va maintenant pouvoir créer une nouvelle boucle pour créer
                # les matchs
                liste_paires_passees = []
                liste_matchs = []
                num_match = 0
                while num_match < nb_match:
                    num_match += 1
                    # On nomme les matchs : 'M1', 'M2', ...
                    nom_match = "M" + str(num_match)

                    # On doit associer une paire de joueur à chaque match en
                    # veillant à ce qu'ils n'aient pas déjà joué ensemble
                    i = 1
                    paire = [liste_joueurs_tour[0], liste_joueurs_tour[i]]
                    if paire in liste_paires_passees:
                        while paire in liste_paires_passees and\
                                i < len(liste_joueurs_tour) - 1:
                            i += 1
                            paire = [liste_joueurs_tour[0],
                                     liste_joueurs_tour[i]]

                    # On ajoute la paire de joueur dans une variable pour
                    # éviter qu'ils ne rejouent ensemble
                    liste_paires_passees.append(paire)

                    # On choisit au hasard dans la paire pour la couleur de
                    # chaque joueur
                    liste_joueurs_tour.remove(liste_joueurs_tour[0])
                    liste_joueurs_tour.remove(liste_joueurs_tour[i - 1])
                    joueur_blanc = random.choice(paire)
                    paire.remove(joueur_blanc)
                    joueur_noir = paire[0]
                    paire.remove(joueur_noir)

                    # on crée l'objet match
                    match = Match(tour.nom_tour, nom_match, joueur_blanc,
                                  joueur_noir)

                    # on fait une liste avec tous les matchs
                    liste_matchs.append(match)
                    # on définit la variable qui contiendra les matchs restant
                    # à jouer dans le tour
                    liste_matchs_restant = liste_matchs.copy()

                # L'opérateur sélectionne le match dont il a le retour
                liste_tuples_matchs_tour = []
                while len(liste_matchs_restant) > 0:
                    if len(liste_matchs_restant) > 1:
                        choix_match = ViewMatch.choix_match(liste_matchs_restant)
                        liste_matchs_restant.remove(choix_match)
                    else:
                        choix_match = liste_matchs_restant[0]
                        liste_matchs_restant.remove(choix_match)
                    # On récupère ensuite les score
                    score = ViewMatch.declaration_scores(choix_match)
                    choix_match.score(score)
                    liste_matchs_joues.append(choix_match)

                    # On fait le tuple demandé qu'on va aussi utiliser dans les
                    # saugardes
                    tuple_match_joue = {choix_match.nom_match:
                        (
                            [
                                {
                                    choix_match.joueur_blanc.identifiant_national: [
                                        choix_match.joueur_blanc.prenom_joueur,
                                        choix_match.joueur_blanc.nom_joueur
                                    ]
                                },
                                choix_match.score_JB
                            ],
                            [
                                {
                                    choix_match.joueur_noir.identifiant_national: [
                                        choix_match.joueur_noir.prenom_joueur,
                                        choix_match.joueur_noir.nom_joueur
                                    ]
                                },
                                choix_match.score_JN
                            ]
                        )
                    }
                    liste_tuples_matchs_tour.append(tuple_match_joue)

                # Mise à jour des scores des joueurs dans le JSON
                tournoi.sauver_joueurs()

                # Affichage de fin du tour et enregistrement de la date
                date_fin_de_tour = ViewInformationTour.fin_tour(tour.nom_tour,
                                                                tournoi.liste_joueurs)
                # Mise à jour de la date de fin du tour
                tour.date_fin_tour = date_fin_de_tour

                # On ajoute le tour terminé dans une liste et on sauvegarde
                # dans un JSON
                liste_tours.append(tour)
                tour.sauvegarde_tour(liste_tours, liste_tuples_matchs_tour)

            # On termine le tournoi en indiquant le ou les gagnants, puis en
            # enregistrant et en archivant le tout
            # On commence par chercher la valeur du score le plus élevé
            score_max = max(joueur.score_actuel for joueur in
                            tournoi.liste_joueurs)
            # On recherche le ou les joueurs qui ont ce score
            liste_gagnants = [joueur for joueur in tournoi.liste_joueurs if
                              joueur.score_actuel == score_max]

            # On affiche le résultat du tournoi
            liste_ID_gagnants = []
            for gagnant in liste_gagnants:
                liste_ID_gagnants.append(gagnant.identifiant_national)
            tournoi.gagnant = liste_ID_gagnants
            tournoi.sauver_tournoi()
            ViewInformationsTournoi.infos_fin_tournoi(liste_gagnants, tournoi)

            # On archive le tournoi et on supprime les JSON temporaires
            ViewInformationsTournoi.pret_pour_archivage()
            archivage_tournoi = tournoi.sauvegarde_fin_tournoi(liste_tours)
            ViewInformationsTournoi.archivage_tournoi(archivage_tournoi)

            # S'il s'agissait d'un tournoi à guichet fermé, il faut mettre à
            # jour la liste des joueurs
            if demande_nv_joueur == "oui":
                for joueur_a_modifier in tournoi.liste_joueurs:
                    retour_mise_a_jour = joueur_a_modifier.mise_a_jour_fin_tournoi(tournoi.nom_tournoi,
                                                                                   tournoi.debut_tournoi)
                    if retour_mise_a_jour == 0:
                        Erreurs.erreur3()
                        break

            # retour au menu principal
            Lancement.lancementMenuPrincipal(0)

        # 2. Consulter les anciens tournois
        elif reponse == 2:

            # On charge le fichier JSON contenant l'historique des tournois
            rapports = rapports_tournois()
            if rapports == "ERR01":
                Erreurs.erreur1()

            # On désérialise les données
            liste_tournois = []
            for tournoi in rapports:
                nom_tournoi = tournoi["nom_tournoi"]
                lieu_tournoi = tournoi["lieu_tournoi"]
                remarque_tournoi = tournoi["remarque_tournoi"]
                debut_tournoi = tournoi["debut_tournoi"]
                fin_tournoi = tournoi["fin_tournoi"]
                nb_tours = tournoi["nb_tours"]
                liste_matchs = tournoi["liste_matchs"]
                liste_joueurs = tournoi["liste_joueurs"]
                gagnant = tournoi["gagnant"]

                # On crée une instance par tournoi
                tournoi_instance = TournoisJSON(nom_tournoi, lieu_tournoi,
                                                remarque_tournoi,
                                                debut_tournoi, fin_tournoi,
                                                nb_tours, liste_matchs,
                                                liste_joueurs, gagnant)

                # On crée une liste de toutes les instances
                liste_tournois.append(tournoi_instance)

            # On affiche le menu de gestion des rapports
            code_rapport_tournoi = RapportsTournois.menu_rapports()

            # On traite le choix de l'utilisateur
            # code 5 : retour au menu principal
            if code_rapport_tournoi == 3:
                Lancement.lancementMenuPrincipal(0)

            # code 1 : affichage de la liste des tournois
            if code_rapport_tournoi == 1:
                RapportsTournois.affichage_liste_tournois(liste_tournois)
                Lancement.lancementMenuPrincipal(2)

            # code 2 : affichage les informations générale d'un tournoi
            if code_rapport_tournoi == 2:
                # On demande de quel tournoi on veut afficher les informations
                date_tournoi = RapportsTournois.quelle_date_tournoi(liste_tournois)
                RapportsTournois.affichage_infos_tournoi(date_tournoi, liste_tournois)
                Lancement.lancementMenuPrincipal(2)

        # 3. Gestion des joueurs du club
        elif reponse == 3:
            # On affiche le menu de la gestion des joueurs
            code_menu_joueur = 0
            while code_menu_joueur == 0:
                code_menu_joueur = MenuGestionJoueur.menujoueur()

                # On traite le choix de l'utilisateur
                if code_menu_joueur == 1:
                    liste_joueurs_abonnes = liste_joueur_JSON()
                    code_menu_joueur = MenuGestionJoueur.affichage_liste_abonnes(liste_joueurs_abonnes)

                elif code_menu_joueur == 2:
                    oui_non = "oui"
                    while oui_non == "oui":
                        # On demande l'identifiant du joueur recherché
                        reponses_formulaire = MenuGestionJoueur.questionnaire_recherche_joueur()

                        # Charger les données du fichier JSON dans une liste
                        with open("JSON/joueurs.json", "r") as fichier:
                            joueurs_json = json.load(fichier)

                        # Maintenant on peut chercher le joueur voulu dans la
                        # liste
                        oui_non = "oui"
                        while oui_non == "oui":
                            for joueur in joueurs_json:
                                if joueur["Identifiant national"] == reponses_formulaire:
                                    oui_non = MenuGestionJoueur.affichage(joueur)
                                    if oui_non == "non":
                                        code_menu_joueur = 0
                                    break

                elif code_menu_joueur == 3:
                    oui_non = "oui"
                    while oui_non == "oui":
                        reponses_formulaire = MenuGestionJoueur.formulaire_nouveau_joueur()
                        creation = JoueurJSON(reponses_formulaire[0],
                                              reponses_formulaire[1],
                                              reponses_formulaire[2],
                                              reponses_formulaire[3],
                                              reponses_formulaire[4],
                                              reponses_formulaire[5],
                                              reponses_formulaire[6],
                                              reponses_formulaire[7])
                        creation.dictionnaire()
                        resultat = creation.enregistreJoueur()
                        retour = MenuGestionJoueur.joueur_enregistre(resultat)
                        if not retour:
                            oui_non = "non"
                            code_menu_joueur = 0

                elif code_menu_joueur == 4:
                    Lancement.lancementMenuPrincipal(0)

                else:
                    Erreurs.erreur2()

        # 4. quitter le programme
        elif reponse == 4:
            sys.exit("Merci et à bientôt !")

        else:
            Erreurs.erreur2()


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
