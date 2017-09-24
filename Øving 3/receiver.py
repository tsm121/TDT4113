from person import Person


class Receiver(Person):
    def __init__(self):
        super(Person, self).__init__()
        self.__decoded_msg = ''

    def operate_cipher(self):

        self.set_decoded_msg(self.get_cipher().decode(self.get_encoded_msg(), self.get_key()))

    def get_decoded_msg(self):

        return self.__decoded_msg

    def set_decoded_msg(self, decoded_msg):
        self.__decoded_msg = decoded_msg
