from cipher import Cipher


class Unbreakable(Cipher):
    def __init__(self):

        super(Unbreakable, self).__init__()

        self.key_word = ''

    def generate_keys(self):

        self.key_word = input("What is the keyword?").lower()
        return self.key_word

    def encode(self, msg, key):

        key_word_mod = self.key_edit(len(msg), key)
        encoded = ''

        for i in range(len(msg)):
            key_num = (ord(key_word_mod[i]) - 32) % 95
            char_num = (ord(msg[i]) - 32 + key_num) % 95
            encoded += Cipher.dictionary[char_num]

        return encoded

    def decode(self, msg, key):

        decoded = ''
        dec_word = ''

        for x in range(len(key)):
            key_word_num = (95 - (ord(key[x]) - 32)) % 95
            dec_word += Cipher.dictionary[key_word_num]

        dec_word_mod = self.key_edit(len(msg), dec_word)

        for i in range(len(msg)):
            char_num = ((ord(msg[i]) - 32) + (ord(dec_word_mod[i]) - 32)) % 95
            decoded += Cipher.dictionary[char_num]

        return decoded

    def key_edit(self, length, key):

        key_word_mod = ''
        for x in range(length):

            j = x % (len(key))
            key_word_mod += key[j]

        return key_word_mod

    def __str__(self):
        return "Unbreakable Cipher"

#x = Unbreakable()
#key = x.generate_keys()
#enc = x.encode("HEMMELIGHET", key)
#print(x.decode(enc, key))
