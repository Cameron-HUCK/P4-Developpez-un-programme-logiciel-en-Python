import os
import json
import random
from Vue.vue import VueClassement, VueAppariements
from Controleur.controleur import ControllerPartie, ControllerTournoi
from Modèle.modele import Joueur, Tournoi, Partie

# Création d'une liste pour stocker les joueurs
players = []

# Définition initiale du tournoi et du contrôleur de tournoi
create_tournament = None
controller_tournament = None


# Fonction pour simuler les matchs d'une ronde
def simuler_matchs(ronde_controller):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Simuler les matchs pour la Ronde {ronde_controller.number_ronde}\n")

    already_played = set()  # Pour suivre les joueurs qui ont déjà joué

    for match in ronde_controller.matchs:
        player1, _ = match.match[0]
        player2, _ = match.match[1]

        # Vérifier si les joueurs ont déjà joué ensemble
        while (player1, player2) in already_played or (player2, player1) in already_played:
            print(f"{player1.first_name} {player1.name} et {player2.first_name} {player2.name} ont déjà joué ensemble. Choisir d'autres joueurs.")
            player1 = random.choice(create_tournament.player_register)
            player2 = random.choice(create_tournament.player_register)

        score1 = float(input(f"Score pour {player1.first_name} {player1.name}: "))
        score2 = float(input(f"Score pour {player2.first_name} {player2.name}: "))

        controller_partie = ControllerPartie(ronde_controller)
        controller_partie.save_result(match, score1, score2)

        # Ajouter les joueurs à la liste des matchs déjà joués
        already_played.add((player1, player2))

    print("\nRésultats enregistrés pour la ronde.")
    input("Appuyez sur Entrée pour continuer...")


