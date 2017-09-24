import random
from action import Action

actions = ['rock','scissor','paper']


class HistorianPlayer:

    def __init__(self, name, historyTime = 2):
        self.name = name
        self.points = 0
        self.actionController = Action()
        self.remember = historyTime

    def choose_action(self,other):

        choice = self.history_choice(other)

        if choice == "":
            choice = actions[random.randint(0, 2)]
            self.actionController.play(choice)
            return choice

        elif choice == "rock":
            self.actionController.play("paper")
            return "paper"

        elif choice == "scissor":
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

    #def get_compHistory(self,other):
        #return other.get_action().gameHistory

    def history_choice(self,other):
        compHistory = other.get_action().gameHistory


        if (len(compHistory) <= self.remember):
            return ""

        startSeq = len(compHistory)-self.remember
        seq = []
        seqChoices = []

        for x in compHistory[startSeq:]:
            seq.append(x)
        for y in range(startSeq):

            if compHistory[y] == seq[0]:
                index1 = y + 1 #start
                index2 = y+self.remember #stop
                seqIndex = 1
                corrChar = 1

                while(index1 < index2):
                    if compHistory[index1] !=  seq[seqIndex]:
                        break
                    else:
                        corrChar +=1
                    index1 += 1
                    seqIndex += 1

                if corrChar == self.remember:
                    seqChoices.append(compHistory[index2])

        return self.mostCommon(seqChoices)

    def mostCommon(self,actions):
        tempS,tempR,tempP = 0,0,0

        for x in actions:
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



