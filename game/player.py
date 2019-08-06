"""
File:player.py
Author:dave
Github:https://github.com/davidus27
Description:Player and variations of bots.
"""
from random import random, randint
from printouts import optionsInput, raising
from sys import exit
from os import system

class Player(object):
    def __init__(self, name = "Player", money = 500.0):
        self.name = name
        self.money = money
        self.hand = []
        self.deposit = 0.0 #how much money player spend in one game
        self.bet = 0.0 #how much money one player need to get to the game to play
        #if bet - deposit == check

    def clearDebt(self):
        """
        Clears deposit and bet on each game
        :returns: TODO

        """
        self.bet = 0.0
        self.deposit = 0.0
        return self

    def callBet(self):
        """
        Action for player to call a bet on table

        :returns: deposit

        """
        debt = self.bet - self.deposit
        if not debt - self.deposit:
            return self.checkBet()
     
        elif debt >= self.money:
            return self.allin()
    
        elif debt < self.money:
           self.money -= self.bet - self.deposit
           debt = self.bet - self.deposit
           self.deposit = self.bet
           print("{} call".format(self.name))
           return (self.bet,debt)

    def raising(self):
        """
        Function for getting input
        :returns: TODO

        """
        debt = self.bet - self.deposit
        return raising(1, self.money-debt)


    def raiseBet(self):
       """
       Method for raising bets
       :returns: bet
       """
       while True:
            debt = self.bet - self.deposit
            raised = self.raising()
            if raised == 0.0:
                return self.callBet()
            
            elif raised >= self.money-debt:
                return self.allin()
            
            else:
                self.money -= raised + self.bet
                bet = self.bet
                self.bet += raised
                self.deposit = self.bet
                print("{} raised bet:{} ".format(self.name,raised))
                return (self.bet,bet + raised)

    def checkBet(self):
        """
        Checks only if difference between deposit and bet is zero
        
        :returns: True/False based on if you can check or not
        """
        if self.bet - self.deposit:
            print("Cannot perform check.", self.name)
            return False
        else:
            print("{} check".format(self.name))
            return (self.bet,0)

    def foldBet(self):
       """
       :returns: self

       """
       print("{} fold.".format(self.name))
       return (self.bet,-1)

    def allin(self):
       """
       Gives all money to the pot

       :currentBet: Money on pot
       :returns: currentBet with all player's money

       """
       #currentBet += self.money
       print("{} all in!".format(self.name))
       self.deposit += self.money
       self.bet = -1
       self.money = 0
       return -1

    def quit(self):
        print("Exiting program. Hope you will come back again.")
        exit()
    
    def options(self):
        """
        Gives all options to the player
        :action: input of the player
        :returns: used function

        """
        options = { 0: self.quit,
                    1: self.checkBet ,
                    2: self.callBet , 
                    3: self.raiseBet , 
                    4: self.foldBet , 
                    5: self.allin,
                    }
        while True:
            action = optionsInput()
            choosed = options[action]()
            if self.bet == -1:
                print("You can only go allin or fold.")
                if action == 4 or action == 5:
                    return choosed
                else:
                    print("Incorrect")
            else:
                if choosed is not False:
                    return choosed
                else:
                    continue

class EasyBot(Player):

    """
    Easy to compete player
    Selects randomly between his options
    """

    def __init__(self):
       """TODO: to be defined1. """
       Player.__init__(self)

    def raising(self):
        """
        Function for getting random input
        :returns: TODO

        """
        debt = self.bet - self.deposit
        return randint(1, self.money - debt) 

    def options(self):
        """
        Gives all options to the player
        :action: input of the player
        :returns: used function

        """
        options = {1: self.checkBet ,
                    2: self.callBet , 
                    3: self.raiseBet , 
                    4: self.foldBet , 
                    5: self.allin,
                    }
        while True:
            x = random()
            if self.bet == -1:
                if x <= 0.5:
                    action = 4
                else:
                    action = 5
            else:
                #if x <= 0.005:
                #    action = 4

                if x <= 0.45:
                    action = 1

                elif x <= 0.85:
                    action = 2

                elif x <= 0.995:
                    action = 3

                #elif x <= 1.0:
                #    action = 5
            
            choosen = options[action]()
            if choosen is not False:
                return choosen
            else:
                continue

