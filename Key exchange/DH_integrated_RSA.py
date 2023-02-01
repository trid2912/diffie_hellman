import numpy as np

class Diffie_Hellman_RSA(object):
    '''Random generation of large prime numbers: p, q, X; and g such that:
       0 < g < p, 0 < g < q, p != g and g < X
       g: base generator
       p, q: secret and know only to Alice and Bob
       X and g are global elements
       compute: n = pq and phi(n) = (p-1)(q-1)
       Alice and Bob agree on random generated e such that:
       phi(n) > e; phi(n), e > 1; and they are co-primes'''

    def __init__(self, p, q, X, g, pri_key, e):
        assert p != q and p > g and q > g and X > g and pri_key < X

        self.__pri_key = pri_key
        self.__p, self.__q, self.X, self.g = p, q, X, g
        self.__G = X-1 #number of smaller co-prime numbers of X

        self.__n = self.__p * self.__q
        self.__phi = (self.__p - 1) * (self.__q - 1)

        assert self.__phi > e
        self.__e = e

        _, self.__d, _ = self.gcdExtended(self.__e, self.__phi) # d = e^-1 (mod phi(n))

    def send_key(self):
        ''' Send key to other side '''

        self.alpha = self.g**self.__pri_key % self.X #public key

        self.key = self.alpha ** self.__e % self.__n #encrypted public key

        return self.key

    def get_key(self, received_key):
        ''' Take the key sent from the other side and set up a encrypted key '''
        self.received_key = received_key

        self.alpha = self.received_key ** self.__d % self.__n #public key

        self.__encrypt_key = self.alpha ** self.__pri_key % self.X                   # = g^(ab) % X
        self.__decrypt_key = (self.alpha ** (self.__G - self.__pri_key)) % self.X    # ig_ab = g_a^(|G| - b) mod p

    def encrypt_by_merkel_hellman(self, plain):
        ''' Encrypt plain text with shared key (encrypted key) '''
        self.plain = plain
        self.cipher = self.plain*self.__encrypt_key % self.pub_key[0]

        return self.cipher

    def decrypt_by_merkel_hellman(self, cipher):
        ''' Decrypt cipher text with inverse of shared key (decrypted key) '''
        self.cipher = cipher
        self.plain = self.cipher*self.__decrypt_key % self.pub_key[0]

        return self.plain

    def convert_to_binary(self, text):
        bin_text = np.array([[int(j) for j in '{0:05b}'.format((ord(i)-ord('A'))%32)] for i in text]).T

        return bin_text

    def CharConvertAscii(self, s):
        nchars = len(s)
        x = sum(ord(s[byte])<<8*(nchars-byte-1) for byte in range(nchars)) # string to int or long. Type depends on nchars
        return x

    def AsciiConvertChar(self, s):

        x = ''.join(chr((s>>8*(nchars-byte-1))&0xFF) for byte in range(nchars)) # int or long to string
        return x

    def gcdExtended(self, a, b):
        ''' ax + by = 1    =>   x = a^-1 (mod b)'''
        # Base Case
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.gcdExtended(b % a, a)
        # Update x and y using results of recursive
        # call
        x = y1 - (b//a) * x1
        y = x1

        return gcd, x, y

#Test

p, q, X, g = 13, 17, 23, 11

Alice = Diffie_Hellman_RSA(p=p, q=q, X=X, g=g, pri_key=4, e=13)
Bob = Diffie_Hellman_RSA(p=p, q=q, X=X, g=g, pri_key=3, e=13)

Bob.get_key(Alice.send_key())
Alice.get_key(Bob.send_key())
