from math import sqrt

def gcd(a, b):
    if b == 0:
        return a
    else:
        while a != 0:
            a, b = b % a, a
        return b

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True

def countPrimitiveRootsAvailable(P):
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
    if (isPrime(P) == False):
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