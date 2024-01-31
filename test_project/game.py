import random

from object import Deck, Player


class TexasHoldem:
    def __init__(self, players: int):
        self.players = [Player() for i in range(players)]
        self.deck = Deck()
        self.deck.shuffle()
        self.board = []

    def play(self):
        # Hand count
        count = 1
        # Dealer index
        didx = random.randint(0, len(self.players))
        while True:
            # Small blind index
            sbidx = (didx + 1) % len(self.players)
            # Big blind index
            bbidx = (didx + 2) % len(self.players)

            print("*** HAND", count, "***\n")
            print("Player " + str(didx + 1) + " is the dealer")
            print("Player " + str(sbidx + 1) + " is small blind")
            print("Player " + str(bbidx + 1) + " is big blind\n")

            self.deal(didx)

            print("Hands:", self.get_hands(), "\n")

            self.flop()
            input()
            self.turn()
            input()
            self.river()
            input()

            self.shuffle()
            didx = (didx + 1) % len(self.players)
            count += 1

    def shuffle(self):
        for player in self.players:
            player.hand = []
        self.deck = Deck()
        self.deck.shuffle()

    def deal(self, didx: int):
        players = len(self.players)
        # For each player starting at the dealer, circularly deal cards
        for i in range(players * 2):
            player = self.players[(i + didx) % players]
            player.hand.append(self.deck.deck.pop(0))

    def get_hands(self):
        return [[str(card) for card in player.hand] for player in self.players]

    def get_deck(self):
        return [str(card) for card in self.deck.deck]

    def get_board(self):
        return [str(card) for card in self.board]

    def flop(self):
        self.deck.burn()
        self.board = self.deck.deck[:3]
        self.deck.deck = self.deck.deck[3:]
        print("Flop:", self.get_board())

    def turn(self):
        self.deck.burn()
        self.board.append(self.deck.deck.pop(0))
        print("Turn:", self.get_board())

    def river(self):
        self.deck.burn()
        self.board.append(self.deck.deck.pop(0))
        print("River:", self.get_board())


if __name__ == "__main__":
    TexasHoldem(5).play()
