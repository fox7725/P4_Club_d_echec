import datetime
import re

from fonctions.fonctions import verification_date


class MenuPrincipal:
    @staticmethod
    def reprise_tournoi():
        print("Il existe actuellement un tournoi en cours")
        tournoi_existe = "réponse"
        while tournoi_existe != "oui" and tournoi_existe != "non":
            tournoi_existe = input("Souhaitez-vous reprendre ? (oui / non)")
            if tournoi_existe == "oui":
                print(" ")
                reprendre = 1
            elif tournoi_existe == "non":
                supprimer = "réponse"
                while supprimer != "oui" and supprimer != "non":
                    supprimer = input("Souhaitez-vous supprimer le tournoi en"
                                      " cours ? (oui / non)")
                    if supprimer == "oui":
                        print(" ")
                        reprendre = 2
                    elif supprimer == "non":
                        print(" ")
                        reprendre = 3
                    else:
                        print(" ")
                        print("Merci de répondre par 'oui' ou par 'non' !")
                        input("Pressez 'ENTER' pour continuer.")
            else:
                print(" ")
                print("Merci de répondre par 'oui' ou par 'non' !")
                input("Pressez 'ENTER' pour continuer.")

        return reprendre

    @staticmethod
    def menu_principal(code_menu_principal):
        # On fait une boucle pour que le menu s'affiche tant que l'utilisateur ne donne pas une réponse autorisée
        while (code_menu_principal != 1 and code_menu_principal != 2 and  code_menu_principal != 3 and
               code_menu_principal != 4):
            print("*" * 66)
            print("-" * 66)
            print("Bienvenue dans le menu principal, merci de faire votre sélection :")
            print("-" * 66)
            print(" ")
            print("1. Commencer un nouveau tournoi")
            print("2. Consulter un ancien tournoi")
            print("3. Gestion des joueurs du club")
            print("4. quitter le programme")
            print(" ")
            print("*" * 66)
            menu_principal = input("Votre réponse :")
            if menu_principal.isdigit():
                code_menu_principal = int(menu_principal)
            else:
                code_menu_principal = 0
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3 ou 4")
                print(" ")
                input("Pressez 'ENTER' pour continuer")
            if (code_menu_principal != 0 and code_menu_principal != 1 and  code_menu_principal != 2 and
                    code_menu_principal != 3 and code_menu_principal != 4):
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3  ou 4")
                print(" ")
                input("Pressez 'ENTER' pour continuer")
        return code_menu_principal


