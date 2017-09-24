from read import Read
from os import listdir
from os.path import isfile, join
from collections import defaultdict
#import timeit


class Analyze:

    def __init__(self, percent=0.0183, n=1):

        #Frequency
        self.pos_word_freq = defaultdict(int)           #Dictionary with positive words and their frequency
        self.neg_word_freq = defaultdict(int)           #Dictionary with negative words and their frequency

        #Popularity
        self.pos_popularity = defaultdict(int)          #Positive words with their popularity
        self.neg_popularity = defaultdict(int)          #Negative words with their popularity
        self.pos_highest_pop = []                       #25 positive words with highest popularity
        self.neg_highest_pop = []                       #25 negative words with highest popularity

        #Information
        self.pos_information_value = defaultdict(int)   #Positive words with their information value
        self.neg_information_value = defaultdict(int)   #Negative words with their information value

        #Most Common
        self.pos_most_common = []                       #25 most common positive words
        self.neg_most_common = []                       #25 most common negative words

        #Other
        self.pos_docs = 0                               #All positive documents
        self.neg_docs = 0                               #All negative documents
        self.pos_all_words = []                         #All positive words with stopwords
        self.neg_all_words = []                         #All negative words with stopwords
        self.pos_words_total = 0                        #Total positive words
        self.neg_words_total = 0                        #Total negative words
        self.pos_doc_count = defaultdict(int)           #Postive - count of word mention in docs
        self.neg_doc_count = defaultdict(int)           #Negative - count of word mention in docs
        self.pos_percent = defaultdict(int)             #Positve - percent of how much word is used in pos doc
        self.neg_percent = defaultdict(int)             #Positve - percent of how much word is used in pos doc

        #N-grams
        self.pos_ngrams = []                            #Positive n-grams
        self.neg_ngrams = []                            #Negative n-grams
        self.pos_ngrams_freq = defaultdict(int)         #Positive n-grams frequency
        self.neg_ngrams_freq = defaultdict(int)         #Negative n-grams frequency

        path_pos, path_neg = self.choose_directory()    #Set paths for positive and negative documents

        #N-grams runtime-list
        if n > 1:
            pos_dic = self.pos_ngrams_freq
            neg_dic = self.neg_ngrams_freq

            self.find_all_words(path_pos, path_neg)
            self.make_ngrams(n)
            self.find_ngram_freq()
            self.prune(percent)
            self.find_most_common(pos_dic, neg_dic)

            self.find_popularity()
            self.find_information_value()
            self.find_highest_information_value()

        #Default runtime-list
        elif n == 1:
            #pos_dic = self.pos_word_freq
            #neg_dic = self.neg_word_freq
            self.find_freq(path_pos, path_neg)
            self.prune(percent)
            #self.find_most_common(pos_dic, neg_dic)
            self.find_popularity()
            #self.find_information_value()
            #self.find_highest_information_value()

        #print(self)
        print("Done reading " + str(self.pos_docs + self.neg_docs) + " documents")

    def find_freq(self, path_pos, path_neg):

        words_dir_train_pos = self.find_directories(path_pos)
        words_dir_train_neg = self.find_directories(path_neg)

        for directory in words_dir_train_pos:
            dir_path = path_pos + "/" + directory
            word_list = Read().read_file_default(dir_path)
            for word in word_list:
                self.pos_word_freq[word] += 1
                self.pos_words_total += 1

            self.pos_all_words.append(word_list)
            self.pos_docs += 1

        for directory in words_dir_train_neg:
            dir_path = path_neg + "/" + directory
            word_list = Read().read_file_default(dir_path)
            for word in word_list:
                self.neg_word_freq[word] += 1
                self.neg_words_total += 1

            self.neg_all_words.append(word_list)
            self.neg_docs += 1

    def prune(self, percent):

        for doc in self.pos_all_words:

            word_list_striped = list(set(doc))
            for word in word_list_striped:

                if word in self.pos_word_freq:
                    self.pos_doc_count[word] += 1


        temp_pos_count = defaultdict(int)
        for word in self.pos_doc_count:
            value = round(self.pos_doc_count.get(word)/self.pos_docs, 7)
            if value > percent:
                temp_pos_count[word] = self.pos_doc_count[word]

        #Negative
        for doc in self.neg_all_words:

            word_list_striped = list(set(doc))
            for word in word_list_striped:

                if word in self.neg_word_freq:
                    self.neg_doc_count[word] += 1

        temp_neg_count = defaultdict(int)
        for word in self.neg_doc_count:
            value = round(self.neg_doc_count.get(word)/self.neg_docs, 7)
            if value > percent:
                temp_neg_count[word] = self.neg_doc_count[word]

        self.pos_doc_count = temp_pos_count
        self.neg_doc_count = temp_neg_count

    def find_most_common(self, pos_dic, neg_dic):
        self.pos_most_common = sorted(pos_dic, key=pos_dic.get, reverse=True)[:25]
        self.neg_most_common = sorted(neg_dic, key=neg_dic.get, reverse=True)[:25]

    def find_popularity(self):
        for word in self.pos_doc_count:
            value = (self.pos_doc_count.get(word) / self.pos_docs) * 100
            self.pos_popularity[word] = round(value, 7)

        for word in self.neg_doc_count:
            value = (self.neg_doc_count.get(word) / self.neg_docs) * 100
            self.neg_popularity[word] = round(value, 7)

    def find_information_value(self):

        for word in self.pos_doc_count:
            self.pos_information_value[word] = round((self.pos_doc_count.get(word) / (self.pos_docs + self.neg_docs))
                                                     * 100, 2)

        for word in self.neg_doc_count:
            self.neg_information_value[word] = round((self.neg_doc_count.get(word) / (self.pos_docs + self.neg_docs))
                                                     * 100, 2)

    def find_highest_information_value(self):

        self.pos_highest_pop = sorted(self.pos_information_value, key=self.pos_information_value.get, reverse=True)[:25]
        self.neg_highest_pop = sorted(self.neg_information_value, key=self.neg_information_value.get, reverse=True)[:25]

    def find_ngram_freq(self):

        for ngram in self.pos_ngrams:
            self.pos_ngrams_freq[ngram] += 1
            self.pos_words_total += 1

        for ngram in self.neg_ngrams:
            self.neg_ngrams_freq[ngram] += 1
            self.neg_words_total += 1


    def make_ngrams(self, n):

        stop_word_ngrams = Read().find_stop_words_engrams(n)
        for doc_words in self.pos_all_words:
            for i in range(1 + len(doc_words) - n):
                ngram = "_".join(doc_words[i:i+n])
                #if ngram not in stop_word_ngrams:
                #   self.pos_ngrams.append(ngram)
                self.pos_ngrams.append(ngram)

        for doc_words in self.neg_all_words:
            for i in range(1 + len(doc_words) - n):
                ngram = "_".join(doc_words[i:i+n])
                #if ngram not in stop_word_ngrams:
                #   self.neg_ngrams.append(ngram)
                self.neg_ngrams.append(ngram)

    @staticmethod
    def choose_directory():

        print("Which train-directory do you want? 'All' or 'Subset'")
        directory = input(">>> ").lower()
        path_pos = "/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 4/data/"
        path_neg = "/Users/tsm121_MB/Dropbox/NTNU/2.klasse/ProgLab2/Øving 4/data/"

        if directory == "subset":
            path_pos += "subset/train/pos"
            path_neg += "subset/train/neg"

        elif directory == "all":
            path_pos += "alle/train/pos"
            path_neg += "alle/train/neg"

        return path_pos, path_neg

    @staticmethod
    def find_directories(filepath):

        return [f for f in listdir(filepath) if isfile(join(filepath, f))]

    def find_all_words(self, path_pos, path_neg):

        words_dir_train_pos = self.find_directories(path_pos)
        words_dir_train_neg = self.find_directories(path_neg)

        for directory in words_dir_train_pos:
            dir_path = path_pos + "/" + directory
            self.pos_all_words.append(Read().read_file_engrams(dir_path))

        for directory in words_dir_train_neg:
            dir_path = path_neg + "/" + directory
            self.neg_all_words.append(Read().read_file_engrams(dir_path))

    def test(self):
        self.find_most_common(self.pos_doc_count, self.neg_doc_count)
        print(self.pos_most_common)
        print(self.neg_most_common)


    def __str__(self):
        print("-" * 140)
        print("Word frequency")
        if len(self.pos_ngrams) > 0:
            print("P ", self.pos_ngrams)
            print("N ", self.neg_ngrams)
        else:
            print("P ", self.pos_word_freq)
            print("N ", self.neg_word_freq)
        print("-" * 140)
        print("25 most common")
        print("P ", self.pos_most_common)
        print("N ", self.neg_most_common)
        print("-" * 140)
        print("Word popularity")
        print("P ", self.pos_popularity)
        print("N ", self.neg_popularity)
        print("-" * 140)
        print("Information value")
        print("P ", self.pos_information_value)
        print("N ", self.neg_information_value)
        print("-" * 140)
        print("25 highest information value")
        print("P ", self.pos_highest_pop)
        print("N ", self.neg_highest_pop)
        print("-" * 140)

        return "\n"


#t0 = timeit.default_timer()

#x = Analyze(0.0175, 2)
#print(x)
#x = Analyze(0.0175)
#x.test()

#t1 = timeit.default_timer()
#print("Time:" + str((t1-t0)))
#print(x)
