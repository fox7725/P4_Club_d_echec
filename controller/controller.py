import sys
import keyboard

from view.view import MenuPrincipal, FormulaireNouveauJoueur, MenuConsulterListeJoueur
from models.models import Joueur

class Lancement :

    def __init__(self):
        pass

    def lancementMenuPrincipal() :
        reponse = 0
        menu = MenuPrincipal()
        reponse = menu.menuprincipal()
        if reponse == 1 :
            print(reponse)
        elif reponse == 2 :
            print(reponse)
        elif reponse == 3 :
            MenuJoueur.afficherMenuJoueur()
        elif reponse == 4 :
            sys.exit("Merci et à bientôt !")
        else :
            print("Une erreur s'est produite, veuillez presser une touche pour recommencer")
            keyboard.read_key()
            Lancement.lancementMenuPrincipal()

class MenuJoueur:
    def afficherMenuJoueur():
        reponse = 0
        menu = MenuConsulterListeJoueur()
        reponse = menu.menujoueur()
        if reponse == 1 :
            print(reponse)
        elif reponse == 3 :
            reponses_formulaire = FormulaireNouveauJoueur.questionnaire()
            creation = Joueur(reponses_formulaire[0], reponses_formulaire[1], reponses_formulaire[2], reponses_formulaire[3], reponses_formulaire[4], reponses_formulaire[5], reponses_formulaire[6], reponses_formulaire[7])
            creation.dictionnaire()
            resultat = creation.enregistreJoueur()
            print(resultat)
        elif reponse == 2 :
            print(reponse)
        elif reponse == 4 :
            print(reponse)
        elif reponse == 5 :
            Lancement.lancementMenuPrincipal()
        else :
            print("Une erreur s'est produite, veuillez presser une touche pour recommencer")
            keyboard.read_key()
            Lancement.lancementMenuPrincipal()

if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")