def isPrime(s):
    i=2
    import math
    while i<=math.sqrt(s):
        if s%i==0:
            return False
        i+=1
    if s%i!=0:
        return True
def isPrime2(s):
    i=2
    while i*i<=s:
        if s%i==0:
            return False
        i+=1
    if s%i!=0:
        return True
def nextPrime(s):
    s+=1
    while isPrime2(s) != True:
        s+=1
    return s
    

def primePos(n):
    res = 2
    for i in range(1,n):
        res = nextPrime(res)
    return res
