from cards import Card, Hand
from helpers import combinations

class Player:
    def __init__(self, name: str):
        self.name = name
        self.private_cards = []
        self.common_cards = []
    
    def set_private_cards(self, private_cards: list[Card]):
        self.private_cards = private_cards
    
    def set_common_cards(self, common_cards: list[Card]):
        self.common_cards = common_cards
    
    def get_player_cards(self):
        return self.private_cards + self.common_cards
    
    def __str__(self):
        cards = " ".join(str(card) for card in self.private_cards)
        return f"{self.name}, {cards}"
    
    def get_hand(self) -> Hand:
        values = []
        suits = []
        dist_values = set(values)
        dist_suits = set(suits)
        len_dist_values = len(dist_values)
        len_dist_suits = len(dist_suits)
        cards_combinations = list(combinations(self.get_player_cards(), n = 5))
        for combination in cards_combinations:           
            for card in sorted(combination, key = lambda c: c.cmp_value):
                values.append(card.cmp_value)
                suits.append(card.suit)
            if len(values) == 5:
                values = []
            if len(suits) == 5:
                suits = []
            for value in values:
                if values.count(value) == 4:
                    return Hand(combination) #'POKER'
                if values.count(value) == 3:
                    if values.count(value[4]) == 2:
                        return Hand(combination) #'FULL HOUSE'
                    else:
                        return Hand(combination) #'THREE'
                if (values[0]) - (values[-1]) == 4 and len(dist_values) == 5 and len(dist_suits) == 1:
                    return Hand(combination) #'STRAIGHT_FLUSH'
                if len_dist_suits == 1:
                    return Hand(combination) #'FLUSH'
                if (values[0]) - (values[-1]) == 4 and len(dist_values) == 5:
                    return Hand(combination) #'STRAIGHT'
                if len_dist_values == 3:
                    return Hand(combination) #'TWO_PAIR'
                if len_dist_values == 4:
                    return Hand(combination) #'ONE_PAIR'
                else:
                    return Hand(combination) #'HIGH_CARD'