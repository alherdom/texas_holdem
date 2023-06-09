from cards import Card, Hand
from roles import Player

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    player1, player2 = players
    pc_player1, pc_player2 = private_cards
    cards_player1 = pc_player1 + common_cards
    cards_player2 = pc_player2 + common_cards
    hand_player1 = Hand(cards_player1)
    hand_player2 = Hand(cards_player2)
    
    return new_player, cards_list
    
    #algo, que tiene que decir que mano es mejor, y que player gana