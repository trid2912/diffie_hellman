import random as rd
from other_func.Check_key import isPrime, gcd

def generate(ranges=[], prime=False, coprime=False):
    if prime:
        interval = [i for i in range(*ranges) if isPrime(i)]
        n = rd.choice(interval)
        return n
    elif coprime:
        interval = [i for i in range(*ranges) if (gcd(i, coprime)==1)]
        n = rd.choice(interval)
        return n 
    else:
        return rd.randrange(*ranges)