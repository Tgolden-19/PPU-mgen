import math

def isPrime(n):
    bound = int(math.sqrt(n))
    for i in range(2, bound + 1):
        if int(n / i) == (n / i):
            return False
    return True

def generatePrimes(n):
    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    return primes

def zetaSeries(n, s):
    sum = 0
    for x in range(n):
        if x!=0:
            sum += 1/(x**s)

    return sum

def primeProduct(n, s):
    prod = 1
    primes = generatePrimes(n)
    for x in range(len(primes)):
        prim = primes[x]
        prod = prod * 1/(1-(1/(prim**s)))

    return prod

def main():
    print(generatePrimes(50))
    n = 1000
    s = 5
    print("zetaSeries = " + str(zetaSeries(n, s)))
    print("primeProduct = " + str(primeProduct(n, s)))


if __name__ == '__main__':
    main()