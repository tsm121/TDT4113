from randomPlayer import RandomPlayer
from sequentialPlayer import SequentialPlayer
from mostCommonPlayer import MostCommonPlayer
from historianPlayer import HistorianPlayer
from player import Player
import sys

from simpleGame import SimpleGame

class ManyGames:

    def __init__(self):

        self.numGames = 10
        self.arrangeSingleMatch()
        self.player1 = None
        self.player2 = None
        self.game = None


    def arrangeSingleMatch(self):


        while (True):
            try:
                mode = int(input("Press 1 for you vs comp. Press 2 for comp vs comp\n>>> "))
                if mode in [1, 2]:
                    break
                else:
                    print("Wrong input. Press 1,2,3 or 4.\n")
            except:
                print("Wrong input. Press 1 or 2.\n")

        self.setRounds()

        if mode == 1:

            self.player1 = Player(input("What is your name? \n>>> "))
            self.player2 = self.opponent()
            self.game = SimpleGame(self.player1,self.player2)

            while (self.numGames > 0):
                self.roundWinner = self.game.play_game(self.player1, self.player2)
                print(self.game)
                print("\n")
                self.numGames -= 1

            if self.player1.points > self.player2.points:
                print("The match is over. " + self.player1.name + " won with " + str(self.player1.points) + " over "
                      + self.player2.name + " with " +str(self.player2.points) + " points." )

            elif self.player2.points > self.player1.points:
                print("The match is over. " + self.player2.name + " won with " + str(self.player2.points) + " over "
                      + self.player1.name + " with " + str(self.player1.points) + " points.")

            else:
                print("The match was a draw. Both with " + str(self.player1.points) + " points.")

        if mode == 2:

            self.player1 = self.opponent()
            self.player2 = self.opponent()
            if type(self.player1) == type(self.player2):
                self.player1.set_name(self.player1.name + "1")
                self.player2.set_name(self.player2.name + "2")

            self.game = SimpleGame(self.player1, self.player2)

            while (self.numGames > 0):
                self.roundWinner = self.game.play_game(self.player1, self.player2)
                print(self.game)
                print("\n")
                self.numGames -= 1

            if self.player1.points > self.player2.points:
                print("The match is over. '" + self.player1.name + "' won with " + str(self.player1.points) + " over '"
                      + self.player2.name + "' with " + str(self.player2.points) + " points.")

            elif self.player2.points > self.player1.points:
                print("The match is over. '" + self.player2.name + "' won with " + str(self.player2.points) + " over '"
                      + self.player1.name + "' with " + str(self.player1.points) + " points.")

            else:
                print("The match was a draw. Both with " + str(self.player1.points) + " points.")
        total = self.player1.points + self.player2.points
        player1Percent = (self.player1.points/total) * 100
        player2Percent = (self.player2.points/total) * 100

        print(self.player1.name + " won " + str(player1Percent) + "% of the time, and " + self.player2.name + " won " + str(player2Percent) + "%.\n")

        print("\nClose plot to play more.\n")
        self.game.plot()

        x = str.lower(input("Do you want to play again? YES/NO\n>>> "))
        if x == "yes":
            self.arrangeSingleMatch()
        else:
            sys.exit("Thanks for playing!")


    def opponent(self):
        while (True):
            try:
                comp = int(input(
                    "Choose opponent: Random Player = 1, Sequential Player = 2, Most Common Player = 3,"
                    " Historian Player = 4\n>>> "))
                if comp == 1:
                    return RandomPlayer("CompRandom")
                elif comp == 2:
                    return SequentialPlayer("CompSequential")
                elif comp == 3:
                    return MostCommonPlayer("CompMostCommon")
                elif comp == 4:
                    return HistorianPlayer("CompHistorian")
                else:
                    print("Wrong input. Press 1,2,3 or 4.\n")
            except:
                print("Wrong input. Press 1,2,3 or 4.\n")

    def setRounds(self):
        while (True):
            try:
                rounds = int(input("How many rounds do you want to play?\n>>> "))
                if rounds < 9999:
                    break
                else:
                    print("Wrong input. Write a number.\n")
            except:
                print("Wrong input. Write a number.\n")

        self.numGames = rounds-1



ManyGames()