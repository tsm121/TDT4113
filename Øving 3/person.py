
class Person:

    def __init__(self):
        self.__key = 0
        self.__cipher = None
        self.__encoded_msg = ''

    def set_encoded_msg(self, encoded_msg):
        self.__encoded_msg = encoded_msg

    def get_encoded_msg(self):
        return self.__encoded_msg

    def set_key(self, key):

        self.__key = key

    def get_key(self):

        return self.__key

    def set_cipher(self, cipher):

        self.__cipher = cipher

    def get_cipher(self):

        return self.__cipher

    def operate_cipher(self):
        pass
