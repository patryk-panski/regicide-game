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
        return self.name.value + self.suit.value


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
