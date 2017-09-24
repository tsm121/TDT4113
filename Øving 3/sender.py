from person import Person

class Sender(Person):

    def __init__(self):
        super(Person, self).__init__()

    def operate_cipher(self):
        print("Write message to encode:")
        msg = input(">>> ")

        self.set_encoded_msg(self.get_cipher().encode(msg, self.get_key()))

#x = Sender()
#x.operate_cipher()
#print(x.get_cipher())
