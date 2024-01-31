import random
from typing import List

from object import Deck, Player


class Texas(object):
    def __init__(self, players: int):
        self.players = [Player() for i in range(players)]
        self.num = players
        self.deck = Deck()
        self.deck.shuffle()
        self.board = []
        self.didx = random.randint(0, self.num - 1)

    def play(self):
        # Small blind index
        sb = (self.didx + 1) % self.num
        # Big blind index
        bb = (self.didx + 2) % self.num

        print("Player " + str(self.didx + 1) + " is the dealer")
        if self.num > 2:
            print("Player " + str(sb + 1) + " is small blind")
            print("Player " + str(bb + 1) + " is big blind\n")

        self.shuffle()
        self.deal()

        print("Hands:", self.get_hands(), "\n")

        self.flop()
        input()
        self.turn()
        input()
        self.river()
        input()

        self.didx = (self.didx + 1) % self.num

    def shuffle(self):
        for player in self.players:
            player.hand = []
        self.deck = Deck()
        self.deck.shuffle()

    def deal(self):
        # For each player starting at the didx, circularly deal cards
        for i in range(self.num * 2):
            player = self.players[(i + self.didx) % self.num]
            player.hand.append(self.deck.deck.pop(0))

    def get_hands(self) -> List[List[str]]:
        return [[str(card) for card in player.hand] for player in self.players]

    def get_deck(self) -> List[List[str]]:
        return [str(card) for card in self.deck.deck]

    def get_board(self) -> List[List[str]]:
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
    Texas(5).play()
