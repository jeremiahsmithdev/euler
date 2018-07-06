"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def isPrime(x):
    for i in range(2, x):
        for a in range(2, x):
            if i * a == x:
                return False
    return True

def primality(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

counter = 0
i = 2
while(counter<10001):
    if primality(i):
        counter += 1
    i+=1
print(i-1)
