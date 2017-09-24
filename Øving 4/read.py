import re


class Read:

    def __init__(self):
        self.stop_words = []

        self.find_stop_words("/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 4/data/stop_words.txt")

    @staticmethod
    def find_stop_words_engrams(n):
        file = open("/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 4/data/stop_words.txt")
        stop_words = [x.strip().lower() for x in file.readlines()]
        stop_words_engrams = []

        for i in range(1 + len(stop_words) - n):
            for j in range(1 + len(stop_words) - n):
                stop_words_engrams.append(stop_words[i] + "_" + stop_words[j])

        return stop_words_engrams

    def find_stop_words(self, path):
        file = open(path)
        self.stop_words = [x.strip().lower() for x in file.readlines()]

        file.close()

    def read_file_default(self, path):

        file = open(path)
        line = file.read().replace("'", "").lower()
        rgx = re.compile("(\w[\w']*\w|\w)")
        words = [x for x in rgx.findall(line) if x not in self.stop_words]
        file.close()
        return words

    @staticmethod
    def read_file_engrams(path):
        file = open(path)
        line = file.read().replace("'", "").lower()
        rgx = re.compile("(\w[\w']*\w|\w)")
        words = [x for x in rgx.findall(line)]
        file.close()
        return words

