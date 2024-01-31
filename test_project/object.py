import itertools
import random


class Card(object):
    SUITS = ["C", "D", "H", "S"]
    RANKS = [i for i in range(2, 15)]

    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank == 14:
            rank = "A"
        elif self.rank == 13:
            rank = "K"
        elif self.rank == 12:
            rank = "Q"
        elif self.rank == 11:
            rank = "J"
        else:
            rank = self.rank
        return str(rank) + self.suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Deck(object):
    def __init__(self):
        self.deck = []
        deck = list(itertools.product(Card.RANKS, Card.SUITS))
        for card in deck:
            self.deck.append(Card(card[0], card[1]))

    def shuffle(self):
        random.shuffle(self.deck)

    def burn(self):
        self.deck.pop(0)

    def __str__(self):
        return str([str(card) for card in self.deck])


class Player(object):
    def __init__(self):
        self.hand = []

    def __str__(self):
        return str([str(card) for card in self.hand])
