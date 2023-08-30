from datetime import datetime


"""Modèle"""


# Définir une classe 'Joueur' pour représenter un joueur
class Joueur:
    def __init__(self, first_name, name, date_of_birth, classement):
        self.first_name = first_name  # Prénom du joueur
        self.name = name  # Nom du joueur
        self.date_of_birth = date_of_birth  # Date de naissance du joueur
        self.classement = classement  # Classement du joueur

    def __str__(self):
        return f"Nom : {self.first_name}," \
               f" Prénom : {self.name}," \
               f" Date de naissance : {self.date_of_birth}," \
               f" Classement : {self.classement}"

    def total_score(self, tournament):
        total = 0
        for ronde in tournament.turns:
            for game in ronde.matchs:
                player1, score1 = game.match[0]
                player2, score2 = game.match[1]
                if player1 == self:
                    total += score1
                elif player2 == self:
                    total += score2
        return total


# Définir une classe 'Tournoi' pour représenter un tournoi d'échecs
class Tournoi:
    def __init__(self, name_tournament, place, start_date, end_date, number_turn=4, current_turn=1):
        self.name_tournament = name_tournament  # Nom du tournoi
        self.place = place  # Lieu du tournoi
        self.start_date = start_date  # Date de début du tournoi
        self.end_date = end_date  # Date de fin du tournoi
        self.number_turn = number_turn  # Nombre de tours dans le tournoi (par défaut 4)
        self.current_turn = current_turn  # Tour actuel du tournoi (initialisé à 1)
        self.player_register = []  # Liste des joueurs inscrits au tournoi
        self.turns = []  # Liste des tours du tournoi
        self.remarques = ""  # Remarques concernant le tournoi

    """Ajoute un tour au tournoi."""
    def add_turn(self, turn):
        self.turns.append(turn)  # Ajouter un tour à la liste des tours du tournoi

    def register_player(self, player_tournament):
        """Inscrit un joueur au tournoi."""
        self.player_register.append(player_tournament)  # Inscrire un joueur à la liste des joueurs inscrits au tournoi

    def mark_as_done(self):
        """Marque le tournoi comme terminé et met à jour la date de fin."""
        self.current_turn = self.number_turn  # Marquer le tournoi comme terminé en mettant le tour actuel au nombre
        # total de tours
        self.end_date = datetime.now()  # Mettre à jour la date de fin du tournoi avec la date et l'heure actuelles
        for turn in self.turns:
            turn.mark_as_done()  # Marquer tous les tours du tournoi comme terminés


# Définir une classe 'Ronde' pour représenter une ronde dans un tour
class Ronde:
    def __init__(self, number_ronde):
        self.end_date_time = None  # Date et heure de fin de la ronde
        # (initialisée à 'None' car la ronde n'est pas encore terminée)
        self.number_ronde = number_ronde  # Numéro de la ronde
        self.matchs = []  # Liste des matchs dans la ronde

    def add_match(self, game):
        """Ajoute un match à la ronde."""
        self.matchs.append(game)  # Ajouter un match à la liste des matchs de la ronde

    def mark_as_done(self):
        """Marque la ronde comme terminée et met à jour la date de fin."""
        self.end_date_time = datetime.now()
        # Mettre à jour la date et l'heure de fin de la ronde avec l'instant présent


# Définir une classe 'Partie' pour représenter une partie (match) entre deux joueurs
class Partie:
    def __init__(self, player_1, score_1, player_2, score_2):
        self.match = ([player_1, score_1], [player_2, score_2])  # Détails du match sous forme de tuple

    def __str__(self):
        player_1, score_1 = self.match[0]
        player_2, score_2 = self.match[1]
        """Format d'affichage pour la partie"""
        return f"{player_1.first_name} ({score_1}) vs {player_2.first_name} ({score_2})"