
from controller.controller import Lancement


def accueil():
    print("=" * 29)
    print(" ")
    print("BIENVENUE DANS VOTRE LOGICIEL")
    print("DE GESTION DE TOURNOIS")
    print("D'ECHECS")
    print(" ")
    print("=" * 29)
    input("Pressez 'ENTER' pour continuer")
    Lancement.lancementMenuPrincipal(0)


if __name__ == "__main__":
    # Affichage du message de bienvenue
    accueil()
