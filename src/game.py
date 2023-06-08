from cards import Card, Hand
from roles import Player

class Game:
    def __init__(self, players):
        self.players = players
    
    def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
        common_cards