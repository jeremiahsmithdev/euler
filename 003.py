"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def isPrime(x):
    for i in range(2, x):
        for a in range(2, x):
            if i * a == x:
                return False

    return True

# print(isPrime(8))

largest = 0
for i in range(2, 600851475143):
    if 600851475143 % i == 0:
        if isPrime(i):
            # print(str(i) + ' is a prime factor')
            if i > largest:
                largest = i
print(largest)
# error calling...
