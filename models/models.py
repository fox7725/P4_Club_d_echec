import json
import os
import send2trash


class Joueur :
    def __init__(self, identifiant_national, nom_joueur, prenom_joueur, sexe, date_naissance, score_actuel = 0):
        self.identifiant_national = identifiant_national
        self.nom_joueur = nom_joueur
        self.prenom_joueur = prenom_joueur
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.score_actuel = score_actuel

    def mise_a_jour_fin_tournoi(self, nom_tournoi, date_tournoi):
        #On crée un tuple contenant les info sur le tournoi que le joueur vient de jouer
        info_tournoi = (nom_tournoi, date_tournoi, {"score" : self.score_actuel})
        # on accède au fichier JSON pour la charger et chercher le joueur
        os.makedirs("JSON", exist_ok=True)
        bdd_joueurs = "JSON/joueurs.json"
        if os.path.exists(bdd_joueurs):
            # Si le fichier JSON pour les joueurs existe, on vérifie que le joueur n'existe pas déjà et on l'enregistre
            with open(bdd_joueurs, 'r') as f:
                contenu = json.load(f)
            for rjoueur in contenu:
                # On commence par vérifier si le joueur existe déjà
                if rjoueur["Identifiant national"] == self.identifiant_national:
                    # On calcul la moyenne des scores du joueur
                    nombre_tournoi_participe = len(rjoueur["Liste des tournois"])
                    calcul_moyenne = ((rjoueur["Moyenne des points par tournoi"] * nombre_tournoi_participe) +
                                      self.score_actuel) / (nombre_tournoi_participe + 1)

                    #on met à jour les informations du joueur
                    rjoueur["Liste des tournois"].append(info_tournoi)
                    rjoueur["Moyenne des points par tournoi"] = calcul_moyenne
            with open(bdd_joueurs, "w") as f:
                json.dump(contenu, f, indent=4)
            return 1

        else :
            return 0


class JoueurJSON :
    def __init__(self, identifiant, nom, prenom, sexe, date_naissance, liste_tournois, moyenne_points):
        self.identifiant_national = identifiant
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date_naissance = date_naissance
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
                 gagnant = [] ):
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
            "liste_joueurs": [joueur.identifiant_national for joueur in self.liste_joueurs],
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
                "identifiant_national" : joueur.identifiant_national,
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

    def sauvegarde_fin_tournoi(self, liste_tours):
        #On crée le dossier archives s'il n'existe pas
        os.makedirs("JSON/archives", exist_ok=True)

        #On récupère le nom et le prénom des joueurs gagnants et on en fait une liste
        gagnants = []
        for gagnant in self.gagnant :
            for le_joueur in self.liste_joueurs :
                if le_joueur.identifiant_national == gagnant:
                    joueur_gagnant = {le_joueur.identifiant_national : [le_joueur.prenom_joueur, le_joueur.nom_joueur]}
                    gagnants.append(joueur_gagnant)
                    break

        #On classe les joueurs par ordre alphabétique
        joueurs_tries = sorted(self.liste_joueurs, key=lambda joueur: joueur.nom_joueur)
        #On crée un dictionnaire avec les données à enregistrer dans le JSON
        tournoi_dict = {
            "nom_tournoi": self.nom_tournoi,
            "lieu_tournoi": self.lieu_tournoi,
            "remarque_tournoi": self.remarque_tournoi,
            "debut_tournoi": self.debut_tournoi,
            "fin_tournoi": self.fin_tournoi,
            "nb_tours": self.nb_tours,
            "liste_matchs": [{tour.nom_tour : tour.liste_tuples_matchs_tour} for tour in liste_tours],
            "liste_joueurs": [
                {
                    joueur.identifiant_national : [
                        joueur.prenom_joueur,
                        joueur.nom_joueur
                    ]
                }
                for joueur in joueurs_tries
            ],
            "gagnant": gagnants
        }

        #On vérifie si une archive existe déjà
        bdd_tournoi = "JSON/archives/tournois.json"
        if os.path.exists(bdd_tournoi):
            #On charge le fichier en mémoire
            with open(bdd_tournoi, 'r') as f:
                contenu = json.load(f)
            #On ajoute le tournoi qui vient de se terminer, pas besoin de faire un classement car le dernier tournoi
            #terminé sera le dernier ajouté
            with open(bdd_tournoi, "w") as f:
                contenu.append(tournoi_dict)
                json.dump(contenu, f, indent=4)
        else :
            #Si l'archive n'existe pas encore, on la crée et on y ajoute le tournoi
            liste_tournoi_dict = []
            liste_tournoi_dict.append(tournoi_dict)
            with open(bdd_tournoi, "w") as f:
                json.dump(liste_tournoi_dict, f, indent=4)

        #On peut maintenant supprimer le dossier "en_cours" et les JSON temporaires qu'il contient :
        #On regarde les fichiers et les sous-répertoires dans le répertoire
        for dossier, sous_repertoires, fichiers in os.walk("JSON/en_cours"):
            #On supprime les fichiers en les déplaçant dans la corbeille pour plus de sécurité
            for fichier in fichiers:
                chemin_fichier = os.path.join(dossier, fichier)
                send2trash.send2trash(chemin_fichier)

        #On supprime le répertoire vide restant
        os.rmdir("JSON/en_cours")

        reponse = "Le tournoi a bien été archivé."
        return reponse


