import keyboard

from controller.controller import Lancement
from view.view import MenuPrincipal
def accueil() :
    print("=" * 29)
    print(" ")
    print("BIENVENUE DANS VOTRE LOGICIEL")
    print("DE GESTION DE TOURNOIS DE")
    print("PING-PONG")
    print(" ")
    print("=" * 29)
    print("Pressez une touche pour continuer")
    keyboard.read_key()
    Lancement.lancementMenuPrincipal()


if __name__ == "__main__":
    #Affichage du message de bienvenue
    accueil()
