#from randomPlayer import RandomPlayer
#from sequentialPlayer import SequentialPlayer
#from mostCommonPlayer import MostCommonPlayer
#from historianPlayer import HistorianPlayer
#from player import Player

import matplotlib.pyplot as plt
import numpy as npy

class SimpleGame:

    def __init__(self, player1, player2):


        self.player1 = player1
        self.player2 = player2
        self.p1Points,self.p2Points = [],[]
        self.roundsPlayed = 0

        self.roundWinner = self.play_game(self.player1,self.player2)

    def play_game(self, player1, player2):


        self.p1_choice = player1.choose_action(player2)
        self.p2_choice = player2.choose_action(player1)
        self.roundsPlayed += 1

        if player1.get_action() == player2.get_action():
            player1.receive_results(0.5)
            player2.receive_results(0.5)
            self.p1Points.append(player1.points+ 0.5)
            self.p2Points.append(player2.points + 0.5)
            return 'draw'

        elif player1.get_action() > player2.get_action():
            player1.receive_results(1)
            self.p1Points.append(player1.points + 1)
            self.p2Points.append(player2.points)
            return 'player1'

        else:
            player2.receive_results(1)
            self.p2Points.append(player2.points + 1)
            self.p1Points.append(player1.points)
            return 'player2'

    def plot(self):
        figur = plt.figure()
        x = npy.arange(self.roundsPlayed)
        plt.plot(x,self.p1Points,"b-")
        plt.plot(x,self.p2Points,"r-")

        plt.xlabel("Rounds")
        plt.ylabel("Points")

        plt.legend([self.player1.get_name() + ' = ' + self.player1.__class__.__name__,
                    self.player2.get_name() + ' = ' + self.player2.__class__.__name__],
                   loc='upper left')

        plt.show()

    def __str__(self):

        if self.roundWinner == 'draw':
            return('The round was a draw. Both players choose ' + self.p1_choice
                  + ' and got 0.5 points each.\nPlayer ' + self.player1.name + ' has ' + str(self.player1.points)
                   + ' and ' + self.player2.name + ' has ' + str(self.player2.points))

        elif self.roundWinner == 'player1':
            return(self.player1.name + ' won with ' + self.p1_choice + ' over '
                  + self.player2.name + ' who chose ' + self.p2_choice + '. '
                  + self.player1.name + ' got 1 point for winning\nPlayer ' + self.player1.name
                   + ' has ' + str(self.player1.points)
                   + ' and ' + self.player2.name + ' has ' + str(self.player2.points))

        else:
            return(self.player2.name + ' won with ' + self.p2_choice + ' over '
                  + self.player1.name + ' who chose ' + self.p1_choice + '. '
                  + self.player2.name + ' got 1 point for winning\nPlayer ' + self.player1.name
                   + ' has ' + str(self.player1.points)
                   + ' and ' + self.player2.name + ' has ' + str(self.player2.points))


#x = RandomPlayer("John")
#y = HistorianPlayer("Sally",2)
#game = SimpleGame(x, y)


#for a in range (500):
    #game.play_game(x,y)
    #print(game)
    #print("\nP1 ",x.get_action().gameHistory)
    #print("P2 ", y.get_action().gameHistory)

#game.plot()