class TournoisJSON :
    def __init__(self, nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours, liste_matchs,
                 liste_joueurs, gagnant):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.remarque_tournoi = remarque_tournoi
        self.debut_tournoi = debut_tournoi
        self.fin_tournoi = fin_tournoi
        self.nb_tours = nb_tours
        self.liste_matchs = liste_matchs
        self.liste_joueurs = liste_joueurs
        self.gagnant = gagnant


class Tour :
    def __init__(self, num_tour, nom_tour, liste_joueurs, nb_matchs, date_debut_tour, liste_tuples_matchs_tour = [],
                 date_fin_tour = " "):
        self.num_tour = num_tour
        self.nom_tour = nom_tour
        self.liste_joueurs = liste_joueurs
        self.nb_matchs = nb_matchs
        self.date_debut_tour = date_debut_tour
        self.liste_tuples_matchs_tour = liste_tuples_matchs_tour
        self.date_fin_tour = date_fin_tour

    @staticmethod
    def sauvegarde_tour(liste_tours, liste_tuples_matchs_tour):
        liste_tours_dict = []
        for tour_a_sauver in liste_tours:
            tour_a_sauver.liste_tuples_matchs_tour = liste_tuples_matchs_tour
            tour_dict = {
                "num_tour": tour_a_sauver.num_tour,
                "nom_tour": tour_a_sauver.nom_tour,
                "nb_matchs": tour_a_sauver.nb_matchs,
                "liste_match": tour_a_sauver.liste_tuples_matchs_tour,
                "date_debut_tour": tour_a_sauver.date_debut_tour,
                "date_fin_tour": tour_a_sauver.date_fin_tour
            }
            liste_tours_dict.append(tour_dict)
        with open("JSON/en_cours/tours_joues.json", "w") as fichier_bis:
            json.dump(liste_tours_dict, fichier_bis, indent=4)


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

    @staticmethod
    def sauvegarde_matchs(liste_matchs_joues):
        # On sauvegarde les matchs joués dans un JSON
        liste_matchs_joues_dict = []
        for match_joue in liste_matchs_joues:
            match_joue_dict = {
                "nom_tour": match_joue.nom_tour,
                "nom_match": match_joue.nom_match,
                "joueur_blanc": match_joue.joueur_blanc.identifiant_national,
                "joueur_noir": match_joue.joueur_noir.identifiant_national,
                "score_JB": match_joue.score_JB,
                "score_JN": match_joue.score_JN
            }
            liste_matchs_joues_dict.append(match_joue_dict)
        with open("JSON/en_cours/matchs_joues.json", "w") as fichier:
            json.dump(liste_matchs_joues_dict, fichier, indent=4)


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