class ViewInformationsTournoi:
    @staticmethod
    def infos_generales_tournoi():
        confirmation = "peut-être"
        while confirmation != "oui":
            confirmation = "peut-être"
            print(" ")
            print("Vous souhaitez débuter un nouveau tournoi. Nous avons donc besoin d'informations complémentaires "
                  "avant de commencer")
            nom_tournoi = input("Quel est le nom du tournoi ?")
            lieu_tournoi = input("Où a lieu le tournoi ?")
            remarque_tournoi = input("Le directeur du tournoi souhaite-t-il ajouter un commentaire ?")
            debut_tournoi_brut = datetime.date.today()
            debut_tournoi = debut_tournoi_brut.strftime("%d/%m/%Y")
            duree_tournoi = input("Combien de jour(s) dure le tournoi ?")
            while not duree_tournoi.isdigit() or int(duree_tournoi) < 0:
                duree_tournoi = input("La valeur entrée n'est pas correcte. Merci de saisir un nombre supérieur à"
                                      " 0 ! Combien de jour(s) dure le tournoi ?")
            duree_tournoi = int(duree_tournoi)
            date_fin_brut = debut_tournoi_brut + datetime.timedelta(
                days=duree_tournoi)
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

            while confirmation != "oui" and confirmation != "non":
                print(" ")
                print("=" * 29)
                print(" ")
                print("Merci de confimer les informations :")
                print("Vous souhaitez organiser le tournoi", nom_tournoi, "de", nb_tours, "tours à partir du",
                      debut_tournoi, "au", fin_tournoi, "à", lieu_tournoi, ".")
                print("Le commentaire saisi par le Directeur est :", remarque_tournoi)
                print(" ")
                print("=" * 29)
                print(" ")
                confirmation = input("Est ce correcte ? (oui / non)")
                if confirmation != "oui" and confirmation != "non":
                    print("Merci de répondre par 'oui' ou par 'non' !")
                    input("Tapez 'ENTER' pour continuer")
            if confirmation == "non":
                print("Merci de resaisir les informations !")
                input("Tapez 'ENTER' pour continuer")
        infos_tournoi = [nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours]
        return infos_tournoi

    @staticmethod
    def demande_nv_joueurs():
        oui_non = "peut-être"
        while oui_non != "oui" and oui_non != "non":
            oui_non = input("Le tournoi se joue-t-il à guichet fermé (seulement les membres du club + invités) ou est"
                            " il ouvert à tous ? (oui / non)")
            if oui_non != "oui" and oui_non != "non":
                print("merci de répondre par 'oui' ou par 'non'")
                input("Tapez 'enter' pour recommencer")
            else:
                return oui_non

    @staticmethod
    def ajout_joueurs_invites(preliste_joueurs):
        if len(preliste_joueurs) == 0 or len(preliste_joueurs) == 1:
            print("Il y a actuellement " + str(len(preliste_joueurs)) + " joueur enregistré dans la base de données")
        else:
            print("Il y a actuellement " + str(len(preliste_joueurs)) + " joueurs enregistrés dans la base de données")

        liste_joueurs = []
        for joueur in preliste_joueurs:
            joueur = {"ID": joueur["Identifiant national"],
                      "nom_joueur": joueur["Nom du joueur"],
                      "prenom_joueur": joueur["Prénom du joueur"],
                      "sexe": joueur["Sexe"],
                      "date_naissance": joueur["Date de naissance"],
                      "points": 0}
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
                    while sexe != "Homme" and sexe != "Femme":
                        sexe = input("Etes-vous un homme ou une femme ?")
                        if sexe != "Homme" and sexe != "Femme":
                            input("Merci de répondre par 'Homme' ou par"
                                  " 'Femme'. Tapez 'ENTER' pour continuer")
                    date_valide = False
                    while not date_valide:
                        date_naissance = input(
                            "Quelle est votre date de naissance (JJ/MM/AAAA)? ")
                        try:
                            date = datetime.datetime.strptime(
                                date_naissance, '%d/%m/%Y').date()
                            print("La date de naissance entrée est valide : ", date)
                            date_valide = True
                        except ValueError:
                            print("La date de naissance entrée est invalide ! Veuillez ressaisir une date.")

                    reponses_formulaire = {
                        "ID": identifiant,
                        "nom_joueur": nom,
                        "prenom_joueur": prenom,
                        "sexe": sexe,
                        "date_naissance": date_naissance,
                        "points": 0
                    }
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

    @staticmethod
    def ajout_joueurs():
        liste_joueurs = []
        是不是 = "oui"
        while 是不是 == "oui":
            id_valide = False
            while not id_valide:
                identifiant = input("Quel est votre Identifiant National ? ")
                if re.match(r'^[a-zA-Z]{2}\d{5}$', identifiant):
                    id_valide = True
                else:
                    print("L'Identifiant National entré est invalide ! Veuillez le ressaisir sous la forme 'XX12345'.")
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

    @staticmethod
    def infos_fin_tournoi(tournoi):
        print(" ")
        print("=" * 29)
        print(" ")
        print("FIN DU TOURNOI", tournoi.nom_tournoi.upper())
        print(" ")
        print("=" * 29)
        print(" ")
        print("Le tournoi d'échec est maintenant terminé, nous vous remercions"
              " d'avoir utilisé ce logiciel de gestion de tournois édité par"
              " Christophe RENARD !")
        if len(tournoi.gagnant) > 1:
            print("Toutes nos félicitations aux gagnants :")
            for joueur in tournoi.gagnant:
                print(joueur.prenom_joueur, joueur.nom_joueur)
        else:
            print("Toutes nos félicitation au gagnant",
                  tournoi.gagnant[0].prenom_joueur,
                  tournoi.gagnant[0].nom_joueur)
        input("Presser 'ENTER' pour retourner au menu principal")

    @staticmethod
    def pret_pour_archivage():
        print("=" * 29)
        print(" ")
        print("Quand vous serez prêt pour terminer le tournoi et l'archiver,"
              " pressez 'ENTER' !")
        print(" ")
        print("=" * 29)
        input("Pressez 'ENTER' pour continuer")

    @staticmethod
    def archivage_tournoi(archivage):
        print("=" * 29)
        print(" ")
        print(archivage)
        print(" ")
        print("=" * 29)
        input("Pressez 'ENTER' pour continuer")


