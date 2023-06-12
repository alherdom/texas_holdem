from helpers import combinations
from cards import Card, Hand

class Player:
    def __init__(self, name: str, private_cards: list[Card] = [], common_cards: list[Card] = []):
        self.name = name
        self.private_cards = private_cards
        self.common_cards = common_cards
    
    def __repr__(self) -> str:
        return self.name