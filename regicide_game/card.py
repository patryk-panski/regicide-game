from dataclasses import dataclass
from enum import Enum
from typing import List
import random


class Suit(Enum):
    HEARTS = "❤"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"
    JESTER = ""


class CardName(Enum):
    ACE = "A"
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    JESTER = "JESTER"


@dataclass
class Card:
    name: CardName
    power: int
    health: int
    suit: Suit

    def __repr__(self):
        return str(self.name.value) + self.suit.value


def create_castle_deck() -> List[Card]:
    """
    This creates a deck with Jacks, Queens, Kings, four of each in that order with their suits shuffled.
    Example: J♠,J❤,J♣,J♦,Q♣,Q♦,Q♠,Q❤,K♣,K❤,K♠,K♦
    """
    suits = list(Suit)
    suits.remove(Suit.JESTER)

    jacks = []
    queens = []
    kings = []

    for suit in suits:
        jacks.append(Card(name=CardName.JACK, power=10, health=20, suit=suit))
        queens.append(Card(name=CardName.QUEEN, power=15, health=30, suit=suit))
        kings.append(Card(name=CardName.KING, power=20, health=40, suit=suit))

    random.shuffle(jacks)
    random.shuffle(queens)
    random.shuffle(kings)

    return jacks + queens + kings


def create_tavern_deck(num_players) -> List[Card]:
    """
    This creates a shuffled deck with all the cards numbered 2 to 10 with the 4 Animal Companions (Ace) and Jesters.
    The number of Jesters depends on the number of players.
    """
    if num_players not in [1, 2, 3, 4]:
        raise ValueError(
            f"'{num_players}' is not a valid number of players. Valid number of players are '1', '2', '3', and '4'."
        )

    suits = list(Suit)
    suits.remove(Suit.JESTER)

    tavern_deck = []

    # add 4 copies of each card (2-10 and Aces) with different suits
    for name in CardName:
        for suit in suits:
            if name in [
                CardName.TWO,
                CardName.THREE,
                CardName.FOUR,
                CardName.FIVE,
                CardName.SIX,
                CardName.SEVEN,
                CardName.EIGHT,
                CardName.NINE,
                CardName.TEN,
            ]:
                tavern_deck.append(
                    Card(name=name, power=name.value, health=name.value, suit=suit)
                )
            if name == CardName.ACE:
                tavern_deck.append(Card(name=name, power=1, health=1, suit=suit))

    # add Jesters based on the number of players
    if num_players == 3:
        tavern_deck.append(
            Card(name=CardName.JESTER, power=0, health=0, suit=Suit.JESTER)
        )
    elif num_players == 4:
        tavern_deck.append(
            Card(name=CardName.JESTER, power=0, health=0, suit=Suit.JESTER)
        )
        tavern_deck.append(
            Card(name=CardName.JESTER, power=0, health=0, suit=Suit.JESTER)
        )

    # shuffle the deck
    random.shuffle(tavern_deck)

    return tavern_deck
