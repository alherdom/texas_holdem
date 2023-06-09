from cards import Card, Hand
from roles import Player

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    player1, player2 = players
    player1.set_private_cards(private_cards[0])
    player2.set_private_cards(private_cards[1])
    player1.set_common_cards(common_cards)
    player2.set_common_cards(common_cards)
    hand1 = player1.get_best_hand()
    hand2 = player2.get_best_hand()
    return hand1, hand2