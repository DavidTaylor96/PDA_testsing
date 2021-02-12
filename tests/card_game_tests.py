import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def test_check_for_ace(self):
        ace = Card("Clubs", 1)
        self.assertEqual(True, CardGame().check_for_ace(ace))

    def test_highest_card(self):
        card1 = Card("Diamonds", 5) 
        card2 = Card("Hearts", 10)
        self.assertEqual(card2, CardGame().highest_card(card1, card2))

    def test_cards_total(self):
        card1 = Card("Spades", 10)
        card2 = Card("Diamonds", 1)
        card3 = Card("Hearts", 7)
        total = (card1, card2, card3)

        self.assertEqual(18, CardGame().cards_total(total))