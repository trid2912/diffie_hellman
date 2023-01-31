from DH_integrated_RSA import *
import time

print('Initiation:')
time.sleep(2)
set_of_pri_key = (13, 11, 23, 9)
print(f"Alice and Bob have chosen the global elements and the secret large prime numbers: (p, q, X, g) = {set_of_pri_key}")
input()

print('-'*100)
print('Public and Private key Generation:')
time.sleep(3)

e = 13
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

print(f"4. Key to decrypt incoming public key is computed (Using RSA scheme)")
input()

print(f"5. Alice and Bob have computed their public keys using their own secret keys: {A_pri_key} and {B_pri_key}\n")
time.sleep(2)
print('-'*100)
input()

print("6. EXCHANGE OF KEYS period")
input()
A_pub_key = Alice.send_key()
print(f"(a). Public key of Alice encrypted as {A_pub_key}\n")
time.sleep(3)

B_pub_key = Bob.send_key()
print(f"(b).Public key of Bob encrypted as {B_pub_key}\n")
input()

print("7. After Decryption:")
input()
Alice.get_key(B_pub_key)
print(f"(a).Alice has received {Alice.get_beta()} from Bob\n")
time.sleep(2)

Bob.get_key(A_pub_key)
print(f"(b).Bob has received {Bob.get_beta()} from Alice\n")
print('-'*100)
input()

print("8.SHARED-SECRET-KEY CALCULATION: GOAL OF DH KEY EXCHANGE")
input()

print(f"(a).Alice has computed shared secret key k1 = {Alice.get_encryptKey()}\n")
time.sleep(2)
print(f"(b).Bob has computed shared secret key k2 = {Bob.get_encryptKey()}\n")

print(f"Shared secret key K = {Alice.get_encryptKey()}")