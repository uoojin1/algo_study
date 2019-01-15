''' Deck of Cards

Design the data structures for a generic deck of cards.
Explain how you would subclass the data structures to inplement black jack
'''

''' My thoughts
1. Card Class

what is blackjack?
its when the player has 2 cards, and the dealer has 2 cards
who ever is closer and less than 21 wins
'''

class Card:
    def __init__(self, val, suite):
        self.val = None
        self.suite = None
        self.exposed = False
    def getValue(self):
        return self.val
    def getSuite(self):
        return self.suite
    def isExposed(self):
        return self.exposed
    def flip(self):
        self.exposed = !self.exposed

class Hand:
    def __init__(self, cards):
        self.cards = cards
    def getNumberOfCards(self):
        return len(self.cards)
    def throwAwayCard(self):
        self.cards = []
    def throwAwayCard(self, target):
        self.cards = [card for card in self.cards if card != target]
        return target
    def getCard(self, card):
        self.card = self.cards.append(card)

class Deck:
    def __init__(self, number):
        self.number = number
        self.cards = []
    def shuffle(self):
    def dealHand(self, numberOfPlayers):
    def dealCard(self, numberOfCards):
    def remainingCards(self):

class Person:
    def __init__(self, cards = [], type = 'Player'):
        self.cards = cards
        self.type = type

class Player(Person):
    def __init__(self, cards, type):
        Person.__init__(cards, type)

class Dealer(Person):
    def __init__(self, cards, type):
        Person.__init__(cards, type)