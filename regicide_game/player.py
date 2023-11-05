import random
from typing import List

from regicide_game.card import Card


class Player:
    hand: List[Card]

    def __init__(self, max_hand_size, tavern_deck) -> None:
        """
        Deal cards to a player
        """
        if len(tavern_deck) > 0:
            for i in range(min(max_hand_size, len(tavern_deck))):
                self.hand.append(tavern_deck.pop(0))

    def play_card(self) -> Card:
        """
        Plays a random card from the hand.
        """
        if len(self.hand) > 0:
            played_card = random.choice(self.hand)
            self.hand.remove(played_card)

        return played_card

    def discard_card(self, card_to_discard, discard_pile):
        """
        Discards a selected card to the discard pile.
        """
        self.hand.remove(card_to_discard)
        discard_pile.append(card_to_discard)

    def suffer_damage(self, damage, discard_pile) -> bool:
        """
        Discard cards from the hand with a total value at least equal to the enemy's attack value.

        Strategy of discarding: from left to right (simple, refine in the future)

        Returns true if the player successfully takes damage, false if the game is over!
        """
        # check if the damage is higher than the sum of all your cards' health
        player_health = 0
        for card in self.hand:
            player_health += card.power

        # GAME OVER
        if player_health < damage:
            return False
        # discard all cards (the game is not over yet)
        elif player_health == damage:
            discard_pile.append(self.hand)
            self.hand = []
            return True
        # pick cards to discard
        else:
            while damage > 0:
                card_to_discard = self.hand.pop(0)
                damage -= card_to_discard.power
                discard_pile.extends(card_to_discard)
            return True
