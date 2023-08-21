"""Controller"""
from Modèle.modele import Ronde


# Définir la classe ControllerTournoi pour gérer la logique du tournoi
class ControllerTournoi:
    def __init__(self, controller_tournament):
        self.controller_tournament = controller_tournament

    def subscribe_player(self, player_tournament):
        """Ajouter un joueur au tournoi"""
        self.controller_tournament.register_player(player_tournament)

    def create_ronde(self):
        """Créer une nouvelle ronde et l'ajouter au tournoi"""
        ronde = Ronde(len(self.controller_tournament.turns) + 1)
        self.controller_tournament.add_turn(ronde)
        return ronde


# Définir la classe ControllerPartie pour gérer la logique d'une partie
class ControllerPartie:
    def __init__(self, ronde):
        self.ronde = ronde

    def add_game(self, game):
        """Ajouter une partie à la ronde"""
        self.ronde.add_match(game)

    def save_result(self, game, score_1, score_2):
        """Enregistrer le résultat de la partie"""
        player_result_1, _ = game.match[0]
        player_result_2, _ = game.match[1]
        game.match = ([player_result_1, score_1], [player_result_2, score_2])