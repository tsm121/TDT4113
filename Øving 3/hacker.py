from person import Person
from cipher import Cipher
from crypto_utils import modular_inverse

from caesar import Caesar
from multiplicative_cipher import Multiplicative
from affine_cipher import Affine
from unbreakable_cipher import Unbreakable


class Hacker(Person):
    def __init__(self):
        super(Person, self).__init__()
        self.dictionary = []

    def hack(self, encrypted_msg, cipher):
        self.set_cipher(cipher)

        self.set_encoded_msg(encrypted_msg)

        if isinstance(cipher, Caesar):
            print("Hacker found a " + str(cipher))
            self.crack_caesar(encrypted_msg)

        elif isinstance(cipher, Multiplicative):
            print("Hacker found a " + str(cipher))
            self.crack_multiplicative(encrypted_msg)

        elif isinstance(cipher, Affine):
            print("Hacker found a " + str(cipher))
            self.crack_affine(encrypted_msg)

        elif isinstance(cipher, Unbreakable):
            print("Hacker found an " + str(cipher))
            self.break_unbreakable(encrypted_msg)

        else:
            pass

    def crack_caesar(self, msg):

        temp_decode = ''

        for key in range(len(Cipher.dictionary)):

            if key > 95:
                print("Could not hack...")
                return ""

            for letter in msg:

                char_num = (ord(letter) - key - 32) % 95
                temp_decode += Cipher.dictionary[char_num]

            corr_words = 0
            for words in temp_decode.split():

                print("Checking '" + words + "' Key used: " + str(key))
                if self.check_word(words.lower()):
                    corr_words += 1
                    if corr_words == len(temp_decode.split()):
                        return temp_decode, key

            temp_decode = ''

    def crack_multiplicative(self, msg):

        temp_decode = ''

        for key in range(len(Cipher.dictionary)):

            if key > 999:
                print("Could not hack...")
                return ""

            m = modular_inverse(key, 95)

            for letter in msg:
                char_num = ((ord(letter) * m) - 32) % 95
                temp_decode += Cipher.dictionary[char_num]

            corr_words = 0
            for words in temp_decode.split():

                print("Checking '" + words + "' Key used: " + str(key))
                if self.check_word(words.lower()):
                    corr_words += 1
                    if corr_words == len(temp_decode.split()):
                        return temp_decode, key

            temp_decode = ''

    def crack_affine(self, msg):

        temp_decode = ''

        for multi_key in range(len(Cipher.dictionary)):

            for key in range(len(Cipher.dictionary)):

                if key > 95:
                    print("Could not hack...")
                    return ""

                m = modular_inverse(multi_key, 95)

                for letter in msg:
                    char_num = ((((ord(letter) - key) * m) - 32) % 95)
                    temp_decode += Cipher.dictionary[char_num]

                corr_words = 0
                for words in temp_decode.split():

                    print("Checking '" + words + "' Mod Key used: " + str(multi_key) + ", Caesar Key used: " + str(key))
                    if self.check_word(words.lower()):
                        corr_words += 1
                        if corr_words == len(temp_decode.split()):
                            return temp_decode, key

                temp_decode = ''

    def break_unbreakable(self, msg):

        for key in self.dictionary:

            temp_decode = ''
            dec_word = ''

            #Encode key_word
            for x in range(len(key)):
                key_word_num = (95 - (ord(key[x]) - 32)) % 95
                dec_word += Cipher.dictionary[key_word_num]

            #make key_word longer
            dec_word_mod = self.mod_key_length(len(msg), dec_word)

            #adding key_word value
            for i in range(len(msg)):
                char_num = ((ord(msg[i]) - 32) + (ord(dec_word_mod[i]) - 32)) % 95
                temp_decode += Cipher.dictionary[char_num]

            corr_words = 0
            for words in temp_decode.split():

                print("Checking '" + words + ", Keyword used: " + key)
                if self.check_word(words.lower()):
                    corr_words += 1
                    if corr_words == len(temp_decode.split()):
                        return temp_decode, key

    def check_word(self, word):

        for x in self.dictionary:

            if x == word:
                print("CRACKED!")
                return True
        return False

    def read_dic(self, file_path='english_words.txt'):

        file = open(file_path)

        temp_list = []
        for line in file.readlines():
            temp_list.append(line.split())

        file.close()

        dic_list = []
        for i in range(len(temp_list) - 1):
            dic_list.append(temp_list[i][0])

        self.dictionary = dic_list

    def mod_key_length(self, length, key):

        key_word_mod = ''
        for x in range(length):

            j = x % (len(key))
            key_word_mod += key[j]

        return key_word_mod

"""
x = Hacker()
x.read_dic()
y = Unbreakable()
key = y.generate_keys()
print(key)
en = y.encode("hello", key)
print(x.break_unbreakable(en))
"""

"""
x = Hacker()
x.read_dic()
y = Affine()
key = y.generate_keys()
print(key)
en = y.encode("How are you", key)
print(x.crack_affine(en))
"""

"""
x = Hacker()
x.read_dic()
y = Multiplicative()
key = y.generate_keys()
print(key)
en = y.encode("hello this is patrick", key)
print(x.crack_multiplicative(en))
"""

"""
x = Hacker()
x.read_dic()
y = Caesar()
en = y.encode("test", 5)
print(x.crack_caesar(en))
"""

