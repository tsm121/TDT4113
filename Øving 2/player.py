import random
from action import Action

actions = ['rock','scissor','paper']

class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.actionController = Action()

    def choose_action(self,other):

        while(True):
            try:
                choice = int(input("What do you want to play?\nRock = 1, Scissor = 2, Paper = 1\n>>> "))
                if choice in [1, 2, 3]:
                    break
                else:
                    print("Wrong input. Press 1,2 or 3.\n")
            except:
                print("Wrong input. Press 1,2 or 3.\n")
        self.actionController.play(actions[choice-1])
        return actions[choice-1]

    def receive_results(self,point):
        self.points += point
        return 'Player ' + self.name + ' has ' + str(self.points) + 'points'

    def set_name(self, name):
        self.name = name

    def get_action(self):
        return self.actionController

    def get_name(self):
        return self.name