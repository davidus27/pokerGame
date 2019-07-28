#!/usr/bin/python
# vim: set fileencoding=utf-8 :

"""
File: dealer.py
Author: dave
Github: https://github.com/davidus27
Description: We need to create a "Dealer" for a game so we can 
    easily manage a pot (money on a table) cards on a table, cards on hands,shuffling and who wins.
"""


import player
import detector
import random


class Dealer(object):
    def __init__(self):
        self.deck = []
        self.players = []
        self.tableCards = []
        self.pot = 0

        self.buildDeck()
        self.shuffle()

    def buildDeck(self):
        """
        Creates list of cards.
        Individual cards are tuples with format: (number,color)
        """
        colors = ["Spades" , "Clubs", "Diamonds", "Hearts"]
        numbers = [2, 3, 4, 5, 6 ,7 ,8 , 9 ,10,"Jack", "Queen","King", "Ace"]
        for color in colors:
            for number in numbers:
                self.deck.append((number,color))
        return self

    def shuffle(self):
        for i in range(len(self.deck)-1 , 0, -1):
            rand = random.randint(0,i)
            self.deck[i], self.deck[rand]= self.deck[rand], self.deck[i]
        return self

    
    def drawCard(self):
        return self.deck.pop()

            
    def dealCard(self):
        """
        Deals cards to everyone
        :returns: self

        """
        for i in self.players:
            i.hand.append(self.drawCard())
        return self 


    def drawTable(self):
        """
        Draw a card on table
        :returns: TODO

        """
        self.tableCards.append(self.drawCard())
        return self

    def listCards(self, player):
        """
        Creates the list of cards for specific player

        :player: object Player()
        :returns: list of cards on table and hand of specific player

        """
        return self.tableCards + player.hand


    def addPlayer(self,player):
        self.players.append(player)
        return self


    def createPlayers(self,numPlayers , name,money, difficulty="easy"):
        """
        Create individual player and his opponents based on difficulty
        """
        self.addPlayer(player.Player(name,money))
        for i in range(1,numPlayers+1):
            if difficulty == "easy":
               self.addPlayer(player.EasyBot())
               self.players[i].name +=str(i)
        return self


    
    def findHandValue(self, player):
        """
        Goes through the list of possible hands to find best one from top to the bottom

        :player: TODO
        :returns: float/int hand value of the player

        """
        d = detector.Detector()
        cards = d.sortCards(self.listCards(player))
        histogram = d.createHistogram(cards)
        options = [d.royalFlush(cards),
                   d.straightFlush(cards),
                   d.fullHouse(histogram, cards),
                   d.flush(cards),
                   d.fourOfKind(histogram, cards),
                   d.threeOfKind(histogram, cards),
                   d.twoPairs(histogram, cards),
                   d.pair(histogram, cards),]
        
        for index,option in enumerate(options):
            if option:
                return 8 - index #+ d.highCard(option)
        return False
        #return d.highCard(cards)
