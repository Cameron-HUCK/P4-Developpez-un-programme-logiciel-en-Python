import os
import random

from Vue.vue import VueClassement, VueAppariements
from Controleur.controleur import ControllerPartie, ControllerTournoi
from Modèle.modele import Joueur, Tournoi, Ronde, Partie


# Création des instances de joueurs (remplacer par vos données réelles)
player1 = Joueur("Alice", "Wonderland", "2000-01-01", 1500)
player2 = Joueur("Bob", "Builder", "2000-01-02", 1400)
player3 = Joueur("Eve", "Green", "2000-01-03", 1600)
player4 = Joueur("Carl", "Johnson", "2000-01-04", 1450)

# Création des instances de parties (matchs)
game_1 = Partie(player1, 0, player2, 0)
game_2 = Partie(player3, 0, player4, 0)

game_3 = Partie(player1, 0, player3, 0)
game_4 = Partie(player2, 0, player4, 0)

game_5 = Partie(player1, 0, player4, 0)
game_6 = Partie(player2, 0, player3, 0)

# Création des instances de rondes et ajout des matchs
ronde_1 = Ronde(1)
ronde_1.matchs = [game_1, game_2]

ronde_2 = Ronde(2)
ronde_2.matchs = [game_3, game_4]

ronde_3 = Ronde(3)
ronde_3.matchs = [game_5, game_6]

# Création du tournoi et ajout des rondes
create_tournament = Tournoi("Tournoi d'échecs", "Salle des échecs", "2023-07-17", "2023-07-24")
create_tournament.turns = [ronde_1, ronde_2, ronde_3]

# Inscription des joueurs au tournoi
create_tournament.player_register = [player1, player2, player3, player4]

# Création du contrôleur de tournoi
controller_tournament = ControllerTournoi(create_tournament)


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
    print("3. Appliquer le nombre de rounds")
    print("4. Lancement du tournoi")
    print("5. Simuler les matchs d'une ronde")
    print("6. Affichage du classement des joueurs")
    print("7. Affichage des appariements d'une ronde")
    print("8. Quitter")

    choice = input("Sélectionnez une option : ")

    if choice == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
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
        os.system('cls' if os.name == 'nt' else 'clear')
        """Inscription d'un joueur"""
        first_name = input("Entrez le prénom du joueur : ")
        last_name = input("Entrez le nom du joueur : ")
        date_of_birth = input("Entrez la date de naissance du joueur (YYYY-MM-DD) : ")
        classement = float(input("Entrez le classement du joueur : "))
        new_player = Joueur(first_name, last_name, date_of_birth, classement)
        controller_tournament.register_player(new_player)
        print("Joueur inscrit avec succès !")

    elif choice == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        """Création d'un round"""
        ronde_controller = controller_tournament.create_ronde()
        print(f"Ronde {ronde_controller.number_ronde} créée !")

    elif choice == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        """Lancement du tournoi"""
        create_tournament.mark_as_done()
        print("Le tournoi est marqué comme terminé.")

    elif choice == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        """Simulation des matchs d'une ronde"""
        round_number = int(input("Entrez le numéro de la ronde : "))
        ronde_controller = create_tournament.turns[round_number - 1]
        simuler_matchs(ronde_controller)

    elif choice == "6":

        os.system('cls' if os.name == 'nt' else 'clear')
        """Affichage du classement des joueurs"""
        vue_classement = VueClassement()
        vue_classement.display_classement(create_tournament)
        input("Appuyez sur Entrée pour continuer...")

    elif choice == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        """Affichage des appariements d'une ronde"""
        round_number = int(input("Entrez le numéro de la ronde : "))
        ronde_controller = create_tournament.turns[round_number - 1]
        vue_appariements = VueAppariements()
        vue_appariements.display_appariements(ronde_controller)
        input("Appuyez sur Entrée pour continuer...")

    elif choice == "8":
        """Quitter le programme"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fermeture...")
        break

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Choix invalide. Veuillez sélectionner une option valide.")


# Afficher les informations sur le tournoi
print("Tournoi :", create_tournament.name_tournament)
print("Lieu :", create_tournament.place)
print("Date de début :", create_tournament.start_date)
print("Date de fin :", create_tournament.end_date)
print("Nombre de tours :", create_tournament.number_turn)
print("Tour actuel :", create_tournament.current_turn)
print("Remarques :", create_tournament.remarques)
