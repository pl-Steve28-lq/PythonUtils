import math

# Greatest Common Divisor
gcd = lambda x, y: math.gcd(x, y)

# Least Common Multiplier
lcm = lambda x, y: (x*y) // gcd(x, y)

# Prime Check Function
def isPrime(n):
    if n == 1: return False
    for k in range(2, int(n**0.5)):
        if n%k == 0: return False
    return True

# Prime List, with Seive of Eratosthenes
def primeList(n):
    seive = [False, False] + [True] * (n-1)
    for k in range(2, int(n**0.5 + 1.5)):
        if seive[k]: seive[k*2::k] = [False] * ( (n-k) // k )
    return [x for x in range(n+1) if seive[x]]

# n-th Prime Function
def Prime(n):
    if n == 1: return 2
    cnt = 1
    num = 1
    while cnt < n:
        num += 2
        if isPrime(num): cnt += 1
    return num

# Factorization of number
def Factorize(n):
    i = 2
    res = {}
    while n%i == 0:
        res[i] = res.get(i, 0) + 1
        n //= i
    i += 1
    while n > 1:
        while n%i == 0:
            res[i] = res.get(i, 0) + 1
            n //= i
        i += 2
    return res

# All factor of number
def Factor(n):
    return list(filter(lambda x:not n%x, range(1, n+1)))

# Mobius Function
def Mobius(n):
    res = Factorize(n).values()
    if len(list(filter(lambda x: x < 2, res))) != len(res): return 0
    else: return (-1) ** len(res)

# Euler-Phi Function
def EulerPhi(n):
    return functools.reduce(lambda x,y: x*(y-1), Factor(n))

# Von Mangoldt Function
def VonMangoldt(n):
    res = Factorize(n)
    if len(res.keys()) != 1: return 0
    return math.log(list(res.keys())[0])
