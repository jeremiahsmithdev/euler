"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


largest = 0
for i in range(100,1000):
    for a in range(100,1000):
        b = i * a
        if str(b)[::-1] == str(b):
            if b > largest:
                largest = b
print(largest)
