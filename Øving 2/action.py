class Action():

    def __init__(self):
        self.lastChoice = ''
        self.gameHistory = []

    def play(self, action):
        self.gameHistory.append(action)
        self.lastChoice = self.gameHistory[-1]

    def __eq__(self, other):
        if self.lastChoice == other.lastChoice:
            return True

        return False

    def __gt__(self, other):

        if self.lastChoice == 'rock' and other.lastChoice == 'scissor':
            return True

        elif self.lastChoice == 'scissor' and other.lastChoice == 'paper':
            return True

        elif self.lastChoice == 'paper' and other.lastChoice == 'rock':
            return True

        return False