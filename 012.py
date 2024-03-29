""" Project Euler Problem 12
========================

The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
28. The first ten terms would be:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

   1: 1
   3: 1,3
   6: 1,2,3,6
  10: 1,2,5,10
  15: 1,3,5,15
  21: 1,3,7,21
  28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""


def divisors(number):
    count = 0
    for o in range(1, number+1):
        if number % o == 0:
            count = count + 1
    return count


def factors(n):
    result_set = set()
    sqrtn = int(n**0.5)
    for i in range(1, sqrtn+1):
        q, r = n/i, n % i
        if r == 0:
            result_set.add(q)
            result_set.add(i)
    return len(result_set)


def countdiv(a):
    count = 0
    for e in range(1, int((a/2)+1)):
        if a % e == 0:
            count += 1
    return count + 1    # +1 to account for number itself as a divisor

def factorial(number):
    fact = 0
    for o in range(1, number+1):
        fact = fact + o
    return fact


# while divisors(triangle) < 50:
# for i in range(1, 500):


number = 1
while factors(factorial(number)) < 500:
    triangle = factorial(number)
    # print(triangle)
    # print('has ' + str(countdiv(triangle)) + ' divisors')
    # print('('+str(divisors(triangle))+')')
    number = number + 1

print(factorial(number))
