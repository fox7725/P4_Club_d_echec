import json
import os


class Joueur :
    def __init__(self, identifiant_nationale, nom_joueur, prenom_joueur, sexe, date_naissance, score_actuel = 0):
        self.identifiant_nationale = identifiant_nationale
        self.nom_joueur = nom_joueur
        self.prenom_joueur = prenom_joueur
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.score_actuel = score_actuel


class JoueurJSON :
    def __init__(self, identifiant, nom, prenom, sexe, date_naissance, remarque, liste_tournois, moyenne_points):
        self.identifiant_national = identifiant
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.remarque = remarque
        self.liste_tournois = liste_tournois
        self.moyenne_points = moyenne_points

    def dictionnaire(self):
        #on crée un dictionnaire
        dict_joueur = {
            "Identifiant national" : self.identifiant_national,
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
        # On crée le dossier JSON pour stocker les BDD s'il n'existe pas
        os.makedirs("JSON", exist_ok=True)
        bdd_joueurs = "JSON/joueurs.json"
        joueur_voulu = "//"
        if os.path.exists(bdd_joueurs):
            # Si le fichier JSON pour les joueurs existe, on vérifie que le joueur n'existe pas déjà et on l'enregistre
            with open(bdd_joueurs, 'r') as f:
                contenu = json.load(f)
            for rjoueur in contenu:
                if rjoueur["Identifiant national"] == self.identifiant_national:
                    # On commence par vérifier si le joueur existe déjà
                    joueur_voulu = rjoueur["Nom du joueur"] + " " + rjoueur["Prénom du joueur"]
                    break
            if joueur_voulu != "//":
                reponse = "Le joueur " + joueur_voulu + " existe déjà."
                return reponse
            else:
                # Si le joueur n'existe pas, on peut le créer et ajouter le joueur
                with open(bdd_joueurs, "w") as f:
                    contenu.append(self.dictionnaire())
                    json.dump(contenu, f, indent=4)
                    reponse = "Le joueur a bien été créé."
                    return reponse
        else:
            # Si le fichier JSON pour les joueurs n'existe pas encore, on le crée et on y ajoute le nouveau joueur
            with open(bdd_joueurs, "w") as f:
                json.dump([self.dictionnaire()], f)
                reponse = "Le joueur a bien été créé."
                return reponse


class Tournoi :
    def __init__(self, nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours, liste_joueurs,
                 gagnant = " " ):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.remarque_tournoi = remarque_tournoi
        self.debut_tournoi = debut_tournoi
        self.fin_tournoi = fin_tournoi
        self.nb_tours = nb_tours
        self.liste_joueurs = liste_joueurs
        self.gagnant = gagnant

    def sauver_tournoi(self):
        # On créé le dossier "en_cours" s'il n'existe pas pour sauvegarder le tournoi en cours
        os.makedirs("JSON/en_cours", exist_ok=True)

        # On enregistre le tournoi dans un JSON pour le récupérer en cas de coupure
        # Convertion de l'objet Tournoi en un dictionnaire JSON
        tournoi_dict = {
            "nom_tournoi": self.nom_tournoi,
            "lieu_tournoi": self.lieu_tournoi,
            "remarque_tournoi": self.remarque_tournoi,
            "debut_tournoi": self.debut_tournoi,
            "fin_tournoi": self.fin_tournoi,
            "nb_tours": self.nb_tours,
            "liste_joueurs": [joueur.identifiant_nationale for joueur in self.liste_joueurs],
            "gagnant": self.gagnant
        }

        # Enregistrement du dictionnaire JSON dans un fichier
        with open("JSON/en_cours/tournoi.json", "w") as fichier :
            json.dump(tournoi_dict, fichier, indent=4)

    def sauver_joueurs(self):
        # Conversion de la liste des joueurs en dictionnaire
        liste_joueurs_dict = []
        for joueur in self.liste_joueurs :
            joueur_dict = {
                "identifiant_nationale" : joueur.identifiant_nationale,
                "nom_joueur" : joueur.nom_joueur,
                "prenom_joueur" : joueur.prenom_joueur,
                "sexe" : joueur.sexe,
                "date_naissance" : joueur.date_naissance,
                "score_actuel" : joueur.score_actuel
            }
            liste_joueurs_dict.append(joueur_dict)
        # Enregistrement du dictionnaire des joueurs dans un fichier JSON
        with open("JSON/en_cours/joueurs_tournoi.json", "w") as fichier_bis :
            json.dump(liste_joueurs_dict, fichier_bis, indent=4)


class Tour :
    def __init__(self, num_tour, nom_tour, liste_joueurs, nb_matchs, date_debut_tour, date_fin_tour = " "):
        self.num_tour = num_tour
        self.nom_tour = nom_tour
        self.liste_joueurs = liste_joueurs
        self.nb_matchs = nb_matchs
        self.date_debut_tour = date_debut_tour
        self.date_fin_tour = date_fin_tour


class Match :
    def __init__(self,nom_tour, nom_match, joueur_blanc, joueur_noir, score_JB = 0, score_JN = 0):
        self.nom_tour = nom_tour
        self.nom_match = nom_match
        self.joueur_blanc = joueur_blanc
        self.joueur_noir = joueur_noir
        self.score_JB = score_JB
        self.score_JN = score_JN

    def score (self, score) :
        if score == "JB" :
            self.score_JB = 1
            self.score_JN = 0
        elif score == "JN" :
            self.score_JB = 0
            self.score_JN = 1
        elif score == "N" :
            self.score_JB = 0.5
            self.score_JN = 0.5
        self.joueur_blanc.score_actuel += self.score_JB
        self.joueur_noir.score_actuel += self.score_JN


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
