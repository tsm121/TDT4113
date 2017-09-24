from cipher import Cipher
import random
import crypto_utils


class Affine(Cipher):
    def __init__(self):

        self.__caesarkey = random.randint(0, 95)

        super(Affine, self).__init__()

    def generate_keys(self):

        mod_key = random.randint(0, 95)

        while True:

            if not crypto_utils.modular_inverse(mod_key, 95):
                print("Making new key...\n")
                mod_key = random.randint(1, 95)

            else:
                return mod_key

    def encode(self, msg, key):

        encoded = ''

        for letter in msg:
            char_num = (((ord(letter) * key) - 32 + self.__caesarkey) % 95)
            encoded += Cipher.dictionary[char_num]

        return encoded

    def decode(self, msg, key):

        decoded = ''
        m = crypto_utils.modular_inverse(key, 95)

        for letter in msg:
            char_num = ((((ord(letter) - self.__caesarkey) * m) - 32) % 95)
            decoded += Cipher.dictionary[char_num]

        return decoded

    def get_caesarkey(self):
        return self.__caesarkey

    def __str__(self):
        return "Affine Cipher"


'''
x = Affine()

mod_key = x.generate_keys()
caesarkey = x.get_caesarkey()
print("Key: ", caesarkey)
print("Mod_Key: ", mod_key)
en = x.encode("Python", mod_key)
de = x.decode(en, mod_key)

print("Encoded: " + en)
print("Decoded: " + de)

print(x.verify("Python", de))

'''