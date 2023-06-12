from __future__ import annotations


class Card:
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    REAL_A_VALUE = 14
   
    def __init__(self, card: str):
        self.suit = card[-1]
        self.value_suit = card
        self.value = Card.SYMBOLS.index(card[:-1]) + 1

    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.REAL_A_VALUE
    
    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE

    def __repr__(self) -> str:
        return self.value_suit
    
    def __eq__(self, other: Card) -> bool:
        return self.cmp_value == other.cmp_value
    
    def __gt__(self, other: Card) -> bool:
        return self.cmp_value > other.cmp_value
    
    def __lt__(self, other: Card) -> bool:
        return self.cmp_value < other.cmp_value


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
    
    def __init__(self, cards: list[Card]):
        self.hand = cards

    def __getitem__(self, index: int) -> Card:
        return self.hand[index]
    
    def __len__(self) -> int:
        return len(self.hand)
    
    def __iter__(self) -> HandIterator:
        return HandIterator(self)
    
    def __repr__(self) -> str:
        return " ".join(str(card) for card in self.hand)
    
    def __contains__(self, card: Card):
        return card in self.hand
    
    # CORREGIR MÉTODOS MÁGICOS, POSIBLES FALLOS EN __gt__ Y __eq__ !
    def __gt__(self, other) -> bool:
        if self.cat > other.cat:
            return True
        if self == other:
            if sum([card.cmp_value for card in self]) > sum([card.cmp_value for card in other]):
                return True
        if self.cat == other.cat:
            if self.cat_rank > other.cat_rank:
                return True
            return False
        return False
        
    def __eq__(self, other) -> bool:
        return self.cat == other.cat and self.cat_rank == other.cat_rank
    
    def is_straight_flush(self, values: list[int], len_set_values: int, len_set_suits: int) -> bool:
        return len_set_suits == 1 and len_set_values == 5 and values[-1] - values[0] == 4
    
    def is_four_of_a_king(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 2 and values[0] == values[3]
    
    def is_full_house(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 2 and values[2] != values[3]
    
    def is_flush(self, len_set_suits: int) -> bool:
        return len_set_suits == 1
    
    def is_straight(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 5 and values[-1] - values[0] == 4
    
    def is_three_of_a_kind(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 3 and values[1] == values[2]
    
    def is_two_pair(self, values: list[int], len_set_values: int) -> bool:
        return len_set_values == 3 and values[1] != values[2]
    
    def is_one_pair(self, len_set_values: int) -> bool:
        return len_set_values == 4
    
    @property
    def cat(self) -> int:
        values = [card.value for card in self.hand]
        values = sorted(values, key=lambda v: values.count(v), reverse=True)
        suits = [card.suit for card in self.hand]
        len_set_values = len(set(values))
        len_set_suits = len(set(suits))
        if self.is_straight_flush(values, len_set_values, len_set_suits):
            return Hand.STRAIGHT_FLUSH
        if self.is_four_of_a_king(values, len_set_values):
            return Hand.FOUR_OF_A_KIND
        if self.is_full_house(values, len_set_values):
            return Hand.FULL_HOUSE
        if self.is_flush(len_set_suits):
            return Hand.FLUSH
        if self.is_straight(values, len_set_values):
            return Hand.STRAIGHT
        if self.is_three_of_a_kind(values, len_set_values):
            return Hand.THREE_OF_A_KIND
        if self.is_two_pair(values, len_set_values):
            return Hand.TWO_PAIR
        if self.is_one_pair(len_set_values):
            return Hand.ONE_PAIR
        return Hand.HIGH_CARD
    
    @property
    def cat_rank(self) -> str | tuple[str]:
        values = [card.value for card in self.hand]
        values = sorted(values, key=lambda v: values.count(v), reverse=True)
        item1 = Card.SYMBOLS[values[0] - 1]
        if self.cat in [Hand.ONE_PAIR, Hand.THREE_OF_A_KIND, Hand.FOUR_OF_A_KIND]:
            return item1
        if self.cat == Hand.TWO_PAIR:
            item2 = Card.SYMBOLS[values[2] - 1]
            return tuple(sorted((item1, item2), reverse = True))
        if self.cat == Hand.FULL_HOUSE:
            item2 = Card.SYMBOLS[values[3] - 1]
            return item1, item2
        return Card.SYMBOLS[max(values) - 1]
        
class HandIterator:
    def __init__(self, hand: Hand):
        self.hand = hand
        self.counter = 0

    def __next__(self) -> Card:
        if self.counter >= len(self.hand):
            raise StopIteration
        item = self.hand[self.counter]
        self.counter += 1
        return item
    
# new_hand = Hand([Card('K❤'), Card('K◆'), Card('3❤'), Card('3◆'), Card('A◆')])
# new_hand = Hand([Card('A♠'), Card('A♣'), Card('Q♠'), Card('Q♣'), Card('J♣')])
# print(new_hand.cat)
# print(new_hand.cat_rank)
# print(new_hand)