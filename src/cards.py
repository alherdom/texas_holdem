from __future__ import annotations

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
        value = card[:-1]
        self.value = Card.SYMBOLS.index(value) + 1
        self.suit = card[-1]
    
    def __repr__(self) -> str:
        return Card.GLYPHS[self.suit][self.value -1]
    
    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE
    
    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE
    
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
    
    def __init__(self, cards: list[Card]) -> None:
        self.cat = 1
        self.hand = cards
    
    def __getitem__(self, index: int) -> Card:
        return self.hand[index]
    
    def __len__(self) -> int:
        return len(self.hand)
    
    def __iter__(self) -> HandIterator:
        return HandIterator(self)
    
    def __repr__(self) -> str:
        return " ".join(str(card) for card in self.hand)

class HandIterator:
    def __init__(self, hand: Hand):
        self.hand = hand
        self.counter = 0

    def __next__(self) -> int:
        if self.counter >= len(self.hand):
            raise StopIteration
        item = self.hand[self.counter]
        self.counter += 1
        return item
    
new_card = Card('A❤')
print(new_card)

new_hand = Hand([Card('A❤'), Card('10❤'), Card('A♠'), Card('Q❤'), Card('K♣')])
print(new_hand)
for card in new_hand:
    print(card.cmp_value)