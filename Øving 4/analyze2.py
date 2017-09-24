from read import Read
from os import listdir
from os.path import isfile, join
from collections import defaultdict
import timeit

class Analyze2:

    def __init__(self, n):

        self.pos_freq = defaultdict(int)
        self.neg_freq = defaultdict(int)
        self.pos_words_total = 0
        self.neg_words_total = 0
        self.pos_docs = 0
        self.neg_docs = 0


        path_pos = "/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 4/data/subset/train/pos"
        path_neg = "/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 4/data/subset/train/neg"
        self.find_freq(path_pos, path_neg)

        print(self.pos_freq)

        print("Done")


    def find_freq(self, path_pos, path_neg):

        words_dir_train_pos = self.find_directories(path_pos)
        words_dir_train_neg = self.find_directories(path_neg)
        pos_words = defaultdict(int)
        neg_words = defaultdict(int)

        for directory in words_dir_train_pos:
            dir_path = path_pos + "/" + directory
            word_list = Read().read_file_default(dir_path)
            for word in word_list:
                pos_words[word] += 1
                self.pos_words_total += 1

            self.pos_docs += 1

        for directory in words_dir_train_neg:
            dir_path = path_neg + "/" + directory
            word_list = Read().read_file_default(dir_path)
            for word in word_list:
                neg_words[word] += 1
                self.neg_words_total += 1
            self.neg_docs += 1

        self.pos_freq = pos_words
        self.neg_freq = neg_words

        temp = 9999
        word = ""
        for x in pos_words:
            if pos_words.get(x) < temp:
                temp = pos_words.get(x)
                word = x
        print(word,temp)

    def find_directories(self, filepath):
        dir_files = [f for f in listdir(filepath) if isfile(join(filepath, f))]
        return dir_files

x = Analyze2(2)
