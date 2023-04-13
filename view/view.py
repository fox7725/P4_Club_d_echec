import sys
import json
import datetime

from models.models import ListeJoueurs


class MenuPrincipal :
    #On crée une classe pour appeler le menu principal quand on le souhaite

    def __init__(self):
        self.code_menu_principal = 0
    def menuprincipal(self) :
        #On fait une boucle pour que le menu s'affiche tant que l'utilisateur ne donne pas une réponse autorisée
        while self.code_menu_principal != 1 and self.code_menu_principal != 2 and self.code_menu_principal != 3 and self.code_menu_principal != 4 :
            print("*" *66)
            print("-" * 66)
            print("Bienvenue dans le menu principal, merci de faire votre sélection :")
            print("-" *66)
            print(" ")
            print("1. Commencer un nouveau tournoi")
            print("2. Consulter un ancien tournoi")
            print("3. Consulter la liste des joueurs enregistrés")
            print("4. quitter le programme")
            print(" ")
            print("*" *66)
            menu_principal = input("Votre réponse :")
            if menu_principal.isdigit() :
                self.code_menu_principal = int(menu_principal)
            else :
                self.code_menu_principal = 0
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3 ou 4")
                print(" ")
            if self.code_menu_principal != 0 and self.code_menu_principal != 1 and self.code_menu_principal != 2 and self.code_menu_principal != 3 and self.code_menu_principal != 4 :
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3  ou 4")
                print(" ")
        return self.code_menu_principal


class TournoiView :

    def demandejoueur() :
        oui_non = "peut-être"
        while oui_non != "oui" and oui_non != "non" :
            oui_non = input("Souhaitez vous enregistrer manuellement les joueurs avant de lancer le tournoi ?")
            if oui_non != "oui" and oui_non != "non" :
                print("merci de répondre par 'oui' ou par 'non'")
                input("Tapez 'enter' pour recommencer")
            else :
                return oui_non

    def nombretours() :
        nb_tours = 4
        q_nb_tours = "pas de nombre"
        oui_non = "peut-être"
        while oui_non != "oui" and oui_non != "non":
            oui_non = input("Le nombre de tour est fixé à 4 par défaut. Souhaitez vous modifier ?")
            if oui_non != "oui" and oui_non != "non":
                print("Merci de répondre par 'oui' ou par 'non'")
                input("Tapez 'ENTER' pour recommencer")
            elif oui_non == "non":
                return nb_tours
            else :
                while not q_nb_tours.isdigit():
                    q_nb_tours = input("Combien de tours les joueurs effectueront ?")
                    if q_nb_tours.isdigit():
                        nb_tours = int(q_nb_tours)
                        return nb_tours
                    else:
                        print("Votre réponse n'est pas un nombre.")
                        input("Tapez 'ENTER' pour recommencer")

    def infostournoi():
        confirmation = "non"
        while confirmation == "non" :
            date_debut = datetime.datetime.today()
            nom_tournoi = input("Quel est le nom du tournoi que vous souhaitez commencer ?")
            duree_tournoi = "ceci n'est pas un nombre"
            while not duree_tournoi.isdigit() :
                duree_tournoi = input("Combien de jour(s) dure le tournoi ?")
                if duree_tournoi.isdigit() :
                    duree_tournoi = int(duree_tournoi)
                    date_fin = date_debut + timedelta(days=duree_tournoi)
                else :
                    print("La valeur entrée n'est pas correcte, merci de saisir un nombre !")
            lieu_tournoi = input("Où a lieu le tournoir ?")
            commentaire_tournoi = input("Le directeur peut ajouter ici ses remarques concernant le tournoi :")
            confirmation = "peut-être"
            while confirmation != "oui" and confirmation != "non" :
                print("Merci de confimer les informations :")
                print("Vous souhaitez organiser le tournoi ", nom_tournoi, " à partir du ", date_debut, " au ", date_fin, " à ", lieu_tounoi, ".")
                print("Le commentaire saisi par le Directeur est : ", commentaire_tournoi)
                confirmation = input("Est ce correcte ? (oui / non")
                if confirmation == "oui" :
                    reponses = [nom_tournoi, date_debut, date_fin, lieu_tournoi, commentaire_tournoi]
                    return reponses
                if confirmation != "oui" and confirmation != "non" :
                    print("Merci de répondre par 'oui' ou par 'non' !")
                    input("Tapez 'ENTER' pour continuer")


