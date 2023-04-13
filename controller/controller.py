import sys

from view.view import *
from models.models import *

class Lancement :

    def lancementMenuPrincipal() :
        reponse = 0
        menu = MenuPrincipal()
        reponse = menu.menuprincipal()

        if reponse == 1 :
            infos_tournoi = TournoiView.infostournoi()
            nom_tournoi = infos_tournoi[0]
            date_debut = infos_tournoi[1]
            date_fin = infos_tournoi[2]
            lieu_tournoi = infos_tournoi[3]
            commentaire_tournoi = infos_tournoi[4]

            nv_joueurs = TournoiView.demandejoueur()
            if nv_joueurs == "oui":
                oui_non = "oui"
                liste_joueurs = []

                while oui_non == "oui":
                    dictionnaire_joueur = FormulaireNouveauJoueur.questionnairejoueurtournoi()
                    liste_joueurs.append(dictionnaire_joueur)

                    if len(liste_joueurs) == 0 or len(liste_joueurs) == 1 :
                        print("Il y a actuellement " + str(len(liste_joueurs)) + " joueur enregistré")
                    else :
                        print("Il y a actuellement " + str(len(liste_joueurs)) + " joueurs enregistrés")

                    oui_non = input("Voulez vous ajouter un nouveau joueur ? (oui / non) ")
                    if oui_non != "oui" and oui_non != "non":
                        print("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
                    elif oui_non == "non":
                        break
            else:
                liste_joueurs = []
                preliste_joueurs = ListeJoueurs.recup_liste()
                if len(preliste_joueurs) == 0 or len(preliste_joueurs) == 1:
                    print("Il y a actuellement " + str(len(preliste_joueurs)) + " joueur enregistré dans la base de données")
                else:
                    print("Il y a actuellement " + str(len(preliste_joueurs)) + " joueurs enregistrés dans la base de donnée")
                for i in preliste_joueurs :
                    joueur = {"ID" : i["Identifiant national"], "nom_joueur" : i["Nom du joueur"], "prenom_joueur" : i["Prénom du joueur"], "points" : 0}
                    liste_joueurs.append(joueur)

                o_n = "peut-être"
                while o_n != "oui" and o_n != "non" :
                    o_n = input("Souhaitez vous ajouter manuellement des invités ? (oui / non)")
                    if o_n != "oui" and o_n != "non":
                        print("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
                    elif o_n == "oui" :
                        y_n = "oui"
                        while y_n == "oui":
                            dictionnaire_joueur = FormulaireNouveauJoueur.questionnairejoueurtournoi()
                            liste_joueurs.append(dictionnaire_joueur)
                            if len(liste_joueurs) == 0 or len(liste_joueurs) == 1:
                                print("Il y a actuellement " + str(len(liste_joueurs)) + " joueur enregistré")
                            else:
                                print("Il y a actuellement " + str(len(liste_joueurs)) + " joueurs enregistrés")

                            y_n = input("Voulez vous ajouter un nouveau joueur ? (oui / non) ")
                            if y_n != "oui" and y_n != "non":
                                print("Votre saisie est invalide, veuillez répondre par 'oui' ou par 'non' !")
                            elif y_n == "non":
                                break
                    elif o_n == "non":
                        break

            nb_tours = TournoiView.nombretours()

            le_tournoi = Tournoi.organisationtournoi(nb_tours, liste_joueurs, nom_tournoi, date_debut, date_fin, lieu_tournoi, commentaire_tournoi)
            #contient dans cet ordre : nb_tours, liste_joueurs, nom_tournoi, date_debut, date_fin, lieu_tournoi, commentaire_tournoi, liste_tours

            for tour in le_tournoi[7] :
                le_tour = Tours.organisationtours(le_tournoi)
                #contient dans cet ordre : date_debut_tour, liste_matchs
                les_tours = [tour, le_tour[0], le_tour[1]]
                les_paires = Match.creation_paires(les_tours[0], le_tour[2], liste_joueurs)
                #contient dico nom du match : dico paires

                resultats_matchs = ViewMatch.afficher_match(les_paires, le_tournoi[3], tour)

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
                    elif oui_non == "non" :
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