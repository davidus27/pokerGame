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
from detector import findHandValue
import random


class Dealer(object):
    def __init__(self):
        self.deck = []
        self.players = []
        self.tableCards = []
        self.pot = 0

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


    def round(self):
        """
        Questions every player which option will be choosen
        :returns: TODO

        """
        for i in self.players:
            diff = i.options()
            if diff:
                self.players[self.players.index(i)+1].diff = diff 
        return self
         

            
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

    def clearCards(self):
        """
        Clear all played cards
        :returns: TODO

        """
        self.tableCards = []
        for index,player in enumerate(self.players):
            self.players[index].hand = []
        return self
  
    def cleanPlayers(self):
        for player in self.players:
            if player.money == 0:
                self.players.remove(player)
    
    
    def addPlayer(self,player):
        self.players.append(player)
        return self


    def createPlayers(self,name,numPlayers=2,money=500.0, difficulty="easy"):
        self.addPlayer(player.Player(name,money))
        for i in range(1,numPlayers+1):
            if difficulty == "easy":
               self.addPlayer(player.EasyBot())
               self.players[i].name +=str(i)
        return self



    """
    def createPlayers(self,name,numPlayers=2,money=500.0, difficulty="easy"):
        self.addPlayer(player.Player(name,money))
        for i in range(1,numPlayers+1):
            if difficulty == "easy":
               self.addPlayer(player.EasyBot())
               self.players[i].name +=str(i)
        return self
    """

    def calculateHandValues(self, players):
        """
        Creates a list of hand values of erverybody playing

        :players: TODO
        :returns: TODO

        """
        handValues = []
        for player in players:
            handValues.append(findHandValue(self.listCards(player)), self.players.index(player))
        return handValues

    def chooseWinner(self, players):
        """
        Decides who won the round
        :returns: TODO

        """
        handValues = self.calculateHandValues(players)
        #maxValue = max(handValues)
        handValues.sort(reverse = True)
        winningPlayers = self.players[0]
        #  Create ellegant and easy to understand function for adding players to the list with same values:  <08-08-19, dave> # 
        for index,value in enumerate(handValues):
            if value[0] == handValues[index+1][0]:
                winningPlayers.append(self.players[value[1]+1])
            else:
                return winningPlayers
        return winningPlayers
        """
        if handValues[index][0] == handValues[index+1][0]:
            winningPlayers.append(self.players[i])
        for value,index in handValues:
            if 
        for index,value in enumerate(handValues):
            if value == maxValue:
                
                winningPlayers.append(self.players[index])
                indexMaxValues.append(handValues.index(maxValue))
        return indexMaxValues
        """
    #lepsia
    def givePot(self,players):
        """
        Gives the pot to the winner(s)
        :returns: TODO

        """
        for i in players:
            money += self.pot/len(index)
        self.pot = 0.0
    
    def givePot(self,index):
        """
        Gives the pot to the winner(s)
        :returns: TODO

        """
        for i in index:
            self.players[i].money += self.pot/len(index)
