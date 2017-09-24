from cipher import Cipher
import random
import crypto_utils


class Multiplicative(Cipher):
    def __init__(self):

        super(Multiplicative, self).__init__()

    def generate_keys(self):

        n = random.randint(1, 99)

        while True:

            if not crypto_utils.modular_inverse(n, 95):
                print("Making new key...\n")
                n = random.randint(1, 99)

            else:
                return n

    def encode(self, msg, key):

        encoded = ''

        for letter in msg:
            char_num = ((ord(letter) * key - 32) % 95)
            encoded += Cipher.dictionary[char_num]

        return encoded

    def decode(self, msg, key):

        decoded = ''
        m = crypto_utils.modular_inverse(key, 95)

        for letter in msg:
            char_num = (((ord(letter) * m) - 32) % 95)
            decoded += Cipher.dictionary[char_num]

        return decoded

    def __str__(self):
        return "Multiplicative Cipher"


'''
x = Multiplicative()

key = x.generate_keys()
m = crypto_utils.modular_inverse(key, 95)
print("Key: ", key)
en = x.encode("Python", key)
de = x.decode(en, key)

print("Encoded: " + en)
print("Decoded: " + x.decode(en, key))

print(x.verify("Python", de))

#'''