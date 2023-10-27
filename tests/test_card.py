import unittest

from regicide_game.card import CardName, Suit, create_castle_deck, create_tavern_deck


class TestCreateCastleDeck(unittest.TestCase):
    def test_that_it_returns_complete_set_of_suits_for_jacks_queens_and_kings(self):
        suits = list(Suit)
        suits.remove(Suit.JESTER)

        castle_deck = create_castle_deck()

        jacks_suits = [x.suit for x in castle_deck[0:4]]
        queens_suits = [x.suit for x in castle_deck[4:8]]
        kings_suits = [x.suit for x in castle_deck[8:12]]

        for suit in suits:
            self.assertIn(suit, jacks_suits)
            self.assertIn(suit, queens_suits)
            self.assertIn(suit, kings_suits)

    def test_that_it_returns_4jacks_4queens_and_4kings_in_order(self):
        castle_deck = create_castle_deck()

        self.assertEqual(len(castle_deck), 12)

        for i in range(0, 12):
            if i <= 3:
                self.assertEqual(castle_deck[i].name, CardName.JACK)
            elif i <= 7:
                self.assertEqual(castle_deck[i].name, CardName.QUEEN)
            else:
                self.assertEqual(castle_deck[i].name, CardName.KING)


class TestCreateTavernDeck(unittest.TestCase):
    def test_there_are_all_expected_card_names_4each_with_unique_suits(self):
        tavern_deck = create_tavern_deck(3)

        card_names = list(CardName)
        card_names = [
            e
            for e in card_names
            if e not in (CardName.JACK, CardName.QUEEN, CardName.KING, CardName.JESTER)
        ]

        # dictionary holding a CardName to list of suits mapping
        unique_cards = {}

        for name in card_names:
            unique_cards[name] = []

        # iterate over the tavern deck and add the card:suit pairing to the dictionary
        for card in tavern_deck:
            if (
                card.name != CardName.JESTER
                and card.suit not in unique_cards[card.name]
            ):
                unique_cards[card.name].append(card.suit)

        # validate each card in the dictionary is assigned a list of length 4
        for card in unique_cards:
            self.assertEqual(len(unique_cards[card]), 4)


if __name__ == "__main__":
    unittest.main()
