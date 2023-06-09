from __future__ import annotations
import helpers

class Card:
    GLYPHS = {
        '♣':'🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞',
        '◆':'🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎',
        '❤':'🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾',
        '♠':'🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮'
        }
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    
    def __init__(self, card: str) -> None:
        value = card[:len(card)-1]
        self.value = Card.SYMBOLS.index(value) + 1
        self.suit = card[-1]
    
    def __repr__(self) -> str:
        return Card.GLYPHS[self.suit][self.value -1]
    
    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE
    
    @property
    def cmp_value(self) -> int:
        return int(self.value) if not self.is_ace() else Card.A_VALUE + Card.K_VALUE
    
    def __eq__(self, other: Card) -> bool:
        return self.value == other.value and self.suit == other.suit
    
    def __lt__(self, other: Card) -> bool:
        return self.value == min(self.value, other.value)
    
class Hand:
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    
    def __init__(self, player_cards: list[Card]) -> None:
        self.player_cards = player_cards
        self.cat = 1
    
    def __repr__(self) -> str:
        return ",".join(str(card) for card in self.player_cards)
    
    def get_best_hand(self) -> Hand:
        values = []
        values = sorted(values)
        suits = []
        dist_values = set(values)
        dist_suits = set(suits)
        len_dist_values = len(dist_values)
        len_dist_suits = len(dist_suits)
        cards_combinations = helpers.combinations(self.player_cards, 5)

        for card in cards_combinations:
            values.append(card.value)
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
        self.cat = Hand.HIGH_CARD
        
new_card = Card('K◆')
print(new_card)
print(new_card.cmp_value)