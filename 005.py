"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


found = False
a = 0
while found is False:
    a += 1
    for i in range(1,21):
        if a % i != 0:
            # print('break')
            break
        if i == 20:
            print('found')
            found = True
print(a)

# took a long time using this 'brute force' method
