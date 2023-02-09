import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

from KeyExchange.DH_integrated_RSA import *
from KeyExchange.Diffie_Hellman import *
from other_func.Key_generator import *
import time
from Attack.MITM import A, B 
from Attack.bruteForce import calculate
import time
from other_func.Check_key import *


class MainWindow(QMainWindow):
    def __init__(self, name = "main") :
        super(MainWindow,self).__init__()
        if name == "RSA":
            loadUi("D:/diffie_hellman/Demonstration/DH_RSA_window.ui", self)
            self.pushButton.clicked.connect(self.RSAClick)
            self.backButton.clicked.connect(self.back)

        elif name == "main":
            loadUi("D:/diffie_hellman/Demonstration/main_window.ui", self)
            self.ChangeWindow1.clicked.connect(self.screen1)
            self.ChangeWindow2.clicked.connect(self.screen2)
            self.ChangeWindow3.clicked.connect(self.screen3)
        elif name == "DH":
            loadUi("D:/diffie_hellman/Demonstration/DH_window.ui", self)
            self.startButton.clicked.connect(self.pushClick)
            self.backButton.clicked.connect(self.back)

        elif name == "MITM":
            loadUi("D:\diffie_hellman\Demonstration\MITM_window.ui", self)
            self.backButton.clicked.connect(self.back)
            self.pushButton.clicked.connect(self.mitm)
            self.bruteforce.clicked.connect(self.brute_force)

    def brute_force(self):
        
        base = int(self.G_input.text())
        
        mod = int(self.p_input.text())

        alice = A(int(self.A_PKey_input.text()), base, mod)

        equal = alice.publish()
        exponent = 1
        start = time.time()
        while True:
            self.Log.addItem("trying " + str(exponent))
            result_list = []
            power_list = []
            while True:
                max_power = 0
                for i in power_list:
                    max_power += int(i)
                #print("max_power=" + str(max_power))
                exponent1 = exponent - max_power
                if exponent1 > 0:
                    result, two_power = calculate(exponent1, base, mod)
                else:
                    break
                result_list.append(result)
                power_list.append(two_power)
                #print("result_list=" + str(result_list))
                #print("power_list=" + str(power_list) + "\n")

            result = result_list[0]
            if len(result_list) == 1:
                result = result % mod
            else:
                for i in range(0, len(result_list) - 1):
                    result = (result * result_list[i+1]) % mod
            if result == equal:
                break
            exponent += 1

        self.Log.addItem("found e=" + str(exponent))
        self.Log.addItem("Time taken: " + str(time.time()- start))
    
    def mitm(self):
        p = int(self.p_input.text())
        g = int(self.G_input.text())
        alice = A(int(self.A_PKey_input.text()), g, p)
        bob = A(int(self.B_PKey_input.text()), g, p)
        eve = B(g,p)
        self.Log.addItem(f'Alice selected (a) : {alice.n}')
        self.Log.addItem(f'Bob selected (b) : {bob.n}')
        self.Log.addItem(f'Eve selected private number for Alice (c) : {eve.a}')
        self.Log.addItem(f'Eve selected private number for Bob (d) : {eve.b}')

        # Generating public values
        ga = alice.publish()
        gb = bob.publish()
        gea = eve.publish(0)
        geb = eve.publish(1)
        self.Log.addItem(f'Alice published (ga): {ga}')
        self.Log.addItem(f'Bob published (gb): {gb}')
        self.Log.addItem(f'Eve published value for Alice (gc): {gea}')
        self.Log.addItem(f'Eve published value for Bob (gd): {geb}')

        # Computing the secret key
        sa = alice.compute_secret(gea)
        sea = eve.compute_secret(ga,0)
        sb = bob.compute_secret(geb)
        seb = eve.compute_secret(gb,1)
        self.Log.addItem(f'Alice computed (S1) : {sa}')
        self.Log.addItem(f'Eve computed key for Alice (S1) : {sea}')
        self.Log.addItem(f'Bob computed (S2) : {sb}')
        self.Log.addItem(f'Eve computed key for Bob (S2) : {seb}')
    def pushClick(self):
        pub_key = (int(self.p_input.text()), int(self.G_input.text()),int(self.p_input.text()) - 1 )
        Alice_pri_key = int(self.A_PKey_input.text())
        Bob_pri_key = int(self.B_PKey_input.text())
        self.Log.addItem(f"Alice and Bob have agreed on a set of public keys {pub_key[0], pub_key[1]}")
        self.Log.addItem(f'Alice has chosen her private key: {Alice_pri_key}')
        self.Log.addItem(f'Bob has chosen his private key: {Bob_pri_key}')
        self.Log.addItem('-'*100)

        Alice = Diffie_Hellman(*pub_key, pri_key=Alice_pri_key)
        Bob = Diffie_Hellman(*pub_key, pri_key=Bob_pri_key)

        self.Log.addItem('EXCHANGE OF KEYS period')
        Alice_pub_key = Alice.send_key()
        self.Log.addItem(f"Alice's public key: {Alice_pub_key}")
        self.Log.addItem('Alice is sending her public key to Bob')
        self.Log.addItem('. . .')
        

        B_key = Bob.get_key(Alice_pub_key)
        self.Log.addItem(f"Bob has received Alice's key: {B_key}\n")
        self.Log.addItem('-'*50)
    
        Bob_pub_key = Bob.send_key()
        self.Log.addItem(f"Bob's public key: {Bob_pub_key}")
        
        self.Log.addItem('Bob is sending his public key to Alice')
        self.Log.addItem('. . .\n')

        A_key = Alice.get_key(Bob_pub_key)
        self.Log.addItem(f"Alice has received Bob's key: {A_key}\n")
        self.Log.addItem('-'*100)

        self.Log.addItem('\nBoth of Alice and Bob have encrypt and decrypt keys, so they can communicate in private\n\n')

    def screen1(self):
        nextwindow = MainWindow("DH")
        widget.addWidget(nextwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def screen2(self):
        nextwindow = MainWindow("RSA")
        widget.addWidget(nextwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def screen3(self):
        nextwindow = MainWindow("MITM")
        widget.addWidget(nextwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def back(self):
        
        nextwindow = MainWindow("main")
        widget.addWidget(nextwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def RSAClick(self):
        self.Log.addItem('Initiation:')
        p = int(self.P_input.text())
        q = int(self.Q_input.text())
        X = int(self.X_input.text())
        g = int(self.G_input.text())

        set_of_pri_key = (p, q, X, g)
        self.Log.addItem(f"\nAlice and Bob have chosen the global elements and the secret large prime numbers: (p, q, X, g) = {set_of_pri_key}")

        self.Log.addItem('-'*100)
        self.Log.addItem('Public and Private key Generation:\n')

        self.Log.addItem(f"n = p * q = {p*q}\n")
        
        phi = (p-1)*(q-1)
        self.Log.addItem(f"phi(n) = (p - 1)(q - 1) = {phi}\n")
        

        e = generate([2, phi], coprime=phi)
        self.Log.addItem(f"1. Alice and Bob have agreed upon the value of e = {e}")

        A_pri_key = int(self.A_PKey_input.text())
        self.Log.addItem(f"2. Alice has selected her private key: {A_pri_key}")
        Alice = Diffie_Hellman_RSA(*set_of_pri_key, pri_key=A_pri_key, e=e)
        

        B_pri_key = int(self.B_PKey_input.text())
        self.Log.addItem(f"3. Bob has selected his private key: {B_pri_key}")
        Bob = Diffie_Hellman_RSA(*set_of_pri_key, pri_key=B_pri_key, e=e)

        self.Log.addItem(f"4. Key to decrypt incoming public key is computed (Using RSA scheme): {Alice.get_decrypt_public_key()}")

        A_send_key = Alice.send_key()
        A_pub_key = Alice.get_alpha()
        self.Log.addItem(f"5. Alice has computed her public keys using her own secret keys: {A_pub_key}")

        B_send_key = Bob.send_key()
        B_pub_key = Bob.get_alpha()
        self.Log.addItem(f"6. Bob has computed his public keys using his own secret keys: {B_pub_key}\n")
        self.Log.addItem('-'*100)

        self.Log.addItem("7. EXCHANGE OF KEYS period")

        self.Log.addItem(f"(a).Public key of Alice has been encrypted as {A_send_key}\n")

        self.Log.addItem(f"(b).Public key of Bob has been encrypted as {B_send_key}\n")

        self.Log.addItem("8. After Decryption:")
        
        Alice.get_key(B_send_key)
        self.Log.addItem(f"(a).Alice has decrypted public key sent from Bob: {Alice.get_beta()}\n")

        Bob.get_key(A_send_key)
        self.Log.addItem(f"(b).Bob has has decrypted public key sent from Alice: {Bob.get_beta()}\n")
        self.Log.addItem('-'*100)
       

        self.Log.addItem("9.SHARED-SECRET-KEY CALCULATION: GOAL OF DH KEY EXCHANGE")

        self.Log.addItem(f"(a).Alice has computed shared secret key k1 = {Alice.get_encryptKey()}\n")
        
        self.Log.addItem(f"(b).Bob has computed shared secret key k2 = {Bob.get_encryptKey()}\n")

        self.Log.addItem(f"Shared secret key K = {Alice.get_encryptKey()}")

        

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.addWidget(MainWindow("main"))

widget.show()
sys.exit(app.exec_())

