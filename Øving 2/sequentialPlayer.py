import random
from action import Action

actions = ['rock','scissor','paper']

class SequentialPlayer:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.actionController = Action()
        self.index = 0

    def choose_action(self,other):

        if (self.get_lastAction() == 'paper'):
            self.index = 0

        else:
            self.index += 1

        tempAction = actions[self.index]
        self.actionController.play(tempAction)
        return tempAction


    def receive_results(self,point):
        self.points += point
        return 'Player ' + self.name + ' has ' + str(self.points) + 'points'

    def set_name(self, name):
        self.name = name

    def get_action(self):
        return self.actionController

    def get_lastAction(self):
        return self.actionController.lastChoice

    def get_name(self):
        return self.name