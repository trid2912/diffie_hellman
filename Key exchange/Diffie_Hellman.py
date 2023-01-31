import numpy as np

class Diffie_Hellman(object):    
    """
    1. Alice and Bob agree on a natural number n and a generating element g in the finite cyclic group G of order n.
       (This is usually done long before the rest of the protocol; g is assumed to be known by all attackers.)
       The group G is written multiplicatively.
    2. Alice picks a random natural number a with 1 < a < n, and sends the element ga of G to Bob.
    3. Bob picks a random natural number b with 1 < b < n, and sends the element gb of G to Alice.
    4. Alice computes the element (gb)a = gba of G.
    5. Bob computes the element (ga)b = gab of G.
    """

    def __init__(self, pub_key, pri_key):
        self.pub_key = pub_key # [n, g, |G|] list of natural number n and generate element g in cyclic group G
        self.__pri_key = pri_key # a random private number

    def send_key(self):
        ''' Send key to other side '''
        return self.pub_key[1] ** self.__pri_key % self.pub_key[0]

    def get_key(self, received_key):
        ''' Take the key sent from the other side and set up a encrypted key '''
        self.received_key = received_key
        self.__encrypt_key = self.received_key**self.__pri_key % self.pub_key[0]                             # g_ab = (g_a)^b mod p
        self.__decrypt_key = (self.received_key**(self.pub_key[-1] - self.__pri_key)) % self.pub_key[0] # ig_ab = g_a^(|G| - b) mod p

    def convert_to_binary(self, text):
        bin_text = np.array([[int(j) for j in '{0:05b}'.format((ord(i)-ord('A'))%32)] for i in text]).T

        return bin_text
    
    def CharConvertAscii(text):                # nhỡ người dùng có nhập chữ, không thì bỏ đi cho hiện TypeError cũng được
        text = input()
        nchars = len(text)
        output = sum(ord(text[byte])<<8*(nchars-byte-1) for byte in range(nchars)) # string to int or long. Type depends on nchars
        ''.join(chr((output>>8*(nchars-byte-1))&0xFF) for byte in range(nchars)) # int or long to string
        return output

    def encrypt(self, plain):
        ''' Encrypt plain text with shared key (encrypted key) '''
        self.plain = plain
        self.cipher = self.plain*self.__encrypt_key % self.pub_key[0]

        return self.cipher

    def decrypt(self, cipher):
        ''' Decrypt cipher text with inverse of shared key (decrypted key) '''
        self.cipher = cipher
        self.plain = self.cipher*self.__decrypt_key % self.pub_key[0]

        return self.plain


Alice = Diffie_Hellman(pub_key=[23, 5, 23], pri_key=6)
Bob = Diffie_Hellman(pub_key=[23, 5, 23], pri_key=15)

Alice.get_key(Bob.send_key())
Bob.get_key(Alice.send_key())

