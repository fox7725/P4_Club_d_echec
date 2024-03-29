import sys
import json
import os

from MVC.models import Joueur, Tournoi, Tour, Match, JoueurJSON
from MVC.view import MenuPrincipal, Erreurs, RapportsTournois, MenuGestionJoueur, ViewInformationsTournoi, ViewMatch
from fonctions.fonctions import liste_joueur_JSON, rapports_tournois, suppression_encours, charger_tournoi_en_cours


class Archives:
    @staticmethod
    def consulter_ancien_tournoi():
        # On charge le fichier JSON contenant l'historique des tournois
        rapports = rapports_tournois()
        if rapports == "ERR01":
            Erreurs.erreur1()
            Reprise.reprise()

        # On désérialise les données
        liste_tournois = []
        for t in rapports:
            tournoi = Tournoi.from_json(t)
            # On crée une liste de toutes les instances
            liste_tournois.append(tournoi)

        # On affiche le menu de gestion des rapports
        code_rapport_tournoi = RapportsTournois.menu_rapports()

        # On traite le choix de l'utilisateur
        # code 3 : retour au menu principal
        if code_rapport_tournoi == 3:
            Reprise.reprise()

        # code 1 : affichage de la liste des tournois
        if code_rapport_tournoi == 1:
            RapportsTournois.affichage_liste_tournois(liste_tournois)
            Lancement.lancement_menu_principal(0, 2)

        # code 2 : affichage les informations générale d'un tournoi
        if code_rapport_tournoi == 2:
            # On demande de quel tournoi on veut afficher les informations
            date_tournoi = RapportsTournois.quelle_date_tournoi(liste_tournois)
            RapportsTournois.affichage_infos_tournoi(date_tournoi, liste_tournois)
            Lancement.lancement_menu_principal(0, 2)

    @staticmethod
    def gestion_joueurs():
        # On affiche le menu de la gestion des joueurs
        code_menu_joueur = 0
        while code_menu_joueur == 0:
            code_menu_joueur = MenuGestionJoueur.menujoueur()

            # 1. Consulter la liste des joueurs enregistrés
            if code_menu_joueur == 1:
                liste_joueurs_abonnes = liste_joueur_JSON()
                code_menu_joueur = MenuGestionJoueur.affichage_liste_abonnes(liste_joueurs_abonnes)

            # 2. Consulter les informations d'un joueur
            elif code_menu_joueur == 2:
                oui_non = "oui"
                while oui_non == "oui":
                    # On demande l'identifiant du joueur recherché
                    reponses_formulaire = (MenuGestionJoueur.questionnaire_recherche_joueur())

                    # Charger les données du fichier JSON dans une liste
                    with open("JSON/joueurs.json", "r") as fichier:
                        joueurs_json = json.load(fichier)

                    # Maintenant on peut chercher le joueur voulu dans la liste
                    oui_non = "oui"
                    while oui_non == "oui":
                        for joueur in joueurs_json:
                            if joueur["Identifiant national"] == reponses_formulaire:
                                oui_non = MenuGestionJoueur.affichage(joueur)
                                if oui_non == "non":
                                    code_menu_joueur = 0
                                break

            # 3. Créer un nouveau joueur
            elif code_menu_joueur == 3:
                oui_non = "oui"
                while oui_non == "oui":
                    reponses_formulaire = (MenuGestionJoueur.formulaire_nouveau_joueur())
                    creation = JoueurJSON(reponses_formulaire[0],
                                          reponses_formulaire[1],
                                          reponses_formulaire[2],
                                          reponses_formulaire[3],
                                          reponses_formulaire[4],
                                          reponses_formulaire[5],
                                          reponses_formulaire[6])
                    creation.dictionnaire()
                    resultat = creation.enregistreJoueur()
                    retour = MenuGestionJoueur.joueur_enregistre(resultat)
                    if not retour:
                        oui_non = "non"
                        code_menu_joueur = 0

            # 4. Retour au menu principal
            elif code_menu_joueur == 4:
                Reprise.reprise()

            else:
                Erreurs.erreur2()
                Reprise.reprise()


class Reprise:
    @staticmethod
    def reprise():
        # On vérifie s'il y a un tournoi en cours
        reprendre = 0
        reponse = 0
        verif_encours = "JSON/en_cours/tournoi.json"
        if os.path.exists(verif_encours):
            reprendre = MenuPrincipal.reprise_tournoi()

            # Reprendre le tournoi en cours
            if reprendre == 1:
                reponse = 1

            # Ne pas reprendre et supprimer le tournoi en cours
            if reprendre == 2:
                suppression_encours()
                reponse = MenuPrincipal.menu_principal(reponse)

            # Ne pas reprendre et ne pas supprimer le tournoi en cours
            elif reprendre == 3:
                reponse = MenuPrincipal.menu_principal(reponse)
        else:
            reponse = MenuPrincipal.menu_principal(reponse)

        Lancement.lancement_menu_principal(reprendre, reponse)


