from sender import Sender
from receiver import Receiver
from hacker import Hacker
from caesar import Caesar
from multiplicative_cipher import Multiplicative
from affine_cipher import Affine
from unbreakable_cipher import Unbreakable
from RSA_cipher import RSA


def main():
    sender = Sender()
    choose_cipher(sender)

    if isinstance(sender.get_cipher(), RSA):
        receiver = Receiver()
        receiver.set_cipher(sender.get_cipher())
        operate_RSA(sender, receiver)

    else:
        sender.set_key(sender.get_cipher().generate_keys())
        sender.operate_cipher()
        print("Encrypting...")

        receiver = Receiver()
        receiver.set_cipher(sender.get_cipher())
        receiver.set_key(sender.get_key())
        receiver.set_encoded_msg(sender.get_encoded_msg())
        receiver.operate_cipher()

    print("Encoded message from Sender: '" + str(sender.get_encoded_msg()) + "'")
    print("Receiver and Sender uses: " + str(receiver.get_cipher()))
    print("Decrypting...")
    print("'" + str(sender.get_encoded_msg()) + "' was decoded to '" + str(receiver.get_decoded_msg()) + "'")

    print("A wild hacker appeared...")
    hacker = Hacker()
    hacker.read_dic()
    hacker.hack(sender.get_encoded_msg(), sender.get_cipher())

def operate_RSA(se, re):

    re.set_key(re.get_cipher().generate_keys())
    n_temp = re.get_cipher().get_n()
    e_temp = re.get_cipher().get_e()

    #print("RE - n: " + str(n_temp) + " e: " + str(e_temp) + " d: " + str(re.get_key()))
    se.set_key((n_temp, e_temp))
    se.operate_cipher()
    print("Encrypting...")
    re.set_encoded_msg(se.get_encoded_msg())
    re.operate_cipher()


def choose_cipher(sender_object):
    print("Choose cipher method:")
    while True:
        try:
            print("1 = Caesar, 2 = Multiplicative, 3 = Affine, 4 = Unbreakable, 5 = RSA")
            x = int(input(">>> "))
            break

        except:
            print("Wrong input. Chose a number from 1 to 5")

    if x == 1:
        sender_object.set_cipher(Caesar())

    elif x == 2:
        sender_object.set_cipher(Multiplicative())

    elif x == 3:
        sender_object.set_cipher(Affine())

    elif x == 4:
        sender_object.set_cipher(Unbreakable())

    elif x == 5:
        sender_object.set_cipher(RSA())


if __name__ == "__main__":
    main()
