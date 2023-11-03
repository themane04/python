import random
import time


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{self.suit}"

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

        list_of_suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
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
    def __str__(self):
        return ", ".join([card for card in self.hand_cards])

    def __init__(self, value_of_hand=0, player_chip=0, player_balance=0, bet_amount=0):
        self.bet_amount = bet_amount
        self.player_balance = player_balance
        self.player_chips = player_chip
        self.hand_cards = []
        self.value_of_hand = value_of_hand

    def add_card(self, card):
        self.hand_cards.append(card)
        if card.value in ["Jack", "Queen", "King"]:
            self.value_of_hand += 10
        elif card.value != "Ace":
            self.value_of_hand += int(card.value)
        else:
            if self.value_of_hand + 11 <= 21:
                self.value_of_hand += 11
            else:
                self.value_of_hand += 1

        if self.value_of_hand > 21:
            for c in self.hand_cards:
                if c.value == "Ace" and c.value != 1:
                    self.value_of_hand -= 10
                    if self.value_of_hand <= 21:
                        break

    def get_hand_value(self):
        return self.value_of_hand

    def is_blackjack(self):
        if len(self.hand_cards) == 2:
            card_values = [card.value for card in self.hand_cards]
            if "Ace" in card_values:
                card_values.remove("Ace")
                if card_values[0] in ["10", "Jack", "Queen", "King"]:
                    return True
        return False


class Player(Hand):

    def player_bet(self):
        self.bet_amount = int(input("Enter bet amount:"))
        if self.bet_amount <= self.player_balance:
            self.player_balance -= self.bet_amount
            print(f"Bet placed of", self.bet_amount, ". Remaining balance is ", self.player_balance)
        else:
            print("Insufficient balance to place bet.")

    def player_win(self):
        winnings = self.bet_amount * 2
        self.player_balance += winnings
        print("Congratulations! You've won: ", winnings)
        print("You Win! Your new balance is: ", self.player_balance)

    def player_lose(self):
        print("Sorry, you lost")
        print("Your balance: ", self.player_balance)


class Dealer(Hand):
    pass


def dot_animation():
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0)
    print()


def gameover_animation():
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print()


print("Prepare to lose everything.")
dot_animation()

running = True
while running:

    player_chips = int(input("Enter starting chips: "))
    chip_target = int(input("Enter chip target: "))
    dot_animation()

    while 0 < player_chips < chip_target:
        deck = Deck()
        deck.cards_shuffle()
        print("The round starts now.")
        player_bet = int(input("Bet amount: "))

        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.draw_card())
        player_hand.add_card(deck.draw_card())

        dealer_hand.add_card(deck.draw_card())
        dealer_hand.add_card(deck.draw_card())

        dot_animation()
        print("Your hand: ", *player_hand.hand_cards, "-Total value: ", player_hand.get_hand_value())
        print("Dealer shows: ", dealer_hand.hand_cards[0], "-Total value: ", dealer_hand.hand_cards[0].value)

        player_choice = input("Hit or stand?: ").upper()
        while player_choice == "HIT":
            player_hand.add_card(deck.draw_card())
            dealer_hand.add_card(deck.draw_card())
            print("Your hand: ", *player_hand.hand_cards, "-Total value: ", player_hand.get_hand_value())
            if player_hand.get_hand_value() > 21:
                break
            player_choice = input("Hit or stand?: ").upper()

        if player_hand.get_hand_value() <= 21:
            while dealer_hand.get_hand_value() < 17:
                dealer_hand.add_card(deck.draw_card())

        print("Dealer's hand: ", dealer_hand, "-Total value: ", dealer_hand.get_hand_value())

        print("Your hand: ", player_hand, "-Total value: ", player_hand.get_hand_value())
        if player_hand.get_hand_value() > 21:
            print("Bust! You lose.")
            player_chips -= player_bet
        elif dealer_hand.get_hand_value() > 21:
            print("Dealer busts! You win.")
            player_chips += player_bet
        elif player_hand.get_hand_value() == 21 and player_hand.is_blackjack():
            print("Blackjack! You win.")
            player_chips += player_bet
        elif dealer_hand.get_hand_value() == 21 and dealer_hand.is_blackjack() == 2:
            print("Dealer has Blackjack! You lose.")
            player_chips -= player_bet
        elif player_hand.get_hand_value() > dealer_hand.get_hand_value():
            print("You have a higher hand. You win!")
            player_chips += player_bet
        elif player_hand.get_hand_value() < dealer_hand.get_hand_value():
            print("Dealer has a higher hand. You lose.")
            player_chips -= player_bet
        else:
            print("It's a draw!")
        print("Your chip count: ", player_chips)
        if player_chips >= chip_target:
            print("You have reched your chip target!")
            break

        if player_chips <= 0:
            print("You've run out of chips. Either sell your house, car or even your wife.")
            break
        gameover_animation()

print("Game over.")
