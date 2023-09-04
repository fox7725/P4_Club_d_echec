import json
import os
import random

from fonctions.fonctions import suppression_encours, maintenant


class Joueur:
    def __init__(self, identifiant_national, nom_joueur, prenom_joueur, sexe,
                 date_naissance, points= 0):
        self.identifiant_national = identifiant_national
        self.nom_joueur = nom_joueur
        self.prenom_joueur = prenom_joueur
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.points = points

    @classmethod
    def creation(cls, j):
        return cls(
            j["ID"],
            j["nom_joueur"],
            j["prenom_joueur"],
            j["sexe"],
            j["date_naissance"],
            points = 0
        )


class Tournoi:
    def __init__(self, nom_tournoi, lieu_tournoi, remarque_tournoi, debut_tournoi, fin_tournoi, nb_tours,
                 liste_joueurs, liste_tours, gagnant=[]):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.remarque_tournoi = remarque_tournoi
        self.debut_tournoi = debut_tournoi
        self.fin_tournoi = fin_tournoi
        self.nb_tours = nb_tours
        self.liste_joueurs = liste_joueurs
        self.liste_tours = liste_tours
        self.gagnant = gagnant


    @classmethod
    def creation(cls, infos_tournoi, liste_joueurs):
        nom_tournoi=infos_tournoi[0]
        lieu_tournoi=infos_tournoi[1]
        remarque_tournoi=infos_tournoi[2]
        debut_tournoi=infos_tournoi[3]
        fin_tournoi=infos_tournoi[4]
        nb_tours=infos_tournoi[5]

        return cls(
            nom_tournoi,
            lieu_tournoi,
            remarque_tournoi,
            debut_tournoi,
            fin_tournoi,
            nb_tours,
            liste_tours=[],
            liste_joueurs=liste_joueurs,
            gagnant=[]
        )


    @classmethod
    def from_json(cls, tournoi_dict):
        # Extraction des données du dictionnaire JSON pour créer un objet Tournoi
        nom_tournoi = tournoi_dict["nom_tournoi"]
        lieu_tournoi = tournoi_dict["lieu_tournoi"]
        remarque_tournoi = tournoi_dict["remarque_tournoi"]
        debut_tournoi = tournoi_dict["debut_tournoi"]
        fin_tournoi = tournoi_dict["fin_tournoi"]
        nb_tours = tournoi_dict["nb_tours"]
        # Liste des joueurs
        liste_joueurs_infos = tournoi_dict["liste_joueurs"]
        liste_joueurs = []
        for joueur_infos in liste_joueurs_infos:
            joueur = Joueur(joueur_infos[0], joueur_infos[1],
                            joueur_infos[2], joueur_infos[3],
                            joueur_infos[4], joueur_infos[5])
            liste_joueurs.append(joueur)
        # Liste des tours
        liste_tours_infos = tournoi_dict["liste_tours"]
        liste_tours = []
        for tour_infos in liste_tours_infos:
            num_tour = tour_infos[0]
            nom_tour = tour_infos[1]
            date_debut_tour = tour_infos[3]
            date_fin_tour = tour_infos[4]

            # Liste des matchs
            liste_matchs_infos = tour_infos[2]
            liste_matchs = []
            for match_infos in liste_matchs_infos:
                nom_match = match_infos[0]
                joueur_blanc_infos = match_infos[1][0]
                score_JB = match_infos[1][1]
                joueur_noir_infos = match_infos[2][0]
                score_JN = match_infos[2][1]

                # Sélection du joueur blanc
                for joueur in liste_joueurs:
                    if joueur_blanc_infos != None:
                        if joueur.identifiant_national == joueur_blanc_infos[0]:
                            joueur_blanc = joueur
                    else:
                        joueur_blanc = None

                # Sélection du joueur noir
                for joueur in liste_joueurs:
                    if joueur_noir_infos != None:
                        if joueur.identifiant_national == joueur_noir_infos[0]:
                            joueur_noir = joueur
                    else:
                        joueur_noir = None

                match = Match(nom_match, joueur_blanc, joueur_noir, score_JB, score_JN)
                liste_matchs.append(match)

            tour = Tour(num_tour, nom_tour, liste_matchs, date_debut_tour, date_fin_tour)
            liste_tours.append(tour)
        # Liste des gagnants
        gagnants_infos = tournoi_dict["gagnant"]
        if gagnants_infos != None:
            gagnants = []
            for gagnant_infos in gagnants_infos:
                for joueur in liste_joueurs:
                    if joueur.identifiant_national == gagnant_infos[0]:
                        gagnant = joueur

                gagnants.append(gagnant)
        else:
            gagnants = None

        return cls(
            nom_tournoi,
            lieu_tournoi,
            remarque_tournoi,
            debut_tournoi,
            fin_tournoi,
            nb_tours,
            liste_joueurs,
            liste_tours,
            gagnants
        )

    def to_json(self):
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
            "liste_joueurs": [
                [
                joueur.identifiant_national,
                joueur.nom_joueur,
                joueur.prenom_joueur,
                joueur.sexe,
                joueur.date_naissance,
                joueur.points
                ]
                for joueur in self.liste_joueurs
            ],
            "liste_tours":
                [
                [
                    tour.num_tour,
                    tour.nom_tour,
                    # Liste des matchs
                    [
                        [
                            match.nom_match,
                            [
                                [
                                    match.joueur_blanc.identifiant_national,
                                    match.joueur_blanc.nom_joueur,
                                    match.joueur_blanc.prenom_joueur,
                                    match.joueur_blanc.sexe,
                                    match.joueur_blanc.date_naissance,
                                    match.joueur_blanc.points
                                ] if match.joueur_blanc else None,
                                match.score_JB
                            ],
                            [
                                [
                                    match.joueur_noir.identifiant_national,
                                    match.joueur_noir.nom_joueur,
                                    match.joueur_noir.prenom_joueur,
                                    match.joueur_noir.sexe,
                                    match.joueur_noir.date_naissance,
                                    match.joueur_noir.points
                                ] if match.joueur_noir else None,
                                match.score_JN
                            ]
                        ]
                    for match in tour.liste_matchs
                    ],
                    tour.date_debut_tour,
                    tour.date_fin_tour
                ]
                for tour in self.liste_tours
            ],
            "gagnant": [
                [
                joueur.identifiant_national,
                joueur.nom_joueur,
                joueur.prenom_joueur,
                joueur.sexe,
                joueur.date_naissance,
                joueur.points
                ]
                for joueur in self.gagnant
            ] if self.gagnant else None
        }

        # Enregistrement du dictionnaire JSON dans un fichier
        with open("JSON/en_cours/tournoi.json", "w") as fichier:
            json.dump(tournoi_dict, fichier, indent=4)

    def sauvegarde_fin_tournoi(self):
        # On crée le dossier archives s'il n'existe pas
        os.makedirs("JSON/archives", exist_ok=True)

        # On classe les joueurs par ordre alphabétique
        joueurs_tries = sorted(self.liste_joueurs, key=lambda joueur: joueur.nom_joueur)
        self.liste_joueurs = joueurs_tries
        # On crée un dictionnaire avec les données à enregistrer dans le JSON
        tournoi_dict = {
            "nom_tournoi": self.nom_tournoi,
            "lieu_tournoi": self.lieu_tournoi,
            "remarque_tournoi": self.remarque_tournoi,
            "debut_tournoi": self.debut_tournoi,
            "fin_tournoi": self.fin_tournoi,
            "nb_tours": self.nb_tours,
            "liste_joueurs": [
                [
                    joueur.identifiant_national,
                    joueur.nom_joueur,
                    joueur.prenom_joueur,
                    joueur.sexe,
                    joueur.date_naissance,
                    joueur.points
                ]
                for joueur in self.liste_joueurs
            ],
            "liste_tours":
                [
                    [
                        tour.num_tour,
                        tour.nom_tour,
                        # Liste des matchs
                        [
                            [
                                match.nom_match,
                                [
                                    [
                                        match.joueur_blanc.identifiant_national,
                                        match.joueur_blanc.nom_joueur,
                                        match.joueur_blanc.prenom_joueur,
                                        match.joueur_blanc.sexe,
                                        match.joueur_blanc.date_naissance,
                                        match.joueur_blanc.points
                                    ] if match.joueur_blanc else None,
                                    match.score_JB
                                ],
                                [
                                    [
                                        match.joueur_noir.identifiant_national,
                                        match.joueur_noir.nom_joueur,
                                        match.joueur_noir.prenom_joueur,
                                        match.joueur_noir.sexe,
                                        match.joueur_noir.date_naissance,
                                        match.joueur_noir.points
                                    ] if match.joueur_noir else None,
                                    match.score_JN
                                ]
                            ]
                            for match in tour.liste_matchs
                        ],
                        tour.date_debut_tour,
                        tour.date_fin_tour
                    ]
                    for tour in self.liste_tours
                ],
            "gagnant": [
                [
                    joueur.identifiant_national,
                    joueur.nom_joueur,
                    joueur.prenom_joueur,
                    joueur.sexe,
                    joueur.date_naissance,
                    joueur.points
                ]
                for joueur in self.gagnant
            ] if self.gagnant else None
        }

        # On vérifie si une archive existe déjà
        bdd_tournoi = "JSON/archives/tournois.json"
        if os.path.exists(bdd_tournoi):
            # On charge le fichier en mémoire
            with open(bdd_tournoi, 'r') as f: contenu = json.load(f)
            # On ajoute le tournoi qui vient de se terminer, pas besoin de faire un classement car le dernier
            # tournoi terminé sera le dernier ajouté
            contenu.append(tournoi_dict)
            with open(bdd_tournoi, "w") as f: json.dump(contenu, f, indent=4)
        else:
            # Si l'archive n'existe pas encore, on la crée et on y ajoute le tournoi
            liste_tournoi_dict = []
            liste_tournoi_dict.append(tournoi_dict)
            with open(bdd_tournoi, "w") as f: json.dump(liste_tournoi_dict, f, indent=4)

        # On peut maintenant supprimer le dossier "en_cours" et les JSON temporaires qu'il contient :
        suppression_encours()
        reponse = "Le tournoi a bien été archivé."
        return reponse


