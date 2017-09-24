

class Cipher:

    dictionary = {0: ' ', 1: '!', 2: '"', 3: '#', 4: '$', 5: '%', 6: '&', 7: "'", 8: '(', 9: ')',
           10: '*', 11: '+', 12: ',', 13: '-', 14: '.', 15: '/', 16: '0', 17: '1', 18: '2',
           19: '3', 20: '4', 21: '5', 22: '6', 23: '7', 24: '8', 25: '9', 26: ':', 27: ';',
           28: '<', 29: '=', 30: '>', 31: '?', 32: '@', 33: 'A', 34: 'B', 35: 'C', 36: 'D',
           37: 'E', 38: 'F', 39: 'G', 40: 'H', 41: 'I', 42: 'J', 43: 'K', 44: 'L', 45: 'M',
           46: 'N', 47: 'O', 48: 'P', 49: 'Q', 50: 'R', 51: 'S', 52: 'T', 53: 'U', 54: 'V',
           55: 'W', 56: 'X', 57: 'Y', 58: 'Z', 59: '[', 60: '\\', 61: ']', 62: '^', 63: '_',
           64: '`', 65: 'a', 66: 'b', 67: 'c', 68: 'd', 69: 'e', 70: 'f', 71: 'g', 72: 'h',
           73: 'i', 74: 'j', 75: 'k', 76: 'l', 77: 'm', 78: 'n', 79: 'o', 80: 'p', 81: 'q',
           82: 'r', 83: 's', 84: 't', 85: 'u', 86: 'v', 87: 'w', 88: 'x', 89: 'y', 90: 'z',
           91: '{', 92: '|', 93: '}', 94: '~'}

    def __init__(self):
        pass

    def generate_keys(self):
        pass

    def verify(self, msg, decoded):

        if msg == decoded:
            return True

        return False

    def encode(self, msg, key):
        pass

    def decode(self, msg, key):
        pass

    def check_msg(self, msg):

        for x in msg:

            if ord(x) < 32 or ord(x) > 126:
                print("An invalid letter is used")
                return False

            else:
                return True
