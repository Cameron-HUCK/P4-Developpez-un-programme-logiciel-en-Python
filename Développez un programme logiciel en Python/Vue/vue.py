"""VUE"""


# Définir la classe VueClassement pour afficher les classements des joueurs dans un tournoi
class VueClassement:
    def display_classement(self, tournament):
        classement = sorted(tournament.player_register, key=lambda player: player.total_score(tournament), reverse=True)
        for index, player in enumerate(classement, 1):
            print(f"{index}. {player.first_name} {player.name} - Score: {player.total_score(tournament)}")


# Définir la classe VueAppariements pour afficher les appariements des parties pour une ronde donnée
class VueAppariements:
    def display_appariements(self, ronde):
        print(f"Ronde {ronde.number_ronde}")
        for games in ronde.matchs:
            player_uno, score1 = games.match[0]
            player_dos, score2 = games.match[1]
            print(f"{player_uno.first_name} ({score1}) vs {player_dos.first_name} ({score2})")