class RapportsTournois:
    @staticmethod
    def menu_rapports():
        code_menu_tournois = 0
        while code_menu_tournois != 1 and code_menu_tournois != 2 and\
                code_menu_tournois != 3:
            print("*" * 66)
            print("-" * 66)
            print("Bienvenue dans le menu visionnage des matchs archivés")
            print("-" * 66)
            print("Que voulez-vous faire, merci de faire votre sélection :")
            print(" ")
            print("1. Afficher la liste des tournois")
            print("2. Afficher les informations générale d'un tournoi")
            print("3. Retour au menu principal")
            print(" ")
            print("*" * 66)
            menu_tournois = input("Votre réponse :")
            if menu_tournois.isdigit():
                code_menu_tournois = int(menu_tournois)
            else:
                code_menu_tournois = 0
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3, ou 4 !")
                print(" ")
            if (code_menu_tournois != 0 and code_menu_tournois != 1 and code_menu_tournois != 2 and
                    code_menu_tournois != 3):
                print(" ")
                print("Merci de choisir parmis les options 1, 2 ou 3 !")
                print(" ")
        return code_menu_tournois

    @staticmethod
    def affichage_liste_tournois(liste_tournois):
        print("Voici l'ensemble des tournois enregistrés dans la base de données :")
        print(" ")
        for tournoi in liste_tournois:
            print(" ")
            print("Nom du tournoi :", tournoi.nom_tournoi, ", commencé le", tournoi.debut_tournoi, "et terminé le",
                  tournoi.fin_tournoi, "à", tournoi.lieu_tournoi)
            print("Nombre de tours :", tournoi.nb_tours, "- Nombre de joueurs :", len(tournoi.liste_joueurs))
            if len(tournoi.gagnant) == 1:
                for gagnant in tournoi.gagnant:
                    print("Le gagnant est le joueur N°", gagnant.identifiant_national, ":", gagnant.prenom_joueur,
                          gagnant.nom_joueur, "avec", gagnant.points, "points.")
            else:
                print("Les gagnants sont :")
                for gagnant in tournoi.gagnant:
                    print("=> Joueur numéro", gagnant.identifiant_national, "Nom :", gagnant.prenom_joueur,
                          gagnant.nom_joueur, "avec", gagnant.points, "points.")
            print(" ")
            print("-" * 66)
        input("Pressez 'ENTER' pour retourner au menu")

    @staticmethod
    def quelle_date_tournoi(liste_tournois):
        print("*" * 66)
        print(" ")
        print("Bienvenue dans le menu visionnage des matchs archivés, quelle est la date de début du match que vous "
              "souhaitez consulter ?")
        print(" ")
        verif_date = 0
        date_existe = 0
        while verif_date == 0 or date_existe == 0:
            date_tournoi = input("Tapez une date au format JJ/MM/AAAA : ")
            verif_date = verification_date(date_tournoi)
            if verif_date == 0:
                print("La date", date_tournoi, "n'est pas une date correcte.")
            if verif_date == 1:
                for tournoi in liste_tournois:
                    if tournoi.debut_tournoi == date_tournoi:
                        date_existe = 1
                        return date_tournoi
                if date_existe == 0:
                    input("Il n'y a pas de tournoi à cette date, merci de saisir une autre date. Pressez 'ENTER' pour"
                          " continuer.")

    @staticmethod
    def affichage_infos_tournoi(date_tournoi, liste_tournois):
        for tournoi in liste_tournois:
            if tournoi.debut_tournoi == date_tournoi:
                print(" ")
                print("*" * 66)
                print(" ")
                print("Vous avez demandé à voir les information du tournoi", tournoi.nom_tournoi, "s'étant déroulé à",
                      tournoi.lieu_tournoi, "du", tournoi.debut_tournoi, "au", tournoi.fin_tournoi, ":")
                print(" ")
                if len(tournoi.gagnant) == 1:
                    for gagnant in tournoi.gagnant:
                        print("Le gagnant est le joueur N°", gagnant.identifiant_national, ":", gagnant.prenom_joueur,
                              gagnant.nom_joueur, "avec", gagnant.points, "points.")
                else:
                    print("Les gagnants sont :")
                    for gagnant in tournoi.gagnant:
                        print("=> Joueur numéro", gagnant.identifiant_national, "Nom :", gagnant.prenom_joueur,
                              gagnant.nom_joueur, "avec", gagnant.points, "points.")
                print(" ")
                print("-" * 66)
                print(" ")
                input("Pressez 'ENTER' pour continuer l'affichage")
                print(" ")
                print("-" * 66)
                print("La liste des joueurs inscrits au tournoi est :")
                # On trie de la liste des joueurs par ordre alphabétique du
                # nom de famille
                liste_joueurs_triee = sorted(tournoi.liste_joueurs, key=lambda x: x.nom_joueur)
                # On fait l'affichage sous forme "numéro : prénom nom"
                for joueur in liste_joueurs_triee:
                    print(f"- {joueur.identifiant_national} : {joueur.prenom_joueur} {joueur.nom_joueur} - "
                          f"{joueur.points} points")
                print(" ")
                print("-" * 66)
                print(" ")
                input("Pressez 'ENTER' pour continuer l'affichage")
                print(" ")
                print("-" * 66)
                print(" ")
                print("Voici la liste des matchs du tournoi :")

                print("Voici la liste des matchs, les joueurs gagnants sont affichés avec une étoile.")

                # Parcourir chaque tour et chaque match
                for tour in tournoi.liste_tours:
                    # Afficher le nom du tour
                    print("=" * 66)
                    print(tour.nom_tour + " :")

                    # Parcourir chaque match dans le tour
                    for match in tour.liste_matchs:
                        # on mémorise les données à afficher
                        impr_joueur1 = ("        Blanc :" + match.joueur_blanc.identifiant_national + " - " +
                                        match.joueur_blanc.nom_joueur + " " + match.joueur_blanc.prenom_joueur + " - "
                                         + str(match.score_JB) + " points.")

                        impr_joueur2 = ("        Noir :" + match.joueur_noir.identifiant_national + " - " +
                                        match.joueur_noir.nom_joueur + " " + match.joueur_noir.prenom_joueur + " - "
                                         + str(match.score_JN) + " points.")

                        # on détermine le joueur gagnant
                        if match.score_JB > match.score_JN:
                            impr_joueur1 += " ***"
                        elif match.score_JN > match.score_JB:
                            impr_joueur2 += " ***"

                        # Afficher les informations du match
                        print("    " + match.nom_match + " :")
                        print(impr_joueur1)
                        print(impr_joueur2)

        print(" ")
        print("-" * 66)
        print(" ")
        input("Pressez 'ENTER' pour retourner au menu")
        print(" ")


