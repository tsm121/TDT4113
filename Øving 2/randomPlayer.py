import random
from action import Action

actions = ['rock','scissor','paper']

class RandomPlayer:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.actionController = Action()

    def choose_action(self,other):
        choice = actions[random.randint(0, 2)]
        self.actionController.play(choice)
        return choice

    def receive_results(self,point):
        self.points += point
        return 'Player ' + self.name + ' has ' + str(self.points) + 'points'

    def set_name(self, name):
        self.name = name

    def get_action(self):
        return self.actionController

    def get_name(self):
        return self.name
