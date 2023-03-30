import sys
import json

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
            if self.code_menu_principal == 4 :
                sys.exit("Merci et à bientôt !")

class MenuNouveauTournoi :
    def __init__(self):
        pass

class MenuConsulterTournoi :
    pass

class MenuConsulterListeJoueur :
    pass

class FormulaireNouveauJoueur :
    pass

class FormulaireRechercheJoueur :
    pass

if __name__ == "__main__":
    print("="*29)
    print(" ")
    print("BIENVENUE DANS VOTRE LOGICIEL")
    print("DE GESTION DE TOURNOIS DE")
    print("PING-PONG")
    print(" ")
    print("="*29)
    input("Pressez 'ENTER' pour continuer")

    menu = MenuPrincipal()
    menu.menuprincipal()
    choix = menu.code_menu_principal
