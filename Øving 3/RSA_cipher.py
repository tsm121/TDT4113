from cipher import Cipher
from crypto_utils import generate_random_prime, modular_inverse, blocks_from_text, text_from_blocks
import random


class RSA(Cipher):
    def __init__(self):

        super(RSA, self).__init__()

        self.__n = None
        self.__e = None

    def generate_keys(self):

        while True:
            while True:
                p = generate_random_prime(16)
                q = generate_random_prime(16)

                if p != q:
                    break

            n_temp = p * q
            phi_temp = (p - 1) * (q - 1)
            e_temp = random.randint(3, phi_temp-1)
            d_temp = modular_inverse(e_temp, phi_temp)

            if d_temp is not False:

                self.set_e(e_temp)
                self.set_n(n_temp)
                #print("e: " + str(self.__e) + " n: " + str(self.__n) + " d: " + str(d_temp))

                return n_temp, d_temp

    def encode(self, msg, key):

        n, e = key
        c = []

        int_blocks = blocks_from_text(msg, 3)

        for t in range(len(int_blocks)):

            c.append(pow(int_blocks[t], e, n))

        return c

    def decode(self, c_blocks, key):

        n, d = key
        text_block = []

        for c in c_blocks:

            text_block.append(pow(c, d, n))

        return text_from_blocks(text_block, 16)

    def get_n(self):
        return self.__n

    def get_e(self):
        return self.__e

    def set_n(self, n):
        self.__n = n

    def set_e(self, e):
        self.__e = e

    def __str__(self):
        return "RSA Cipher"

'''
x = RSA()
d = x.generate_keys()
n = x.get_n()
e = x.get_e()
print("d: " + str(d) + " n: " + str(n) + " e: " + str(e))
en = x.encode("Pythonafdsjiofsd", (n, e))
print(en)
de = x.decode(en, (n, d))
print(de)
'''