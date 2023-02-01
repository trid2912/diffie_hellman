from random import randint
from math import sqrt

P = input("Please enter input PK P: ")
G = input("Please enter input PK G: ")
publickey = [P, G]

def CharConvertAscii(s):                # nhỡ người dùng có nhập chữ, không thì bỏ đi cho hiện TypeError cũng được
    s = input()
    nchars = len(s)
    x = sum(ord(s[byte])<<8*(nchars-byte-1) for byte in range(nchars)) # string to int or long. Type depends on nchars
    ''.join(chr((x>>8*(nchars-byte-1))&0xFF) for byte in range(nchars)) # int or long to string
    return x

def checkInt(x):
    flag = True
    for var in publickey:
        try:
            int(var)
        except ValueError:
            flag = False
    if flag:
        x = CharConvertAscii(x)
        
def gcd(a, b):
    if b == 0:
        return a
    else:
        while a != 0:
            a, b = b % a, a
        return b

def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True

def countPrimitiveRootsAvailable(P):    #number of relatively prime in range(2,P)
    result = 1
    for i in range(2, P, 1):
        if (gcd(i, P) == 1):
            result += 1
 
    return result

def primefactorize(fac, n) :
    while (n % 2 == 0) :
        fac.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0) :
            fac.add(i)
            n = n // i
    if (n > 2) :
        fac.add(n)

def checkPrimitiveRoot(P,G):
    s = set()
    s1 = set()                   #tập chứa thừa số nguyên tố của P
    if (isprime(P) == False):
        return -1
    phi = P - 1
    primefactorize(s, phi)                          #căn nguyên thủy: 
    for r in range(2, P):                           #đầu tiên phải tìm tập thừa số nguyên tố của n -> số thừa số này là m
        for prif in s:                              #cho từng thừa số vào phép đồng dư để check: M^k(mod n)  
            if (pow(r, phi // prif, P) == 1):       # k chạy đến n, nếu mà số kết quả đồng dư trong 1 loop (giá trị đồng dư sẽ liên tục lặp lại)
                flag = True                         # mà bằng với giá trị m thì tức là thừa số nguyên tố đó là căn nguyên thủy của m
                break
        if (flag == False):
            s1.append(r)
            return r
    if G in s1:
        return("G is the primitive root of P, Public keys are satisfied to make the cryptosystem.")

def main():
    checkInt(P)
    checkInt(G)
    isprime(int(P))
    isprime(int(G))
    checkPrimitiveRoot(int(P),int(G))
    

if __name__ == '__main__':
    main()
    #P = 23
    #G = 9
    print("The Value of Public keys are :%d, %d" %(15) %(20))
     
    # Alice will choose the private key a
    # a = 4
    a = int(input("Enter the private key of Alice: "))
    print('The Private Key a for Alice is :%d'%(a))
    # Bob will choose the private key b
    # b = 3
    b = int(input("Enter the private key of Bob: "))
    print('The Private Key b for Bob is :%d'%(b))
    print("All ingredients are available!!")

    # computing the generated key to be public values to exchange to each other
    x = int(pow(G,a,P)) 
    y = int(pow(G,b,P)) 
    
    print('Bob got the public key is :%d'%(x))
    print('Alice got the public key is :%d'%(y))

    # Secret key Alice back-off computing:
    ska = int(pow(y,a,P))
    # Secret key for Bob computing:
    skb = int(pow(x,b,P))
     
    print('Secret key for the Alice is : %d'%(ska))
    print('Secret key for the Bob is : %d'%(skb))

    if ska == skb:
        print("The encryption is satisfied. Well done 2 nerdies!")