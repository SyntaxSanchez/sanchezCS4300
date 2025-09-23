# task3.py

def numberSignCheck(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

def primesTen():
    primes = []
    num = 2
    while len(primes) < 10:
        if isPrime(num):
            primes.append(num)
        num += 1
    return primes

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_1_to_100():
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total

