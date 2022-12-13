import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('tarot',1)
        self.card2= Card('hearts', 10)
        self.card= Card('tarot', 8)
        self.cards =[self.card1, self.card, self.card2]

        self.cardgame = CardGame()

    def test_check_for_ace(self):
        result = self.cardgame.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_highest_card(self):
        result = self.cardgame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        result = self.cardgame.cards_total(self.cards)
        self.assertEqual(result, "You have a total of 19")