class MenuConsulterTournoi :
    pass


class MenuConsulterListeJoueur :
    def __init__(self):
        self.code_menu_joueur = 0
    def menujoueur(self):
        while self.code_menu_joueur != 1 and self.code_menu_joueur != 2 and self.code_menu_joueur != 3 and self.code_menu_joueur != 4 :
            print("*" *66)
            print("-" * 66)
            print("Bienvenue dans le menu de gestion des joueur, merci de faire votre sélection :")
            print("-" *66)
            print(" ")
            print("1. Consulter la liste des joueurs enregistrés")
            print("2. Consulter les informations d'un joueur")
            print("3. Créer un nouveau joueur")
            print("4. Retour au menu principal")
            print(" ")
            print("*" *66)
            menu_joueur = input("Votre réponse :")
            if menu_joueur.isdigit() :
                self.code_menu_joueur = int(menu_joueur)
            else :
                self.code_menu_joueur = 0
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3, ou 4 !")
                print(" ")
            if self.code_menu_joueur != 0 and self.code_menu_joueur != 1 and self.code_menu_joueur != 2 and self.code_menu_joueur != 3 and self.code_menu_joueur != 4 :
                print(" ")
                print("Merci de choisir parmis les options 1, 2, 3, 4 !")
                print(" ")
        return self.code_menu_joueur


class FormulaireNouveauJoueur :

    def questionnaire():
        #Formulaire pour l'inscription des joueurs dans le JSON en tant que membres de l'association
        print(" ")
        identifiant = input("Quel est votre identifiant national ?")
        nom = input("Quel est votre nom ?")
        prenom = input("Quel est votre prénom ?")
        sexe = input("Êtes vous un homme ou une femme ?")
        date_naissance = input("Quelle est votre date de naissance ?")
        remarque = " "
        liste_tournois = 0
        moyenne_points = 0
        reponses_formulaire = [identifiant, nom, prenom, sexe, date_naissance, remarque, liste_tournois, moyenne_points]
        return reponses_formulaire

    def questionnairejoueurtournoi():
        #Formulaire pour l'enregistrement manuel des joueurs du tournoi
        identifiant = input("Quel est votre identifiant national ?")
        nom = input("Quel est votre nom ?")
        prenom = input("Quel est votre prénom ?")
        reponses_formulaire = {"ID" : identifiant, "nom_joueur" : nom, "prenom_joueur" : prenom, "points" : 0}
        return reponses_formulaire



class FormulaireRechercheJoueur :
    def questionnaire():
        identifiant = input("Quel est l'identifiant national du joueur ?")
        return identifiant
    def affichage(resultat):
        if type(resultat) != dict :
            print(resultat)
        else :
            print("Voici les informations demandées")
            for cle in resultat :
                print(cle, ":", resultat[cle])


class ListeDesJoeurs :
    def affiche_liste_joueurs():
        resultat = ListeJoueurs.recup_liste()
        if resultat == False :
            print ("La base de données des joueurs n'est pas accessible. Veuillez contacter l'administrateur")
            input("Pressez 'ENTER' pour retourner au menu")
        else :
            print("Il y a actuellement " + str(len(resultat)) + " joueurs inscrits.")
            input("Pressez 'ENTER' pour afficher la liste des joueurs")
            for joueur in resultat :
                print(" ")
                print("=" * 29)
                print ("Idedntifiant national : " + joueur["Identifiant national"])
                print ("Nom du joueur : " + joueur["Nom du joueur"])
                print ("Prénom du joueur : " + joueur["Prénom du joueur"])
                print("=" * 29)
            input("Pressez 'ENTER' pour retourner au menu")


class ViewMatch :
    def __init__(self, les_paires, nom_tournoi, nom_tour):
        self.les_paires = les_paires
        #contient dico nom du match : dico paires
        self.nom_tournoi = nom_tournoi
        self.nom_tour = nom_tour

    def afficher_match(self):
        print("Bienvenue dans le tournoi ", self.nom_tournoi)
        print("Nous en sommes actuellement au ", self.nom_tour)
        choix_match = input("De quel match avez vous le retour ? (Format 'M+Numéro)")




if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")