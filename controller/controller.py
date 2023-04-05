import sys
import keyboard

from view.view import MenuPrincipal, FormulaireNouveauJoueur, MenuConsulterListeJoueur, FormulaireRechercheJoueur, ListeDesJoeurs
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
            print("Une erreur s'est produite")
            input("Pressez 'ENTER' pour continuer")
            Lancement.lancementMenuPrincipal()

class MenuJoueur:
    def afficherMenuJoueur():
        reponse = 0
        menu = MenuConsulterListeJoueur()
        reponse = menu.menujoueur()
        if reponse == 1 :
            ListeDesJoeurs.affiche_liste_joueurs()
            MenuJoueur.afficherMenuJoueur()
        elif reponse == 3 :
            oui_non = "oui"
            while oui_non == "oui" :
                reponses_formulaire = FormulaireNouveauJoueur.questionnaire()
                creation = Joueur(reponses_formulaire[0], reponses_formulaire[1], reponses_formulaire[2], reponses_formulaire[3], reponses_formulaire[4], reponses_formulaire[5], reponses_formulaire[6], reponses_formulaire[7])
                creation.dictionnaire()
                resultat = creation.enregistreJoueur()
                print(resultat)
                oui_non = "peut-être"
                while oui_non != "oui" and oui_non != "non" :
                    oui_non = input("Voulez vous créer un nouveau joueur ? (oui / non) ")
                    if oui_non != "oui" and oui_non != "non" :
                        print ("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
                    if oui_non == "non" :
                        MenuJoueur.afficherMenuJoueur()
        elif reponse == 2 :
            oui_non = "oui"
            while oui_non == "oui" :
                reponses_formulaire = FormulaireRechercheJoueur.questionnaire()
                consultation = Joueur(reponses_formulaire, 0, 0, 0, 0, 0, 0, 0)
                resultat = consultation.consulter_joueur()
                #print(resultat)
                print(FormulaireRechercheJoueur.affichage(resultat))
                oui_non = "peut-être"
                while oui_non != "oui" and oui_non != "non" :
                    oui_non = input("Voulez vous consulter un autre joueur ? (oui / non) ")
                    if oui_non != "oui" and oui_non != "non" :
                        print ("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
                    if oui_non == "non" :
                        MenuJoueur.afficherMenuJoueur()
        elif reponse == 4 :
            Lancement.lancementMenuPrincipal()
        else :
            print("Une erreur s'est produite")
            input("Pressez 'ENTER' pour continuer")
            MenuJoueur.afficherMenuJoueur()

if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")