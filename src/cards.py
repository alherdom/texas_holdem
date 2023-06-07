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
        value = card[:len(card)-1]
        self.value = Card.SYMBOLS.index(value) + 1
        self.suit = card[-1]
        
    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE
    
    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE
    
    def __repr__(self) -> str:
        return Card.GLYPHS[self.suit][self.value -1]
    
    def __eq__(self, other: Card) -> bool:
        return self.cmp_value == other.cmp_value and self.suit == other.suit
    
    def __lt__(self, other: Card) -> bool:
        return self.cmp_value == min(self.cmp_value, other.cmp_value)