class MenuGestionJoueur:
    @staticmethod
    def menujoueur():
        code_menu_joueur = 0
        while code_menu_joueur != 1 and code_menu_joueur != 2 and\
                code_menu_joueur != 3 and code_menu_joueur != 4:
            print("*" * 66)
            print("-" * 66)
            print("Bienvenue dans le menu de gestion des joueur, merci de faire votre sélection :")
            print("-" * 66)
            print(" ")
            print("1. Consulter la liste des joueurs enregistrés")
            print("2. Consulter les informations d'un joueur")
            print("3. Créer un nouveau joueur")
            print("4. Retour au menu principal")
            print(" ")
            print("*" * 66)
            menu_joueur = input("Votre réponse :")
            if menu_joueur.isdigit():
                code_menu_joueur = int(menu_joueur)
            else:
                code_menu_joueur = 0
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3, ou 4 !")
                print(" ")
            if code_menu_joueur != 0 and code_menu_joueur != 1 and code_menu_joueur != 2 and code_menu_joueur != 3 and\
                    code_menu_joueur != 4:
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3, 4 !")
                print(" ")
        return code_menu_joueur

    @staticmethod
    def formulaire_nouveau_joueur():
        # Formulaire pour l'inscription des joueurs dans le JSON en tant que membres de l'association
        print(" ")
        id_valide = False
        while not id_valide:
            identifiant = input("Quel est votre Identifiant National ? ")
            if re.match(r'^[a-zA-Z]{2}\d{5}$', identifiant):
                id_valide = True
            else:
                print("L'Identifiant National entré est invalide ! Veuillez le ressaisir sous la forme 'XX12345'.")
        nom = input("Quel est votre nom ? ")
        prenom = input("Quel est votre prénom ? ")
        sexe = "non binaire"
        while sexe != "H" and sexe != "F":
            sexe = input("Êtes vous un homme ou une femme ? (H / F) ")
            if sexe != "H" and sexe != "F":
                print("Merci de répondre par 'H' pour Homme ou par 'F' pour Femme.")
        verif_date = 0
        while verif_date == 0:
            date_naissance = input("Quelle est votre date de naissance ? ")
            verif_date = verification_date(date_naissance)
            if verif_date == 0:
                print("La valeur entrée (", date_naissance, ") n'est pas une date valide. Merci de recommencer.")
        liste_tournois = []
        moyenne_points = 0
        reponses_formulaire = [identifiant, nom, prenom, sexe, date_naissance, liste_tournois, moyenne_points]
        return reponses_formulaire

    @staticmethod
    def joueur_enregistre(resultat):
        print(resultat)
        oui_non = "peut-être"
        while oui_non != "oui" and oui_non != "non":
            oui_non = input("Voulez vous créer un nouveau joueur ? (oui / non) ")
            if oui_non != "oui" and oui_non != "non":
                print("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
            elif oui_non == "non":
                return False
            elif oui_non == "oui":
                return True

    @staticmethod
    def questionnaire_recherche_joueur():
        identifiant = input("Quel est l'identifiant national du joueur ?")
        return identifiant

    @staticmethod
    def affichage(resultat):
        print("Voici les informations demandées")
        for cle in resultat:
            print(cle, ":", resultat[cle])
        oui_non = "peut-être"
        while oui_non != "oui" and oui_non != "non":
            oui_non = input("Voulez vous consulter un autre joueur ? (oui / non) ")
            if oui_non != "oui" and oui_non != "non":
                print("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
            else:
                return oui_non

    @staticmethod
    def affichage_liste_abonnes(liste_abonnes):
        print("Voici la liste des joueurs enregistrés dans le club :")
        liste_abonnes_triee = sorted(liste_abonnes, key=lambda x: x['Nom du joueur'])
        for abonne in liste_abonnes_triee:
            for cle in abonne:
                print(cle, ":", abonne[cle])
            print("-" * 29)
        input("Pour continuer pressez 'ENTER'")
        return 0


class ViewMatch:
    @staticmethod
    def choix_match(matchs_restant, tour):
        # On commence par afficher la liste des matchs restant dans le tour en cours
        print(" ")
        print("=" * 29)
        print("Vous êtes dans le " + tour + ". Voici la liste des matchs restant à jouer :")
        print(" ")
        for match in matchs_restant:
            print("match :", match.nom_match, "- Joueur Blanc :", match.joueur_blanc.nom_joueur,
                  match.joueur_blanc.prenom_joueur, "- Joueur Noir :", match.joueur_noir.nom_joueur,
                  match.joueur_noir.prenom_joueur)
            print("-" * 29)

        # Puis on demande à l'utilisateur de choisir son match
        while True:
            choix_match = input("Entrez le nom du match dont vous avez le retour ?")
            for recherche_choix_match in matchs_restant:
                if recherche_choix_match.nom_match == choix_match:
                    return recherche_choix_match
            print("Ceci n'est pas un match à jouer")

    @staticmethod
    def declaration_score(match):
        score = "Pas de score"
        while score != "JB" and score != "JN" and score != "N":
            print("=" * 29)
            print(" ")
            print("Résultat du match", match.nom_match, "opposant", match.joueur_blanc.prenom_joueur,
                  match.joueur_blanc.nom_joueur, "vs", match.joueur_noir.prenom_joueur, match.joueur_noir.nom_joueur)
            print(" ")
            print("=" * 29)
            print("- En cas de match nul, répondez 'N'")
            print("- Pour le joueur blanc", match.joueur_blanc.prenom_joueur, match.joueur_blanc.nom_joueur,
                  "répondez 'JB'")
            print("- Pour le joueur noir", match.joueur_noir.prenom_joueur, match.joueur_noir.nom_joueur,
                  "répondez 'JN'")
            score = input("Qui a gagné le match ?")
            print("=" * 29)
            if score != "JB" and score != "JN" and score != "N":
                print("Merci de répondre par 'JB', 'JN' ou 'N' uniquement !")
                input("Pressez 'ENTER' pour continuer")
                print("=" * 29)
            else:
                return score


class Erreurs:
    @staticmethod
    def erreur1():
        print("Aucune base de données n'est présente. Merci de contacter votre administrateur !")
        input("Tapez 'ENTER' pour retourner au menu principal")

    @staticmethod
    def erreur2():
        print("Une erreur s'est produite")
        input("Pressez 'ENTER' pour continuer")

    @staticmethod
    def erreur3():
        print(" ")
        print("Nous n'avons pas pu mettre les informations des joueurs à jour, le fichier 'joueurs.json' est "
              "introuvable")
        print(" ")
        input("Pressez 'ENTER' pour continuer")
