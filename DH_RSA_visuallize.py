from KeyExchange.DH_integrated_RSA import *
from other_func.Key_generator import generate
import time

print('Initiation:')
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
X = int(input("Enter a prime number X: "))
g = int(input("Enter a generator number g: "))

set_of_pri_key = (p, q, X, g)
print(f"\nAlice and Bob have chosen the global elements and the secret large prime numbers: (p, q, X, g) = {set_of_pri_key}")
input()

print('-'*100)
print('Public and Private key Generation:\n')
input()

print(f"n = p * q = {p*q}\n")
input()
phi = (p-1)*(q-1)
print(f"phi(n) = (p - 1)(q - 1) = {phi}\n")
input()

e = generate([2, phi], coprime=phi)
e=13
print(f"1. Alice and Bob have agreed upon the value of e = {e}")
input()

A_pri_key = 4
print(f"2. Alice has selected her private key: {A_pri_key}")
Alice = Diffie_Hellman_RSA(*set_of_pri_key, pri_key=A_pri_key, e=e)
input()

B_pri_key = 3
print(f"3. Bob has selected his private key: {B_pri_key}")
Bob = Diffie_Hellman_RSA(*set_of_pri_key, pri_key=B_pri_key, e=e)
input()

print(f"4. Key to decrypt incoming public key is computed (Using RSA scheme): {Alice.get_decrypt_public_key()}")
input()

A_send_key = Alice.send_key()
A_pub_key = Alice.get_alpha()
print(f"5. Alice has computed her public keys using her own secret keys: {A_pub_key}")
input()

B_send_key = Bob.send_key()
B_pub_key = Bob.get_alpha()
print(f"6. Bob has computed his public keys using his own secret keys: {B_pub_key}\n")
print('-'*100)
input()

print("7. EXCHANGE OF KEYS period")
input()

print(f"(a).Public key of Alice has been encrypted as {A_send_key}\n")
input()

print(f"(b).Public key of Bob has been encrypted as {B_send_key}\n")
input()

print("8. After Decryption:")
input()
Alice.get_key(B_send_key)
print(f"(a).Alice has decrypted public key sent from Bob: {Alice.get_beta()}\n")
input()

Bob.get_key(A_send_key)
print(f"(b).Bob has has decrypted public key sent from Alice: {Bob.get_beta()}\n")
print('-'*100)
input()

print("9.SHARED-SECRET-KEY CALCULATION: GOAL OF DH KEY EXCHANGE")
input()

print(f"(a).Alice has computed shared secret key k1 = {Alice.get_encryptKey()}\n")
input()
print(f"(b).Bob has computed shared secret key k2 = {Bob.get_encryptKey()}\n")

print(f"Shared secret key K = {Alice.get_encryptKey()}")

input()