"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


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
s = 0
for i in range(2,2000000):
    if primality(i):
        s = s + i
print(s)
# Checking "010.py" against solution: 142913828922
# Time elapsed: user: 10.8 s, sys: 42.9 ms, total: 10.9 s