class NouveauTournoi:
    @staticmethod
    def mise_en_place():
        # On commence par demander les informations sur le tournoi infos_tournoi = [nom_tournoi,
        # lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours]
        infos_tournoi = ViewInformationsTournoi.infos_generales_tournoi()

        # On demande si on ajoute les joueurs manuellement
        demande_nv_joueur = ViewInformationsTournoi.demande_nv_joueurs()

        if demande_nv_joueur == "oui":
            preliste_joueurs = liste_joueur_JSON()
            if preliste_joueurs == "ERR01":
                liste_joueurs_infos = None
                Erreurs.erreur1()
                Reprise.reprise()
            else:
                liste_joueurs_infos = ViewInformationsTournoi.ajout_joueurs_invites(preliste_joueurs)
        else:
            liste_joueurs_infos = ViewInformationsTournoi.ajout_joueurs()

        # On peut maintenant créer une liste d'objets joueurs
        liste_joueurs = []
        for j in liste_joueurs_infos:
            joueur = Joueur.creation(j)
            liste_joueurs.append(joueur)

        # On crée une instance de tournoi à partir des informations
        # données
        tournoi = Tournoi.creation(infos_tournoi, liste_joueurs)

        # On peut maintenant créer la liste des tours et des matchs
        liste_tours = []
        for num_tour in range(1, tournoi.nb_tours + 1):
            liste_matchs = []
            for num_match in range(1, len(liste_joueurs) // 2 + 1):
                match = Match.initialisation(num_match)
                liste_matchs.append(match)
            tour = Tour.initialisation(num_tour, liste_matchs)
            liste_tours.append(tour)
        tournoi.liste_tours = liste_tours
        # On fait une première sauvegarde du tournoi
        tournoi.to_json()
        return tournoi


class Lancement:
    @staticmethod
    def lancement_menu_principal(reprendre, reponse):
        # S'il n'y a pas de réponse, il faut d'abord vérifier si on doit reprendre un match
        if reponse == 0:
            Reprise.reprise()

        # 1. lancer un  tournoi
        if reponse == 1:
            # Si on souhaite reprendre le tournoi en cours
            if reprendre == 1:
                # On récupère les informations du tournoi
                tournoi_dict = charger_tournoi_en_cours()
                tournoi = Tournoi.from_json(tournoi_dict)

            # Si on commence un nouveau tournoi
            else:
                tournoi = NouveauTournoi.mise_en_place()

            # Le tournoi peut maintenant commencer
            paires_ayant_joue = []
            matchs_restant = []
            for tour in tournoi.liste_tours:
                # On commence par organiser les tours
                # organisation_du_tour = [paires_ayant_joue, match_restant]
                organisation_du_tour = tour.organisation_tour(tournoi, paires_ayant_joue)
                paires_ayant_joue.append(organisation_du_tour[0])
                matchs_restant.extend(organisation_du_tour[1])
                # On sauvegarde pour garder les modifications s'il y en a
                tournoi.to_json()

                # On peut passer à la réception des scores: L'opérateur sélectionne le match dont il a le retour
                while len(matchs_restant) > 0:
                    if len(matchs_restant) == 1:
                        choix_match = matchs_restant[0]
                        matchs_restant.remove(choix_match)
                    if len(matchs_restant) > 1:
                        # L'opérateur choisi le match dont il a le retour
                        choix_match = ViewMatch.choix_match(matchs_restant, tour.nom_tour)
                        matchs_restant.remove(choix_match)

                    # On récupère les scores
                    score = ViewMatch.declaration_score(choix_match)
                    choix_match.score(score)

                    # On sauvegarde après chaque match
                    tournoi.to_json()

            # On termine le tournoi en indiquant le ou les gagnants, puis en enregistrant et en archivant le tout
            # On commence par chercher la valeur du score le plus élevé
            score_max = max(joueur.points for joueur in tournoi.liste_joueurs)
            # On recherche le ou les joueurs qui ont ce score et on met à jour le JSON
            tournoi.gagnant = [joueur for joueur in tournoi.liste_joueurs if joueur.points == score_max]
            tournoi.to_json()

            # On peut maintenant afficher les résultats et les archiver
            ViewInformationsTournoi.infos_fin_tournoi(tournoi)
            ViewInformationsTournoi.pret_pour_archivage()
            # On fait la mise à jour des joueurs du club
            joueurs_tournoi = []
            for j in tournoi.liste_joueurs:
                joueur_tournoi = JoueurJSON(
                    j.identifiant_national,
                    j.nom_joueur,
                    j.prenom_joueur,
                    j.sexe,
                    j.date_naissance,
                    [tournoi.nom_tournoi, tournoi.debut_tournoi, {"score": j.points}],
                    j.points)
                joueurs_tournoi.append(joueur_tournoi)
            maj_joueurs = JoueurJSON.mise_a_jour_tournoi(joueurs_tournoi)
            # On archive le tournoi
            archivage = tournoi.sauvegarde_fin_tournoi()
            ViewInformationsTournoi.archivage_tournoi(archivage, maj_joueurs)

            # Fin du tournoi
            Reprise.reprise()

        # 2. Consulter les anciens tournois
        if reponse == 2:
            Archives.consulter_ancien_tournoi()

        # 3. Gestion des joueurs du club
        if reponse == 3:
            Archives.gestion_joueurs()

        # 4. quitter le programme
        if reponse == 4:
            sys.exit("Merci et à bientôt !")

        else:
            Erreurs.erreur2()
            Reprise.reprise()


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
