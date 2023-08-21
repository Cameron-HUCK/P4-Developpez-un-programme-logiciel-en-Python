from Vue.vue import VueClassement, VueAppariements
from Controleur.controleur import ControllerPartie, ControllerTournoi
from Modèle.modele import Joueur, Tournoi, Tour, Ronde, Partie


# Créer des instances de joueurs
player1 = Joueur("Wonderland", "Alice", "2000-01-01", 1500)
player2 = Joueur("Builder", "Bob", "2000-01-02", 1400)
player3 = Joueur("Green", "Eve", "2000-01-03", 1600)
player4 = Joueur("Johnson", "Carl", "2000-01-04", 1450)

# Créer des instances de parties (matchs 1)
game_1 = Partie(player1, 1, player2, 0)
game_2 = Partie(player3, 0.5, player4, 0.5)

# Créer une instance de ronde 1 et ajouter les matchs
ronde_1 = Ronde(1)
ronde_1.add_match(game_1)
ronde_1.add_match(game_2)

# Créer des instances de parties (matchs 2)
game_3 = Partie(player1, 0.5, player3, 0.5)
game_4 = Partie(player2, 1, player4, 0)

# Créer une instance de la ronde 2 et ajouter les matchs
ronde_2 = Ronde(2)
ronde_2.add_match(game_3)
ronde_2.add_match(game_4)

# Créer une instance de ronde et ajouter les matchs
game_5 = Partie(player1, 0, player4, 1)
game_6 = Partie(player2, 0.5, player3, 0.5)

ronde_3 = Ronde(3)
ronde_3.add_match(game_5)
ronde_3.add_match(game_6)

# Créer une instance de tournoi et ajouter les rondes
create_tournament = Tournoi("Tournoi d'échecs", "Salle des échecs", "2023-07-17", "2023-07-24")
create_tournament.add_turn(ronde_1)
create_tournament.add_turn(ronde_2)
create_tournament.add_turn(ronde_3)

# Inscrire des joueurs au tournoi
create_tournament.register_player(player1)
create_tournament.register_player(player2)
create_tournament.register_player(player3)
create_tournament.register_player(player4)


# Parcourir les rondes et afficher les détails du tournoi
for ronde in create_tournament.turns:
    print(f"\nRonde {ronde.number_ronde}")
    for match in ronde.matchs:
        player1, score1 = match.match[0]
        player2, score2 = match.match[1]
        print(f"{player1.first_name} ({score1}) vs {player2.first_name} ({score2})")


# Créer une instance du ControllerTournament
controller_tournament = ControllerTournoi(create_tournament)

# Menu interactif pour la création et la gestion de tournois
while True:
    print("\nMenu:")
    print("1. Create Tournament")
    print("2. Register Player")
    print("3. Create Round")
    print("4. Record Match Result")
    print("5. Display Player Rankings")
    print("6. Display Round Pairings")
    print("7. Remove Player")
    print("8. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        """Create a new tournament"""
        name = input("Enter tournament name: ")
        place = input("Enter tournament location: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        number_turns = int(input("Enter number of turns: "))
        create_tournament = Tournoi(name, place, start_date, end_date, number_turns)
        controller_tournament = ControllerTournoi(create_tournament)
        print("Tournament created!")

    elif choice == "2":
        """Register a player"""
        first_name = input("Enter player's first name: ")
        last_name = input("Enter player's last name: ")
        date_of_birth = input("Enter player's date of birth (YYYY-MM-DD): ")
        classement = float(input("Enter player's ranking: "))
        new_player = Joueur(first_name, last_name, date_of_birth, classement)
        controller_tournament.subscribe_player(new_player)
        print("Player registered successfully!")

    elif choice == "3":
        """Create a round"""
        ronde_controller = controller_tournament.create_ronde()
        print(f"Round {ronde_controller.number_ronde} created!")

    elif choice == "4":
        """Record match result"""
        round_number = int(input("Enter the round number: "))
        score1 = float(input("Enter player 1's score: "))
        score2 = float(input("Enter player 2's score: "))
        ronde_controller = create_tournament.turns[round_number - 1]
        game_1 = Partie(ronde_controller.matchs[0][0], score1, ronde_controller.matchs[0][1], score2)
        controller_partie = ControllerPartie(ronde_controller)
        controller_partie.save_result(game_1, score1, score2)
        print("Match result recorded!")

    elif choice == "5":
        """Display player rankings"""
        vue_classement = VueClassement()
        vue_classement.display_classement(create_tournament)

    elif choice == "6":
        """Display round pairings"""
        round_number = int(input("Enter the round number: "))
        ronde_controller = create_tournament.turns[round_number - 1]
        vue_appariements = VueAppariements()
        vue_appariements.display_appariements(ronde_controller)

    elif choice == "7":
        """Remove a player"""
        player_name = input("Enter player's first name to remove: ")
        player_found = None
        for player in create_tournament.player_register:
            if player.first_name.lower() == player_name.lower():
                player_found = player
                break
        if player_found:
            create_tournament.player_register.remove(player_found)
            print(f"Player {player_found.first_name} removed from the tournament.")
        else:
            print(f"No player with the name {player_name} found.")

    elif choice == "8":
        """Exit the program"""
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")


# Créer une ronde et l'ajouter au tournoi
ronde_controller = controller_tournament.create_ronde()

# Créer des parties (matchs) et les ajouter à la ronde
game_1 = Partie(player1, 1, player2, 0)
game_2 = Partie(player3, 0.5, player4, 0.5)
ronde_controller.add_match(game_1)
ronde_controller.add_match(game_2)

# Enregistrer les résultats des parties
controller_partie = ControllerPartie(ronde_controller)
controller_partie.save_result(game_1, 1, 0)
controller_partie.save_result(game_2, 0.5, 0.5)

# Afficher les classements des joueurs
vue_classement = VueClassement()
vue_classement.display_classement(create_tournament)

# Afficher les appariements des parties pour une ronde donnée
vue_appariements = VueAppariements()
vue_appariements.display_appariements(ronde_controller)

# Simuler la fin du tournoi
create_tournament.mark_as_done()

# Afficher les informations sur le tournoi
print("Tournoi :", create_tournament.name_tournament)
print("Lieu :", create_tournament.place)
print("Date de début :", create_tournament.start_date)
print("Date de fin :", create_tournament.end_date)
print("Nombre de tours :", create_tournament.number_turn)
print("Tour actuel :", create_tournament.current_turn)
print("Remarques :", create_tournament.remarques)
