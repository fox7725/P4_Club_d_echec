import sys
import json
import datetime
import re


class MenuPrincipal :

    #On crée une classe pour appeler le menu principal quand on le souhaite
    def menuprincipal(code_menu_principal) :
        #On fait une boucle pour que le menu s'affiche tant que l'utilisateur ne donne pas une réponse autorisée
        while code_menu_principal != 1 and code_menu_principal != 2 and code_menu_principal != 3 and\
                code_menu_principal != 4 :
            print("*" *66)
            print("-" * 66)
            print("Bienvenue dans le menu principal, merci de faire votre sélection :")
            print("-" *66)
            print(" ")
            print("1. Commencer un nouveau tournoi")
            print("2. Consulter un ancien tournoi")
            print("3. Gestion des joueurs du club")
            print("4. quitter le programme")
            print(" ")
            print("*" *66)
            menu_principal = input("Votre réponse :")
            if menu_principal.isdigit() :
                code_menu_principal = int(menu_principal)
            else :
                code_menu_principal = 0
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3 ou 4")
                print(" ")
                input ("Pressez 'ENTER' pour continuer")
            if code_menu_principal != 0 and code_menu_principal != 1 and code_menu_principal != 2 and\
                    code_menu_principal != 3 and code_menu_principal != 4 :
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3  ou 4")
                print(" ")
                input("Pressez 'ENTER' pour continuer")
        return code_menu_principal


