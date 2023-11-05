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
    active_player: Player
    standby_players: List(Player)
    current_enemy: Card
    attackers: List(Card)

    # setup the game
    def __init__(self) -> None:
        self.castle_deck = create_castle_deck()
        self.tavern_deck = create_tavern_deck(NUMBER_OF_PLAYERS)
        self.discard_pile = []

        # create players
        for i in range(NUMBER_OF_PLAYERS):
            self.standby_players.append(Player(MAX_HAND_SIZE, self.tavern_deck))

        self.current_enemy = self.castle_deck.pop(0)
        self.attackers = []

    # play the game
    def play(self):
        """
        All high-level logic of the game happens here.
        """
        game_over = False

        # while the game is on, play all turns player by player
        while not game_over:
            # Choose a player to go next
            if self.active_player is None:
                self.active_player = self.standby_players[0]
            else:
                self.standby_players.append(self.active_player)
                self.active_player = self.standby_players[0]

            # STEP 1
            self.attack_the_enemy()

            # STEP 3
            is_defeated = self.damage_the_enemy()

            if is_defeated:
                # if defeated, set a new current enemy
                # if enemy is defeated, place all attackers cards in the discard pile
                # if enemy is defeated, skip turn 4 and the player who defeated the enemy plays first
                pass
            else:
                # STEP 4
                game_over = self.take_damage()

    # run step 1 - play a card
    def attack_the_enemy(self):
        """
        The active player plays a card from their hand to attack the enemy.

        The played card will be added to attackers list of cards.
        """
        self.attackers.append(self.active_player.play_card())

    # run step 2 (this is extra, to be done later)

    # run step 3 - deal damage
    def damage_the_enemy(self):
        """
        Deal damage to enemy and check if they are defeated.

        """
        is_defeated = False

        # check if the total damage of the attackers is equal or greater to the enemy's health

        # if it is equal, place the defeated enemy card on top (front) of the tavern deck

        # if it is greater, place the defeated enemy card in the discard pile

        return is_defeated

    # run step 4 - suffer damage
    def take_damage(self):
        return self.active_player.suffer_damage(
            self.current_enemy.power, self.discard_pile
        )
