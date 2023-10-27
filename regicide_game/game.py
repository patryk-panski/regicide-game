from typing import List

from regicide_game.card import Card, create_castle_deck, create_tavern_deck
from regicide_game.player import Player

# constants throughout the game
NUMBER_OF_PLAYERS = 3
MAX_HAND_SIZE = 9 - NUMBER_OF_PLAYERS


class Game:
    # state of the game
    castle_deck: List(Card)
    tavern_deck: List(Card)
    discard_pile: List(Card)
    current_player: Player
    standby_players: List(Player)
    current_enemy: Card
    attackers: List(Card)

    # setup the game
    def __init__(self) -> None:
        self.castle_deck = create_castle_deck()
        self.tavern_deck = create_tavern_deck(NUMBER_OF_PLAYERS)
        self.discard_pile = []
        # TODO
