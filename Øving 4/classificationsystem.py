from classifier import Classifier
from os import listdir
from os.path import isfile, join
from timeit import default_timer


class ClassificationSystem:

    def __init__(self):
        print("Write path to folder you want to check")
        path = input(">>> ")
        print("What is your prune-percentage")
        percent = input(">>> ")
        percent = float(percent)/100
        t0 = default_timer()
        self.classifier = Classifier(percent)

        #1.175 -> 84.35

        pos_doc_list, neg_doc_list = self.find_directories(path)

        for path_pos in pos_doc_list:
            self.classifier.check_document(path_pos)

        for path_neg in neg_doc_list:
            self.classifier.check_document(path_neg)

        print("Done analyzing " + str(len(pos_doc_list) + len(neg_doc_list)) + " documents")
        self.analyse_value()
        t1 = default_timer()
        print("Total runtime: " + str(round(t1-t0, 2)) + " sec")

    @staticmethod
    def find_directories(filepath):

        pos_path = filepath + "/pos/"
        neg_path = filepath + "/neg/"
        return [pos_path + f for f in listdir(pos_path) if isfile(join(pos_path, f))],\
               [neg_path + f for f in listdir(neg_path) if isfile(join(neg_path, f))]

    def analyse_value(self):
        pos = 0
        neg = 0
        wrong = 0
        for doc in self.classifier.document_dic:
            if self.classifier.document_dic[doc] == (1, 1):
                pos += 1
            elif self.classifier.document_dic[doc] == (0, 0):
                neg += 1
            else:
                wrong += 1

        print("\nTotal correct analysed documents", pos + neg)
        print("Total wrong analysed documents", wrong)
        print("Percentage correct: " + str(round((((pos + neg) / (pos + neg + wrong)) * 100), 2)))

x = ClassificationSystem()