# Menu interactif pour le tournoi
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nMenu:")
    print("1. Création du tournoi")
    print("2. Inscription des joueurs")
    print("3. Ajouter un Round")
    print("4. Simuler les matchs d'une ronde")
    print("5. Affichage du classement des joueurs")
    print("6. Affichage du score d'une ronde")
    print("7. Affichage des informations du tournoi actuelle")
    print("8. Fin du tournoi")
    print("9. Quitter")

    choice = input("Sélectionnez une option : ")

    if choice == "1":
        """Création d'un nouveau tournoi"""
        name_tournament = input("Entrez le nom du tournoi : ")
        place = input("Entrez le lieu du tournoi : ")
        start_date = input("Entrez la date de début (YYYY-MM-DD) : ")
        end_date = input("Entrez la date de fin (YYYY-MM-DD) : ")
        number_turns = int(input("Entrez le nombre de rounds : "))
        create_tournament = Tournoi(name_tournament, place, start_date, end_date, number_turns)
        controller_tournament = ControllerTournoi(create_tournament)
        print("Tournoi créé !")

    elif choice == "2":
        """Inscription des joueurs"""
        if len(players) >= 8:
            print("Le nombre maximum de joueurs (8) est atteint.")
        else:
            first_name = input("Entrez le prénom du joueur : ")
            last_name = input("Entrez le nom du joueur : ")
            date_of_birth = input("Entrez la date de naissance du joueur (YYYY-MM-DD) : ")
            classement = float(input("Entrez le classement du joueur : "))
            new_player = Joueur(first_name, last_name, date_of_birth, classement)

            # Vérification pour éviter l'inscription d'un même joueur plusieurs fois
            if new_player not in players:
                players.append(new_player)
                if create_tournament:
                    create_tournament.player_register.append(new_player)
                print("Joueur inscrit avec succès !")
            else:
                print("Ce joueur est déjà inscrit.")

    elif choice == "3":
        """Création d'un round"""
        if create_tournament:
            ronde_controller = controller_tournament.create_ronde()
            print(f"Ronde {ronde_controller.number_ronde} créée !")
            # Création des instances de parties (matchs) si la liste players contient suffisamment de joueurs
            if len(players) >= 4:
                round_matches = []
                # Assurez-vous que le nombre de joueurs inscrits est pair
                if len(players) % 2 != 0:
                    print("Le nombre de joueurs inscrits n'est pas pair, certains joueurs ne joueront pas cette ronde.")
                # Créez des matchs en paires de joueurs
                for i in range(0, len(players), 2):
                    if i + 1 < len(players):
                        game = Partie(players[i], 0, players[i + 1], 0)
                        round_matches.append(game)
                ronde_controller.matchs = round_matches
                # Retirez les joueurs de la liste create_tournament.player_register
                if create_tournament:
                    for match in round_matches:
                        player1, player2 = match.match[0], match.match[1]
                        if player1 in create_tournament.player_register:
                            create_tournament.player_register.remove(player1)
                        if player2 in create_tournament.player_register:
                            create_tournament.player_register.remove(player2)
            else:
                print("Il n'y a pas suffisamment de joueurs inscrits pour créer des matchs.")
        else:
            print("Veuillez d'abord créer un tournoi.")

    elif choice == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        """Simulation des matchs d'une ronde"""
        round_number = int(input("Entrez le numéro de la ronde : "))
        ronde_controller = create_tournament.turns[round_number - 1]
        simuler_matchs(ronde_controller)

    elif choice == "5":
        """Affichage du classement des joueurs"""
        vue_classement = VueClassement()
        vue_classement.display_classement(create_tournament)
        input("Appuyez sur Entrée pour continuer...")

    elif choice == "6":
        """Affichage des appariements d'une ronde"""
        round_number = int(input("Entrez le numéro de la ronde : "))
        ronde_controller = create_tournament.turns[round_number - 1]
        vue_appariements = VueAppariements()
        vue_appariements.display_appariements(ronde_controller)
        input("Appuyez sur Entrée pour continuer...")

    elif choice == "7":
        # Afficher les informations sur le tournoi
        if create_tournament is None:
            print("Aucun tournoi n'a été créé. Veuillez d'abord créer un tournoi.")
        else:
            print("Tournoi :", create_tournament.name_tournament)
            print("Lieu :", create_tournament.place)
            print("Date de début :", create_tournament.start_date)
            print("Date de fin :", create_tournament.end_date)
            print("Nombre de tours :", create_tournament.number_turn)
            print("Tour actuel :", create_tournament.current_turn)
            print("Remarques :", create_tournament.remarques)

        # Afficher le classement même si le tournoi est marqué comme terminé
        if create_tournament.is_done:
            vue_classement = VueClassement()
            vue_classement.display_classement(create_tournament)

    elif choice == "8":
        os.system('cls' if os.name == 'nt' else 'clear')
        """Fin du tournoi"""
        create_tournament.mark_as_done()
        print("Le tournoi est marqué comme terminé.")
        # Générer un fichier JSON avec les données du tournoi
        tournament_data = {
            "name_tournament": create_tournament.name_tournament,
            "place": create_tournament.place,
            "start_date": create_tournament.start_date,
            "end_date": create_tournament.end_date,
            "number_turns": create_tournament.number_turn,
            "current_turn": create_tournament.current_turn,
            "player_register": [
                {
                    "first_name": player.first_name,
                    "name": player.name,
                    "date_of_birth": player.date_of_birth,
                    "classement": player.classement
                }
                for player in create_tournament.player_register
            ],
            "turns": [
                {
                    "number_ronde": turn.number_ronde,
                    "matchs": [
                        {
                            "match": [
                                [
                                    player1.first_name,
                                    player1.name,
                                    player1.date_of_birth,
                                    player1.classement
                                ],
                                [
                                    player2.first_name,
                                    player2.name,
                                    player2.date_of_birth,
                                    player2.classement
                                ],
                                [score1, score2]
                            ]
                        }
                        for game in turn.matchs
                        for player1, score1, player2, score2 in [
                            (game.match[0][0], game.match[0][1], game.match[1][0], game.match[1][1])
                        ]
                    ]
                }
                for turn in create_tournament.turns
            ],
            "remarques": create_tournament.remarques,
            "is_done": create_tournament.is_done
        }
        with open("tournament_data.json", "w") as json_file:
            json.dump(tournament_data, json_file)
        print("Les données du tournoi ont été sauvegardées")

    elif choice == "9":
        """Quitter le programme"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fermeture...")
        break

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Choix invalide. Veuillez sélectionner une option valide.")
