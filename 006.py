"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


Sum = 0
SumS = 0
for i in range(101):
    Sum += i
    SumS += i**2

print(Sum**2 - SumS)

# Checking "006.py" against solution: 25164150
# Time elapsed: user: 10.3 ms, sys: 6.85 ms, total: 17.2 ms
