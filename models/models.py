import json
import os


class Joueur :

    def __init__(self, q_identifiant, q_nom, q_prenom, q_sexe, q_date_naissance, q_remarque, stat_liste_tournois, stat_moyenne_points):
        self.identifiant = q_identifiant
        self.nom = q_nom
        self.prenom = q_prenom
        self.sexe = q_sexe
        self.date_naissance = q_date_naissance
        self.remarque = q_remarque
        self.liste_tournois = stat_liste_tournois
        self.moyenne_points = stat_moyenne_points

    def dictionnaire(self):
        #on crée un dictionnaire
        dict_joueur = {
            "Identifiant national" : self.identifiant,
            "Nom du joueur" : self.nom,
            "Prénom du joueur" : self.prenom,
            "Sexe" : self.sexe,
            "Date de naissance" : self.date_naissance,
            "Remarque du directeur" : self.remarque,
            "Liste des tournois" : self.liste_tournois,
            "Moyenne des points par tournoi" : self.moyenne_points
        }
        return dict_joueur

    def enregistreJoueur(self):
        bdd_joueurs = "joueurs.json"
        if os.path.exists(bdd_joueurs):
            #Si le fichier JSON pour les joueurs existe, on vérifie que le joueur n'existe pas déjà et on l'enregistre
            with open(bdd_joueurs, 'r') as f :
                contenu = json.load(f)
            for rjoueur in contenu :
                if rjoueur["Identifiant national"] == self.identifiant :
                    #On commence par vérifier si le joueur existe déjà
                    joueur_voulu = rjoueur["Nom du joueur"]+" "+rjoueur["Prénom du joueur"]
                    break

            if joueur_voulu :
                print("Le joueur ", joueur_voulu, " existe déjà. Pressez 'ENTER' pour retourner au menu principal")

            else :
                #S'il n'existe pas, on peut l'ajouter
                with open(bdd_joueurs, "w") as f :
                    contenu.append(self.dictionnaire())
                    json.dump(contenu, f)
                    print("Ce joueur a bien été créé. Pressez 'ENTER' pour retourner au menu principal")

        else :
            #Si le fichier JSON pour les joueurs n'existe pas encore, on le crée et on y ajoute le nouveau joueur
            with open(bdd_joueurs, "w") as f :
                json.dump([self.dictionnaire()], f)
                print("Ce joueur a bien été créé. Pressez 'ENTER' pour retourner au menu principal")


    def consulter_joueur(self):
        bdd_joueurs = "joueurs.json"
        if os.path.exists(bdd_joueurs):
            #Si le fichier JSON pour les joueurs existe on peut récupérer le contenu
            with open(bdd_joueurs, 'r') as f :
                contenu = json.load(f)
            for rjoueur in contenu :
                if rjoueur["Identifiant national"] == self.identifiant :
                    #On commence par vérifier si le joueur existe via une boucle et une condition
                    joueur_voulu = rjoueur
                    break

            if joueur_voulu :
                print(joueur_voulu)
            else:
                input("ce joueur n'existe pas ! Voulez vous l'enregistrer ?")
        else :
            print("Soit aucun joueur n'a encore été enregistré, soit le fichier JSON a été supprimé. Veuillez contacter l'administrateur.")

joueur1=Joueur("q_identifiant", "q_nom", "q_prenom", "q_sexe", "q_date_naissance", "q_remarque", "stat_liste_tournois", "stat_moyenne_points")
joueur1.dictionnaire()
joueur1.enregistreJoueur()
input("pause")
joueur2=Joueur("AB4587", "RENARD", "Christophe", "Homme", "25 août 1980", "t'es un mauvais", 5, 8)
joueur2.dictionnaire()
joueur2.enregistreJoueur()
input("pause2")
joueur3=Joueur("AB4587", 0, 0, 0, 0, 0, 0, 0)
joueur3.consulter_joueur()