class Tour:
    def __init__(self, num_tour, nom_tour, liste_matchs, date_debut_tour=" ", date_fin_tour=" "):
        self.num_tour = num_tour
        self.nom_tour = nom_tour
        self.liste_matchs = liste_matchs
        self.date_debut_tour = date_debut_tour
        self.date_fin_tour = date_fin_tour

    @classmethod
    def initialisation(cls, num_tour, liste_matchs):
        nom_tour = "Round " + str(num_tour)
        return cls(
            num_tour,
            nom_tour,
            liste_matchs=liste_matchs,
            date_debut_tour=" ",
            date_fin_tour=" ",
        )

    def organisation_tour(self, tournoi, paires_ayant_joue):
        # On commence par récupérer les paires de joueurs ayant joué ensemble sur les tours terminés
        match_restant = []
        if self.date_fin_tour != " ":
            for match in self.liste_matchs:
                paire = [match.joueur_blanc, match.joueur_noir]
                paires_ayant_joue.append(paire)

        # Si le tour a déjà commencé mais n'est pas terminé
        if self.date_fin_tour == " " and self.date_debut_tour != " ":
            for match in self.liste_matchs:
                # On récupère les paires
                paire = [match.joueur_blanc, match.joueur_noir]
                paires_ayant_joue.append(paire)
                # si les deux joueurs ont un score à 0, le match n'a pas été joué
                if match.score_JB == 0 and match.score_JN == 0:
                    match_restant.append(match)

        # Si le tour n'a pas commencé on crée la liste des matchs
        if self.date_debut_tour == " ":
            # On enregistre la date de lancement du tour
            self.date_debut_tour = maintenant()
            # On récupère et on classe la liste des joueurs
            liste_joueurs_tour = tournoi.liste_joueurs.copy()
            if self.nom_tour == "Round 1":
                random.shuffle(liste_joueurs_tour)
            else:
                liste_joueurs_tour.sort(key=lambda x: (-x.points, x.nom_joueur))
            for match in self.liste_matchs:
                # On vérifie que la paire qu'on va créer n'a pas déjà joué ensemble
                i = 1
                duo = [liste_joueurs_tour[0], liste_joueurs_tour[i]]
                if duo in paires_ayant_joue:
                    while duo in paires_ayant_joue and  i < len(liste_joueurs_tour) - 1:
                        i += 1
                        duo = [liste_joueurs_tour[0], liste_joueurs_tour[i]]

                        # Si on a parcouru toutes les possibilités de paires, on revient à la paire d'origine
                        if i == len(liste_joueurs_tour) - 1:
                            i = 1
                            duo = [liste_joueurs_tour[0], liste_joueurs_tour[1]]

                        break

                # On crée la paire et on l'ajoute aux paires ayant joué
                match.joueur_blanc = duo[0]
                match.joueur_noir = duo[1]
                paire = [match.joueur_blanc, match.joueur_noir]
                paires_ayant_joue.append(paire)

                # On retire ces joueurs de la liste pour éviter les doublons
                liste_joueurs_tour.remove(match.joueur_noir)
                liste_joueurs_tour.remove(match.joueur_blanc)

                # On ajoute le match aux matchs à jouer
                match_restant.append(match)

        organisation = [paires_ayant_joue, match_restant]
        return organisation