class ViewInformationsTournoi :
    def infos_generales_tournoi():
        confirmation = "peut-être"
        liste_tours = []
        while confirmation != "oui":
            confirmation = "peut-être"
            print(" ")
            print("Vous souhaitez débuter un nouveau tournoi. Nous avons donc besoin d'informations complémentaires avant"
                  "de commencer")
            nom_tournoi = input("Quel est le nom du tournoi ?")
            lieu_tournoi = input("Où a lieu le tournoi ?")
            remarque_tournoi = input("Le directeur du tournoi souhaite-t-il ajouter un commentaire ?")
            debut_tournoi_brut = datetime.date.today()
            debut_tournoi = debut_tournoi_brut.strftime("%d/%m/%Y")
            duree_tournoi = input("Combien de jour(s) dure le tournoi ?")
            while not duree_tournoi.isdigit() and duree_tournoi < 0:
                duree_tournoi = input("La valeur entrée n'est pas correcte. Merci de saisir un nombre supérieur à 0 !")
            duree_tournoi = int(duree_tournoi)
            date_fin_brut = debut_tournoi_brut + datetime.timedelta(days=duree_tournoi)
            fin_tournoi = date_fin_brut.strftime("%d/%m/%Y")
            是不是 = "peut-être"
            while 是不是 != "oui" and 是不是 != "non":
                是不是 = input("Le nombre de tour est fixé à 4 par défaut. Souhaitez vous modifier ?")
                if 是不是 != "oui" and 是不是 != "non":
                    print("Merci de répondre par 'oui' ou par 'non'")
                    input("Tapez 'ENTER' pour recommencer")
                elif 是不是 == "non":
                    nb_tours = 4
                else:
                    q_nb_tours = "pas de nombre"
                    while not q_nb_tours.isdigit():
                        q_nb_tours = input("Combien de tours les joueurs effectueront ?")
                        if q_nb_tours.isdigit():
                            nb_tours = int(q_nb_tours)
                        else:
                            print("Votre réponse n'est pas un nombre.")
                            input("Tapez 'ENTER' pour recommencer")

                num_tour = 0
                while num_tour < nb_tours:
                    num_tour += 1
                    nom_tour = "Round " + str(num_tour)
                    liste_tours.append(nom_tour)


            while confirmation != "oui" and confirmation != "non" :
                print(" ")
                print("=" * 29)
                print(" ")
                print("Merci de confimer les informations :")
                print("Vous souhaitez organiser le tournoi", nom_tournoi, "de", nb_tours, "tours à partir du", debut_tournoi, "au", fin_tournoi, "à",
                      lieu_tournoi, ".")
                print("Le commentaire saisi par le Directeur est :", remarque_tournoi)
                print(" ")
                print("=" * 29)
                print(" ")
                confirmation = input("Est ce correcte ? (oui / non)")
                if confirmation != "oui" and confirmation != "non":
                    print("Merci de répondre par 'oui' ou par 'non' !")
                    input("Tapez 'ENTER' pour continuer")
            if confirmation == "non" :
                print("Merci de resaisir les informations !")
                input("Tapez 'ENTER' pour continuer")
        infos_tournoi = [nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours, liste_tours]
        return infos_tournoi

    def demande_nv_joueurs():
        oui_non = "peut-être"
        while oui_non != "oui" and oui_non != "non":
            oui_non = input("Le tournoi se joue-t-il à guichet fermé (seulement les membres du club + invités) ou est "
                            "il ouvert à tous ? (oui / non)")
            if oui_non != "oui" and oui_non != "non":
                print("merci de répondre par 'oui' ou par 'non'")
                input("Tapez 'enter' pour recommencer")
            else:
                return oui_non


    def ajout_joueurs():
        liste_joueurs = []
        是不是 = "oui"
        while 是不是 == "oui":
            id_valide = False
            while not id_valide:
                identifiant = input("Quel est votre identifiant national ? ")
                if re.match(r'^[a-zA-Z]{2}\d{5}$', identifiant):
                    id_valide = True
                else:
                    print("L'identifiant national entré est invalide ! Veuillez ressaisir un identifiant de la forme"
                          " XX12345.")
            nom = input("Quel est votre nom ?")
            prenom = input("Quel est votre prénom ?")
            sexe = "NSP"
            while sexe != "Homme" and sexe != "Femme":
                sexe = input("Etes-vous un homme ou une femme ?")
                if sexe != "Homme" and sexe != "Femme":
                    input("Merci de répondre par 'Homme' ou par 'Femme'. Tapez 'ENTER' pour continuer")
            date_valide = False
            while not date_valide:
                date_naissance = input("Quelle est votre date de naissance (JJ/MM/AAAA)? ")
                try:
                    date = datetime.datetime.strptime(date_naissance, '%d/%m/%Y').date()
                    print("La date de naissance entrée est valide : ", date)
                    date_valide = True
                except ValueError:
                    print("La date de naissance entrée est invalide ! Veuillez ressaisir une date.")
            reponses_formulaire = {"ID": identifiant, "nom_joueur": nom, "prenom_joueur": prenom, "sexe": sexe,
                                   "date_naissance": date_naissance, "points": 0}
            liste_joueurs.append(reponses_formulaire)
            if len(liste_joueurs) == 0 or len(liste_joueurs) == 1:
                print("Il y a actuellement " + str(len(liste_joueurs)) + " joueur enregistré")
            else:
                print("Il y a actuellement " + str(len(liste_joueurs)) + " joueurs enregistrés")

            是不是 = input("Voulez vous ajouter un nouveau joueur ? (oui / non) ")
            if 是不是 != "oui" and 是不是 != "non":
                print("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
            elif 是不是 == "non":
                return liste_joueurs

    def ajout_joueurs_invites(preliste_joueurs):
        if len(preliste_joueurs) == 0 or len(preliste_joueurs) == 1:
            print("Il y a actuellement " + str(len(preliste_joueurs)) + " joueur enregistré dans la base de données")
        else:
            print("Il y a actuellement " + str(len(preliste_joueurs)) + " joueurs enregistrés dans la base de données")

        liste_joueurs = []
        for joueur in preliste_joueurs:
            joueur = {"ID": joueur["Identifiant national"], "nom_joueur": joueur["Nom du joueur"],
                      "prenom_joueur": joueur["Prénom du joueur"], "sexe": joueur["Sexe"],
                      "date_naissance": joueur["Date de naissance"], "points": 0}
            liste_joueurs.append(joueur)

        o_n = "peut-être"
        while o_n != "oui" and o_n != "non":
            o_n = input("Souhaitez vous ajouter manuellement des invités ? (oui / non)")
            if o_n != "oui" and o_n != "non":
                print("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
            elif o_n == "oui":
                是不是 = "oui"
                while 是不是 == "oui":
                    identifiant = input("Quel est votre identifiant national ?")
                    nom = input("Quel est votre nom ?")
                    prenom = input("Quel est votre prénom ?")
                    sexe = "NSP"
                    while sexe != "Homme" and sexe != "Femme" :
                        sexe = input("Etes-vous un homme ou une femme ?")
                        if sexe != "Homme" and sexe != "Femme" :
                            input("Merci de répondre par 'Homme' ou par 'Femme'. Tapez 'ENTER' pour continuer")
                    date_naissance = input("Quelle est votre date de naissance ?")
                    reponses_formulaire = {"ID": identifiant, "nom_joueur": nom, "prenom_joueur": prenom, "sexe": sexe,
                                           "date_naissance": date_naissance, "points": 0}
                    liste_joueurs.append(reponses_formulaire)
                    if len(liste_joueurs) == 0 or len(liste_joueurs) == 1:
                        print("Il y a actuellement " + str(len(liste_joueurs)) + " joueur enregistré")
                    else:
                        print("Il y a actuellement " + str(len(liste_joueurs)) + " joueurs enregistrés")

                    是不是 = input("Voulez vous ajouter un nouveau joueur ? (oui / non) ")
                    if 是不是 != "oui" and 是不是 != "non":
                        print("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
                    elif 是不是 == "non":
                        return liste_joueurs
            elif o_n == "non":
                return liste_joueurs


class ViewInformationTour :
    def lancement_tour(tour):
        print("=" * 29)
        print(" ")
        print("Quand vous êtes prêts à lancer le ", tour)
        input("pressez 'ENTER'.")
        date_brut_debut_tour = datetime.datetime.now()
        date_debut_tour = date_brut_debut_tour.strftime("%d/%m/%Y à %I:%M%p")
        print(" ")
        print("Merci ! Le ", tour, "commence donc le ", date_debut_tour)
        print(" ")
        print("=" * 29)
        input("pressez 'ENTER'.")
        return date_debut_tour

    def fin_tour(tour):
        print("=" * 29)
        print(" ")
        print("Le ", tour, "est maintenant terminé")
        date_brut_fin_tour = datetime.datetime.now()
        date_fin_tour = date_brut_fin_tour.strftime("%d/%m/%Y à %I:%M%p")
        print("le ", date_fin_tour)
        print(" ")
        print("=" * 29)
        input("pressez 'ENTER' pour continuer.")
        return date_fin_tour


class ViewMatch :
    def appel_match(match_joue):
        jeu = "pas de match"
        while jeu not in match_joue :
            print("Voici la liste des matchs restant à jouer :", match_joue)
            jeu = input("De quel match avez vous le retour ?")
            if jeu in match_joue :
                return jeu
            else :
                print("Ceci n'est pas un match à jouer")

    def declaration_scores(joueur_blc, joueur_nr, nom_match):
        score = "Pas de score"
        while score != "JB" and score != "JN" and score != "N" :
            print("=" * 29)
            print(" ")
            print("Résultat du match", nom_match, "opposant", joueur_blc.prenom_joueur, joueur_blc.nom_joueur,
                  "vs", joueur_nr.prenom_joueur, joueur_nr.nom_joueur)
            print(" ")
            print("=" * 29)
            print("- En cas de match nul, répondez 'N'")
            print("- Pour le joueur blanc", joueur_blc.prenom_joueur, joueur_blc.nom_joueur, "répondez 'JB'")
            print("- Pour le joueur noir", joueur_nr.prenom_joueur, joueur_nr.nom_joueur, "répondez 'JN'")
            score = input("Qui a gagné le match ?")
            if score != "JB" and score != "JN" and score != "N" :
                print("Merci de répondre par 'JB', 'JN' ou 'N' uniquement !")
                input("Pressez 'ENTER' pour continuer")
            else :
                return score


class Erreurs :
    def erreur1():
        print("Aucune base de données n'est présente. Merci de contacter votre administrateur !")
        input("Tapez 'ENTER' pour retourner au menu principal")

    def erreur2():
        print("Une erreur s'est produite, merci de recommencer !")
        input("Tapez 'ENTER' pour retourner au menu principal")


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
