from cipher import Cipher
import random


class Caesar(Cipher):

    def __init__(self):
        
        super(Caesar, self).__init__()

    def generate_keys(self):

        return random.randint(1, 95)

    def encode(self, msg, key):

        encoded = ''

        for letter in msg:

            char_num = ((ord(letter) + key - 32) % 95)
            encoded += Cipher.dictionary[char_num]

        return encoded

    def decode(self, msg, key):

        decoded = ''

        for letter in msg:

            char_num = ((ord(letter) - key - 32) % 95)
            decoded += Cipher.dictionary[char_num]

        return decoded

    def __str__(self):
        return "Caesar Cipher"


'''
x = Caesar()

key = x.generate_keys()
en = x.encode("Python", key)
de = x.decode(en, key)

print("Encoded: " + en)
print("Decoded: " + x.decode(en, key))
print(key)

print(x.verify("Python", de))
'''