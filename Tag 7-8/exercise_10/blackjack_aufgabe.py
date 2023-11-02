import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value_card(self):
        if self.value in ["Jack", "Queen", "King"]:
            return 10
        elif self.value == "Ace":
            return 11
        else:
            return self.value


class Deck:
    def __init__(self):
        self.list_of_cards = []

        list_of_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        list_of_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        for suit in list_of_suits:
            for value in list_of_values:
                new_card = Card(value, suit)
                self.list_of_cards.append(new_card)

    def cards_shuffle(self):
        random.shuffle(self.list_of_cards)

    def draw_card(self):
        if len(self.list_of_cards) == 0:
            return None
        else:
            drawcard = self.list_of_cards.pop(0)
            return drawcard


class Hand:
    def __init__(self, value_of_hand):
        self.hand_cards = []
        self.value_of_hand = value_of_hand

    def add_card(self, card):
        pass

    def get_hand_value(self):
        pass
