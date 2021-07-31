"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


sum = 0
for i in range(1000):
    if i % 3 == 0:
        a = i
    if i % 5 == 0:
        a = i

    sum += a
    # print(a)
    a = 0

print(sum)

# Checking "001.py" against solution: 233168
# Time elapsed: user: 12 ms, sys: 9.35 ms, total: 21.3 ms
print something
