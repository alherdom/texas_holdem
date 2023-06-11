from __future__ import annotations

class Card:
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    
    def __init__(self, card: str) -> None:
        self.value_suit = card
        self.value = Card.SYMBOLS.index(card[:-1]) + 1
        self.suit = card[-1]
    
    def __repr__(self) -> str:
        return self.value_suit
    
    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE
    
    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE
    
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
    
    def __init__(self, cards: list[Card]) -> None:
        self.hand = cards
        self.cat: int
        self.cat_rank: str | tuple[str]
    
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
    
    def __gt__(self, other):
        pass
        
    def __eq__(self, other):
        for card1, card2 in zip(self, other):
            if card1 != card2:
                return False
            else:
                return True
            

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
    
new_card = Card('A❤')
print(new_card)
cards1 = [Card('A❤'),Card('A❤'),Card('A❤'),Card('A❤'),Card('A❤')]
new_hand1 = Hand(cards1)
print(new_hand1)
cards2 = [Card('A❤'),Card('A❤'),Card('A❤'),Card('8❤'),Card('A❤')]
new_hand2 = Hand(cards2)
print(new_hand2)
# print(new_hand1 == new_hand2)
card1 = Card('A❤')
card2 = Card('K❤')
print(card1 > card2)
print(card1 < card2)
print(card2 > card1)
print(card2 < card1)
print(card1 == card2)
print(card1.cmp_value)
print(card2.cmp_value)