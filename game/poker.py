"""
File: poker.py
Author: dave
Github: https://github.com/davidus27
Description: Game is the main Object implementing all the necessary tools for playing. Game is created in function main()
                        RUNS THE WHOLE PROGRAM!
"""
import dealer
import printouts
import detector
import os
class Game(object):
    """
    Creates players based on inputs on call.
    """
    def __init__(self):
        self.rounds = 1
        self.players = []
        self.dealer = dealer.Dealer()



    def createPlayers(self):
        self.dealer.createPlayers(name = printouts.nameQuest(),
                                  numPlayers = printouts.numQuest(),
                                  money = 500,
                                  difficulty = printouts.diffQuest()
                                  )
        return self

    def giveCards(self):
        """
        gives cards.
        :returns: TODO

        """
        self.dealer.dealCard()
        self.dealer.dealCard()

    def question(self):
        """
        Questions every player which option will be choosen
        :returns: TODO

        """
        for i in self.players:
            i.options()
        return self
 
    def gameOn(self):
        """
        Clears all the cards, create cards and shuffles them
        :returns: TODO

        """
        self.dealer.clearCards()
        self.dealer.buildDeck()
        self.dealer.shuffle()
        return self

    def controlDeposit(self):
        """
        checks if there are any differences
        :arg1: TODO
        :returns: TODO

        """
        deposit = self.players[0].deposit #reference
        for player in self.players:
            if player.deposit == deposit:
                continue
            else:
                return False
        return True

    def round(self):
        """
        Goes through all players until every player gave same ammount to the pot
        :returns: TODO

        """
        while True:
            for index,player in enumerate(self.players):
                #prev_depo = player.deposit
                bet = player.options()
                x = (index + 1) % len(self.players)
                
                if bet == -1:
                    pass 
                    #Allin
                else:
                    if bet[1] == -1:
                        #fold
                        self.players.remove(player)
                    else:
                        self.players[x].bet = bet[0]
                        self.dealer.pot += bet[1]
                print("Bet:{}\nDeposit:{}".format(player.bet,player.deposit))
                print("Pot:", self.dealer.pot)
            if self.controlDeposit():
                break
            else:
                continue
        return self
        """"
                if type(bet) == tuple:
                    self.players.remove(player)
                    bet = bet[1]
                elif bet:
                    self.players[x].bet = bet
                print("Pot before:", self.dealer.pot) 
                self.dealer.pot += bet - prev_depo
                print("Bet:{}\nDeposit:{}".format(player.bet,player.deposit))
                print("Pot:", self.dealer.pot)
            print(self.controlDeposit())
            if self.controlDeposit():
                break
            else:
                continue
        return self
        """

        """
        while True:
            for index,player in enumerate(self.players):
                prev_depo = player.deposit
                bet = player.options()
                x = (index + 1) % len(self.players)
                
                if type(bet) == tuple:
                    self.players.remove(player)
                    bet = bet[1]
                elif bet:
                    self.players[x].bet = bet
                print("Pot before:", self.dealer.pot) 
                self.dealer.pot += bet - prev_depo
                print("Bet:{}\nDeposit:{}".format(player.bet,player.deposit))
                print("Pot:", self.dealer.pot)
            print(self.controlDeposit())
            if self.controlDeposit():
                break
            else:
                continue
        return self
        """

    def printSituation(self, table=False):
        """
        Prints out whole situation in the game.
        :returns: TODO

        """
        printouts.info(self.dealer.players[0].name, self.dealer.players[0].money)
        print("Your cards:")
        printouts.cards(self.dealer.players[0].hand)
        print()
        if table:
            print("Community cards:")
            printouts.cards(table)
            print()
   
    def showdown(self):
        """
        Ending of the round
        :returns: TODO

        """
        for player in self.players:
            print(player.name)
            printouts.cards(player.hand)

        winners = self.dealer.chooseWinner()
        self.dealer.givePot(winners)
        printouts.roundWinners(winners)
        input("Press Enter to continue.")
        return self

    def cardOnTable(self, phase):
        """
        Three cards on table while flop
        :returns: TODO

        """
        if phase == "Preflop":
            self.dealer.drawTable()
            self.dealer.drawTable()
            self.dealer.drawTable()
        elif phase == "River":
            pass
        else:
            self.dealer.drawTable()

    def oneRound(self, phase):
        """
        Creates flop part of easy game
        :returns: TODO

        """
        print("\n\t\t{}\n".format(phase))
        self.printSituation(self.dealer.tableCards)
        self.round()
        self.cardOnTable(phase)

def main():
    """ 
    Work to create game
    """
    game = Game()
    print("Let's play Texas Hold'em!\n")
    #game.askQuestions()
    game.createPlayers()
    while True:
        #The simple game functioning:
        #Players bets on preflop (before the release of firt three cards)
        #First three cards are released
        #Another beting
        #Turn-fourth card release
        #Another bets
        #River-final card
        #Last beting
        #Showdown-cards are showed (if any players are left)
        game.gameOn()
        game.giveCards()
        #  deleting players that loose:  <29-07-19, dave> # 
        game.players = game.dealer.players
        print("\n\t\tRound", game.rounds)

        #Preflop
        phase = "Preflop"
        game.oneRound(phase)
        
        #Flop
        phase = "Flop"
        game.oneRound(phase)
        
        #Turn
        phase = "Turn"
        game.oneRound(phase)

        #River
        phase = "River"
        game.oneRound(phase)
        
        #Showdown
        print("\n\t\tShowdown\n")
        game.showdown()

        game.rounds += 1
        if len(game.dealer.players) == 1:
            break
        
        #print(game.dealer.chooseWinner())



if __name__ == "__main__":
    main()

