from analyze import Analyze
from read import Read
from collections import defaultdict
from math import log10


class Classifier(Analyze):

    def __init__(self, percent):
        super().__init__(percent)

        self.word_freq = defaultdict(int)
        self.word_list = []
        self.document_dic = defaultdict(int)

    def read_document(self, path):
        self.word_list = Read().read_file_default(path)

    def analyze_document(self):
        pos_value = 0
        neg_value = 0
        for word in set(self.word_list):
            if word in self.pos_popularity:
                pos_value += log10(self.pos_popularity[word])

            if word in self.neg_popularity:
                neg_value += log10(self.neg_popularity[word])

        if pos_value > neg_value:
            return 1    #Analysed as positive
        elif pos_value < neg_value:
            return 0    #Analysed as negative
        else:
            return -1   #NA

    def check_document(self, path):
        formated_path, org_value = self.format_path(path)
        #print("Checking doc: " + "'" + formated_path + "'")

        self.read_document(path)
        doc_value = self.analyze_document()
        self.document_dic[formated_path] = (doc_value, org_value)

        #if doc_value == 1:
        #    print("Document was 'positive'\n")
        #elif doc_value == 0:
        #    print("Document was 'negative'\n")
        #else:
        #    print("Could not evaluate document\n")
    @staticmethod
    def format_path(path):

        formated_path = path.split("/")
        org_value = -1
        if formated_path[-2] == "pos":
            org_value = 1
        elif formated_path[-2] == "neg":
            org_value = 0
        return formated_path[-1], org_value

#x = Classifier()
#x.check_document("/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 4/data/subset/test/pos/1_10.txt")