class Match:
    def __init__(self, nom_match, joueur_blanc = None, joueur_noir=None, score_JB=0,score_JN=0):
        self.nom_match = nom_match
        self.joueur_blanc = joueur_blanc
        self.joueur_noir = joueur_noir
        self.score_JB = score_JB
        self.score_JN = score_JN

    @classmethod
    def initialisation(cls, num_match):
        nom_match = "M" + str(num_match)
        return cls(
            nom_match,
            joueur_blanc = None,
            joueur_noir = None,
            score_JB=0,
            score_JN=0
        )

    def score(self, score):
        if not self.joueur_blanc or not self.joueur_noir:
            return
        if score == "JB":
            self.score_JB = 1
            self.score_JN = 0
        elif score == "JN":
            self.score_JB = 0
            self.score_JN = 1
        elif score == "N":
            self.score_JB = 0.5
            self.score_JN = 0.5
        self.joueur_blanc.points += self.score_JB
        self.joueur_noir.points += self.score_JN


class JoueurJSON:
    def __init__(self, identifiant, nom, prenom, sexe, date_naissance,
                 liste_tournois, moyenne_points):
        self.identifiant_national = identifiant
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.liste_tournois = liste_tournois
        self.moyenne_points = moyenne_points

    def dictionnaire(self):
        # on crée un dictionnaire
        dict_joueur = {
            "Identifiant national": self.identifiant_national,
            "Nom du joueur": self.nom,
            "Prénom du joueur": self.prenom,
            "Sexe": self.sexe,
            "Date de naissance": self.date_naissance,
            "Liste des tournois": self.liste_tournois,
            "Moyenne des points par tournoi": self.moyenne_points
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

    @staticmethod
    def mise_a_jour_tournoi(joueurs_tournoi):
        # On vérifie qu'un JSON existe pour la gestion des joueurs
        bdd_joueurs = "JSON/joueurs.json"
        if os.path.exists(bdd_joueurs):
            # On charge le fichier en mémoire
            with open(bdd_joueurs, 'r') as f:
                contenu = json.load(f)
            # On transforme chaque joueur du JSON en objet
            joueurs_JSON = []
            for j in contenu:
                joueur = JoueurJSON(
                    j["Identifiant national"],
                    j["Nom du joueur"],
                    j["Prénom du joueur"],
                    j["Sexe"],
                    j["Date de naissance"],
                    j["Liste des tournois"],
                    j["Moyenne des points par tournoi"]
                )
                joueurs_JSON.append(joueur)
            # On récupère les joueurs du tournoi faisant partie du club pour les mettre à jour.
            joueurs_maj = []
            for joueur_tournoi in joueurs_tournoi:
                tournois = []
                for joueur_club in joueurs_JSON:
                    if joueur_tournoi.identifiant_national == joueur_club.identifiant_national:
                        tournois.extend(joueur_club.liste_tournois)
                        tournois.append(joueur_tournoi.liste_tournois)
                        if len(tournois) > 0:
                            score = 0
                            for t in tournois:
                                score += t[2]["score"]
                            moyenne = score / len(tournois)
                        else:
                            moyenne = 0

                        joueur_maj = {
                            "Identifiant national": joueur_club.identifiant_national,
                            "Nom du joueur": joueur_club.nom,
                            "Prénom du joueur": joueur_club.prenom,
                            "Sexe": joueur_club.sexe,
                            "Date de naissance": joueur_club.date_naissance,
                            "Liste des tournois": tournois,
                            "Moyenne des points par tournoi": moyenne
                        }
                        joueurs_maj.append(joueur_maj)

            # On vérifie s'il n'y a pas des joueurs qui n'ont pas joué
            for joueur_JSON in joueurs_JSON:
                joueur_trouve = False
                for joueur_maj in joueurs_maj:
                    if joueur_maj["Identifiant national"] == joueur_JSON.identifiant_national:
                        joueur_trouve = True
                if joueur_trouve == False:
                    joueur_ajout = {
                        "Identifiant national": joueur_JSON.identifiant_national,
                        "Nom du joueur": joueur_JSON.nom,
                        "Prénom du joueur": joueur_JSON.prenom,
                        "Sexe": joueur_JSON.sexe,
                        "Date de naissance": joueur_JSON.date_naissance,
                        "Liste des tournois": joueur_JSON.liste_tournois,
                        "Moyenne des points par tournoi": joueur_JSON.moyenne_points
                    }
                    joueurs_maj.append(joueur_ajout)
            # On met à jour le JSON
            with open(bdd_joueurs, "w") as f:
                json.dump(joueurs_maj, f, indent=4)
            reponse = "Les statistiques des joueurs du club ont bien été mises à jour."
        else :
            reponse = "Le fichier JSON des joueurs n'a pas été trouvé, rapprochez vous de votre administrateur !"
        return reponse
