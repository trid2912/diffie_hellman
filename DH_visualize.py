from KeyExchange.Diffie_Hellman import *
from other_func.Key_generator import *
import time


# Original Diffie Hellman
print('-'*100)
print('Initiation:')
p = int(input("Enter a prime number p (23): "))
g = int(input("Enter a generator number g (5): "))

pub_key = (p, g, p-1)
print(f"Alice and Bob have agreed on a set of public keys {pub_key}\n")
print("-"*100)
input()

print('CHOOSING PRIVATE KEY\n')
time.sleep(3)
Alice_pri_key = 6
Alice = Diffie_Hellman(*pub_key, pri_key=Alice_pri_key)
print(f'Alice has chosen her private key: {Alice_pri_key}\n')
input()

Bob_pri_key = 15
Bob = Diffie_Hellman(*pub_key, pri_key=Bob_pri_key)
print(f'Bob has chosen his private key: {Bob_pri_key}\n')
print('-'*100)
input()

print('EXCHANGE OF KEYS period\n')
time.sleep(3)
Alice_pub_key = Alice.send_key()
print(f"Alice's public key: {Alice_pub_key}")
time.sleep(2)
print('Alice is sending her public key to Bob')
print('. . .\n')
time.sleep(4)

B_key = Bob.get_key(Alice_pub_key)
print(f"Bob has received Alice's key: {B_key}\n")
print('-'*50)
input()

Bob_pub_key = Bob.send_key()
print(f"Bob's public key: {Bob_pub_key}")
time.sleep(2)
print('Bob is sending his public key to Alice')
print('. . .\n')
time.sleep(4)

A_key = Alice.get_key(Bob_pub_key)
print(f"Alice has received Bob's key: {A_key}\n")
time.sleep(2)
print('-'*100)
input()

print('\nBoth of Alice and Bob have encrypt and decrypt keys, so they can communicate in private\n\n')
time.sleep(2)

input("Press arbitrary button to close..")