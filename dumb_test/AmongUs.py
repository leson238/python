import random


class Player:
    AVAILABLE_COLOR = {"RED", "BLUE", "CYAN", "LIME", "GREEN",
                       "BROWN", "BLACK", "WHITE", "YELLOW", "PINK"}
    OCCUPIED_COLOR = set()

    def __init__(self, color):
        self.color = color
        self.votes = 0

    @property
    def color(self, player_choice=None):
        if player_choice in Player.AVAILABLE_COLOR:
            Player.AVAILABLE_COLOR.remove(player_choice)
            Player.OCCUPIED_COLOR.add(player_choice)
            return color
        else:
            ai_choice = random.choice(Player.AVAILABLE_COLOR)
            Player.AVAILABLE_COLOR.remove(ai_choice)
            Player.OCCUPIED_COLOR.add(ai_choice)
            return ai_choice

    def change_color(self, player_choice):
        if player_choice in Player.AVAILABLE_COLOR:
            Player.AVAILABLE_COLOR.remove(player_choice)
            Player.OCCUPIED_COLOR.add(player_choice)
            self.color = player_choice
        else:
            print(f"{player_choice} color is not available")

    def get_voted(self):
        self.votes += 1

    def vote(self, who, available_player):
        if who in available_player:
            who.get_voted()
        else:
            print(f"{who.color} does not present in this game")
