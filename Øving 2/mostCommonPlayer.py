import random
from action import Action

actions = ['rock','scissor','paper']

class MostCommonPlayer:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.actionController = Action()

    def choose_action(self,other):

        mostCommonChoice = self.mostCommon(other)

        if mostCommonChoice == "":
            choice = actions[random.randint(0, 2)]
            self.actionController.play(choice)
            return choice

        elif mostCommonChoice == "rock":
            self.actionController.play("paper")
            return "paper"

        elif mostCommonChoice == "scissor":
            self.actionController.play("rock")
            return "rock"

        else:
            self.actionController.play("scissor")
            return "scissor"

    def receive_results(self,point):
        self.points += point
        return 'Player ' + self.name + ' has ' + str(self.points) + 'points'

    def set_name(self, name):
        self.name = name

    def get_action(self):
        return self.actionController

    def mostCommon(self,other):
        tempS,tempR,tempP = 0,0,0

        for x in other.get_action().gameHistory:
            if x == "rock":
                tempR += 1
            elif x == "scissor":
                tempS += 1
            else:
                tempP += 1

        if tempS == tempR and tempS == tempP:
            return ""
        elif tempS > tempR and tempS > tempP:
            return "scissor"
        elif tempR > tempS and tempR > tempP:
            return "rock"
        else:
            return "paper"

    def get_name(self):
        return self.name
