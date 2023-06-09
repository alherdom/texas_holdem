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
        return self.name
    
    def get_best_hand(self) -> Hand:
        values = []
        suits = []
        dist_values = set(values)
        dist_suits = set(suits)
        len_dist_values = len(dist_values)
        len_dist_suits = len(dist_suits)
        cards_combinations = combinations(self.get_player_cards(), n = 5)
        
        for combination in cards_combinations:
            for card in sorted(combination, key = lambda c: c.cmp_value):
                values.append(card.cmp_value)
                suits.append(card.suit)
        
        for value in values:
            # FOR OF A KIND
            if values.count(value) == 4:
                self.cat = Hand.FOUR_OF_A_KIND
            # THREE OF A KIND or FULL HOUSE
            if values.count(value) == 3:
                if values.count(value[4]) == 2:
                    self.cat = Hand.FULL_HOUSE
                else:
                    self.cat = Hand.THREE_OF_A_KIND

        # STRAIGHT FLUSH
        if max(values) - min(values) == 4 and len(dist_values) == 5 and len(dist_suits) == 1:
            self.cat = Hand.STRAIGHT_FLUSH
        # FLUSH
        if len_dist_suits == 1:
            self.cat = Hand.FLUSH
        # STRAIGHT
        if max(values) - min(values) == 4 and len(dist_values) == 5:
            self.cat = Hand.STRAIGHT
        # TOW PAIR
        if len_dist_values == 3:
            self.cat = Hand.TWO_PAIR
        # ONE PAIR
        if len_dist_values == 4:
            self.cat = Hand.ONE_PAIR
        # HIGH CARD
        else:
            self.cat = Hand.HIGH_CARD
        return self.cat