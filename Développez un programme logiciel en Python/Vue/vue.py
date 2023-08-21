"""VUE"""


# Définir la classe VueClassement pour afficher les classements des joueurs dans un tournoi
class VueClassement:
    def display_classement(self, tournament):
        """Trier les joueurs en fonction de leur classement"""
        classement = sorted(tournament.player_register, key=lambda player_tri: player_tri.classement)
        for index, player in enumerate(classement, 1):
            print(f"{index}. {player}")


# Définir la classe VueAppariements pour afficher les appariements des parties pour une ronde donnée
class VueAppariements:
    def display_appariements(self, ronde):
        print(f"Ronde {ronde.number_ronde}")
        for games in ronde.matchs:
            player_uno, score1 = games.match[0]
            player_dos, score2 = games.match[1]
            print(f"{player_uno.first_name} ({score1}) vs {player_dos.first_name} ({score2})")