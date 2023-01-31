from Diffie_Hellman import *
from DH_integrated_RSA import *
from Plain_Text_Processing import *
import time


# Original Diffie Hellman
print('-'*100)
print('Initiation:')
time.sleep(2)
pub_key = (23, 5, 22)
print(f"Alice and Bob have agreed on a set of public keys {pub_key}\n")
print("-"*100)
time.sleep(2)

print('CHOOSING PRIVATE KEY\n')
time.sleep(3)
Alice_pri_key = 6
Alice = Diffie_Hellman(*pub_key, pri_key=Alice_pri_key)
print(f'Alice has chosen her private key: {Alice_pri_key}\n')
time.sleep(3)

Bob_pri_key = 15
Bob = Diffie_Hellman(*pub_key, pri_key=Bob_pri_key)
print(f'Bob has chosen his private key: {Bob_pri_key}\n')
print('-'*100)
time.sleep(3)

print('EXCHANGE OF KEYS period\n')
time.sleep(3)
Alice_pub_key = Alice.send_key()
print(f"Alice's public key: {Alice_pub_key}")
time.sleep(2)
print('Alice is sending her public key to Bob')
print('. . .\n')
time.sleep(4)

Bob.get_key(Alice_pub_key)
print("Bob has received Alice's key\n")
print('-'*50)
time.sleep(3)

Bob_pub_key = Bob.send_key()
print(f"Bob's public key: {Bob_pub_key}")
time.sleep(2)
print('Bob is sending his public key to Alice')
print('. . .\n')
time.sleep(4)

Alice.get_key(Bob_pub_key)
print("Alice has received Bob's key\n")
time.sleep(2)
print('-'*100)
time.sleep(2)

print('\nBoth of Alice and Bob have encrypt and decrypt keys, so they can communicate in private\n\n')
time.sleep(2)

input("Press arbitrary button to close..")