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

    def __init__(self, n, g, G, pri_key):
        self.n, self.g, self.G = n, g, G # [n, g, |G|] list of natural number n and generate element g in cyclic group G
        self.__pri_key = pri_key         # a random private number

    def send_key(self):
        ''' Send key to other side '''
        return self.g ** self.__pri_key % self.n

    def get_key(self, received_key):
        ''' Take the key sent from the other side and set up a encrypted key '''
        self.received_key = received_key
        self.__encrypt_key = self.received_key**self.__pri_key % self.n                   # g_ab = (g_a)^b mod p
        self.__decrypt_key = (self.received_key**(self.G - self.__pri_key)) % self.n    # ig_ab = g_a^(|G| - b) mod p
        
        return(self.__decrypt_key)

    def encrypt(self, plain):
        ''' Encrypt plain text with shared key (encrypted key) '''
        self.plain = plain
        self.cipher = self.plain * self.__encrypt_key % self.n

        return self.cipher

    def decrypt(self, cipher):
        ''' Decrypt cipher text with inverse of shared key (decrypted key) '''
        self.cipher = cipher
        self.plain = self.cipher*self.__decrypt_key % self.n

        return self.plain