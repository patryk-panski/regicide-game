import unittest

from regicide_game.card import CardName, Suit, create_castle_deck


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


if __name__ == "__main__":
    unittest.main()
