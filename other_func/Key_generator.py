import random as rd
from Check_key import isPrime

def generate(ranges=[], prime=False):
    if prime:
        primes = [i for i in range(*ranges) if isPrime(i)]
        n = rd.choice(primes)
    else:
        return rd.randrange(*ranges)